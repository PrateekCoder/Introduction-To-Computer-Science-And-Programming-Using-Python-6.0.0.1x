'''
Problem 4 - Part 1
5.0/5.0 points (graded)
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a⋅x2+b⋅x+c.

This function takes in four numbers and returns a single number.
'''

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return ((a*(x*x))+(b*x)+c)
