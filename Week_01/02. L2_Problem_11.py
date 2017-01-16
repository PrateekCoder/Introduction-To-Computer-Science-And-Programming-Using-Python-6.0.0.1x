'''
Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that prints out one of the following messages:

"string involved" if either varA or varB are strings

"bigger" if varA is larger than varB

"equal" if varA is equal to varB

"smaller" if varA is smaller than varB

For problems such as these, do not include raw_input statements or define the variable varA or varB. Our automating testing will provide values of varA and varB for you - so write 
your code in the following box assuming varA and varB are already defined.
'''

if type(varA)==str or type(varB)==str:
    print("string involved")

elif varA>varB:
        print("bigger")
    
elif varA==varB:
        print("equal")
        
else:
        print("smaller")