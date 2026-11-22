"""
deque: a list with two open ends

A normal list is fast at the end (append, pop), but slow at the front.
A deque (say "deck") is fast at both ends. It's used for queues, like "first in, first out", 
which you'll meet in BFS and other interview patterns.

"""

from collections import deque

d = deque([1,2,34,5,67,3])
print(d)

d.append(4)
print(d)

d.appendleft(0)
print(d)

d.pop() # last item is removed
print(d)

d.popleft() # removes first item
print(d)

