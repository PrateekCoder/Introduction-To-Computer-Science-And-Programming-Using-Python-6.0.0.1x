'''
L12 Problem 5
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 10 minutes

Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
'''

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


##for/else clause
##http://freetstar.com/python-whilefor-loop-else-clause/
def forElse(x):    
    for x in range(1,5):
        if x == 6 :
           print "found the number",x
           break
    else:
         print "not found!"