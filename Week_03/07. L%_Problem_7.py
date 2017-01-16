'''
L5 Problem 7
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 6 minutes

For this problem, write a recursive function, lenRecur, which computes the length of an input argument (a string), by counting up the number of characters in the string.

Hint: String slicing may be useful in this problem...
'''
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    s = aStr
    sLen = 0
    
    if s == '':
        return 0
    else:
        return 1 + lenRecur(s[0:-1])