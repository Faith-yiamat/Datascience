# implementation using list
queue = []
# we use append method to add elements 
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)

# removing the last element

print(queue.pop(0))
print(queue)


# impelementation using collections.deque
from collections import deque
q = deque()
q.append("Yiamat")
q.append("Faith")
q.append("Oloserian")
print(q)
print(type(q))
# remove the last element in a deque
print(q.popleft())
print(q)

print(type(q))