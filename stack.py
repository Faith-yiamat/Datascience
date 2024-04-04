# creating a stack
stack = []
stack.append("Faith")
stack.append("Yiamat")
stack.append("Ynonne")
stack.append("Martin")
print(stack)

# accessing the top item without removing it (peeking)
top_item = stack[-1]
print(top_item)

# accessing the top item and removing it
removing = stack.pop()
print(removing)

# removing the element in stack
remove_elem = stack.remove([2])
print(remove_elem)
print(stack)
for le in stack:print(stack.remove(2))

# adding the elements to stack
add = stack.append("Oloserian")
print(add)
print(stack)