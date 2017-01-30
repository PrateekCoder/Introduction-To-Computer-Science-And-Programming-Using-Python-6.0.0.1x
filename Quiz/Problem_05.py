'''
Problem 5
10.0/10.0 points (graded)
Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order. A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.

def primesList(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # Your code here
    
'''

def primesList(N):
    '''
    N: an integer
    '''
    if N==2: return [2]
    elif N<2: return []
    s=range(3,N+1,2)
    mroot = N ** 0.5
    half=(N+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]