'''
Problem 1: Encryption (buildCoder)
15.0/15.0 points (graded)
You'll now write a program to encrypt plaintext into ciphertext using the Caesar cipher.

Be sure you have fully read and understood the introduction to this problem!
'''

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    letter = []
    for low in string.ascii_lowercase:
        letter.append(low)
##    for upper in string.ascii_uppercase:
##        letter.append(upper)

    numKeyDict = {}
    num = 1
    for letter1 in letter:
        numKeyDict[num] = letter1
        num += 1

    letterKeyDict = {}
    numNew = 1
    for letter2 in letter:
        letterKeyDict[letter2] = numNew
        numNew += 1    
       
    newDict = {}
    for original in letterKeyDict:
        originalVal = letterKeyDict[original]
        if originalVal + shift > 26:
            originalVal -= 26
        newDict[original] = numKeyDict[originalVal+shift]
        newDict[original.upper()] = numKeyDict[originalVal+shift].upper()
    return newDict