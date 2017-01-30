'''
L11 Problem 6
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 20 minutes

For this exercise, you will be coding your very first class, a Queue class. Queues are a fundamental computer science data structure. A queue is basically like a line at Disneyland - you can add elements to a queue, and they maintain a specific order. When you want to get something off the end of a queue, you get the item that has been in there the longest (this is known as 'first-in-first-out', or FIFO). You can read up on queues at Wikipedia if you'd like to learn more.

In your Queue class, you will need three methods:

__init__: initialize your Queue (think: how will you store the queue's elements? You'll need to initialize an appropriate object attribute in this method)
insert: inserts one element in your Queue
remove: removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError.
When you're done, you should test your implementation. Your results should look something like this:

>>> queue = Queue()
>>> queue.insert(5)
>>> queue.insert(6)
>>> queue.remove()
5
>>> queue.insert(7)
>>> queue.remove()
6
>>> queue.remove()
7
>>> queue.remove()
Traceback (most recent call last):
  File "<stdin>", line 26, in <module>
  File "queue.py", line 15, in remove
    raise ValueError()
ValueError
Be sure to handle that last case correctly - when popping from an empty Queue, throw the appropriate error.
'''

class Queue(object):
    def __init__(self):
        self.qlist = []

    def insert(self, e):
        self.qlist.append(e)
            
    def remove(self):
        try:
            return self.qlist.pop(0)
        except:
            raise ValueError()

##    def remove(self):
##        "Removes an element from the attribute list"
##        # Check if the list is empty; if so then raise a ValueError
##        if self.qlist == []:
##            raise ValueError()
##        else:
##            # Otherwise we want to remove the first element from the list
##            # and return that to the user.
##            element = self.qlist[0]
##            self.qlist.remove(element)
##            return element
##            # Could also do this in 1 line:
##            # return self.qlist.pop(0)
            
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.qlist]) + '}'    