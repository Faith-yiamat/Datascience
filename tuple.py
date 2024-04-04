# accessing items in a tuple 
my_tuple = (1,2,3,4,5)
print(my_tuple[0])   # output 1
print(my_tuple[3]) # output 4

# adding items to a tuple
new_tuple = my_tuple + (6,)
print(new_tuple)      # output (1,2,3,4,5,6)

# removing items from a tuple
index_to_remove = 1
remove_item = my_tuple[:index_to_remove] + my_tuple[index_to_remove + 1:]
print(remove_item)  # output (1,3,4,5)