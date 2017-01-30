'''
Problem 6-2
10.0/10.0 points (graded)
Now assume that you have a working insert procedure. Starting with any Frob in a doubly linked list, we would like to find the "front" Frob, i.e., the one whose name is closest to the beginning of the alphabet. Write a recursive function called findFront to do this. findFront should take as an argument any Frob that is part of a doubly linked list.
'''

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if (start.getBefore()==None):
        return start
    else:
        return findFront(start.getBefore())