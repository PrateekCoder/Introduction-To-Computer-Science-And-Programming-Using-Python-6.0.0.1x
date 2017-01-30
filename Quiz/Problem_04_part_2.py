'''
Problem 4 - Part 2
5.0/5.0 points (graded)
Write a Python function, twoQuadratics, that takes in two sets of coefficients and x-values and prints the sum of the results of evaluating two quadratic equations. It does not do anything else. That is, you should evaluate and print the result of the following equation: a1∗x12+b1∗x1+c1+a2∗x22+b2∗x2+c2
You should use the evalQuadratic function you defined in the "Quadratic" problem of these exercises (you don't need to redefine evalQuadratic in this box; when you call evalQuadratic, our definition will be used).

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
  # Your code here  
If you are getting this problem incorrect, re-read the problem statement carefully.
'''


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    print(evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2 ,c2, x2))
           