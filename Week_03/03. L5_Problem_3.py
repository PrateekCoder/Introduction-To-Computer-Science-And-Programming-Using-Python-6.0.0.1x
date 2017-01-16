'''
L5 Problem 3
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 10 minutes

The function recurPower(base, exp) from Problem 2 computed baseexp by decomposing the problem into one recursive case and one base case:

baseexp=base⋅baseexp−1ifexp>0baseexp=1ifexp=0

Another way to solve this problem just using multiplication (and remainder) is to note that

baseexp=(base2)exp2ifexp>0andexpisevenbaseexp=base⋅baseexp−1ifexp>0andexpisoddbaseexp=1ifexp=0

Write a procedure recurPowerNew which recursively computes exponentials using this idea.
'''

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp==0:
        return 1
    elif exp==1:
        return base
    elif exp%2==0:
        return recurPowerNew(base*base, exp/2)
    elif exp%2!=0:
        return base*recurPowerNew(base, exp-1)