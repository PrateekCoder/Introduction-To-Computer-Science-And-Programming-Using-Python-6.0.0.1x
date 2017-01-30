'''
Problem 1: Encryption (applyShift)
5.0/5.0 points (graded)
Once you have written buildCoder and applyCoder, you should be able to use them to encode strings.

Test Cases

>>> applyShift('This is a test.', 8)
'Bpqa qa i bmab.'
>>> applyShift('Bpqa qa i bmab.', 18)
'This is a test.'
'''

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

##>>> applyShift('This is a test.', 8)
##'Bpqa qa i bmab.'
##>>> applyShift('Bpqa qa i bmab.', 18)
##'This is a test.'
#

# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    text: string
    returns: 0 <= int < 26
    """
    maxNum = 0
    bestShift = 0
    shStr = ''
    wordCount = 0

    def split(text):
        ex = string.punctuation + string.digits
        for i in text:
            if i in ex:
                text = text.replace(i,'')
        return text.split(' ')

    for shift in range(26):
        shStr = applyShift(text, shift)
        strList = split(shStr)

        for word in strList:
            if isWord(wordList, word):
                wordCount += 1
                
        if wordCount > maxNum:
            maxNum = wordCount
            bestShift = shift

    return bestShift
