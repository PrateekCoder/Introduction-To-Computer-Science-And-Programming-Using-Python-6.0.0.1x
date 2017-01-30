'''
Problem 1: Encryption (applyCoder)
15.0/15.0 points (graded)
Next, define the function applyCoder, which applies a coder to a string of text.

Test Cases

>>> applyCoder("Hello, world!", buildCoder(3))
'Khoor, zruog!'
>>> applyCoder("Khoor, zruog!", buildCoder(23))
'Hello, world!'
'''

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    result = []
    for i in text:
        if i in string.punctuation or i ==' ' or i in string.digits:
            result.append(i)
        else:
            result.append(coder[i])
    result = ''.join(result)
    return result