list1 = [1,2,3,4,5,6]

# add 7 at the end of the list
list1.append(7)

# removes all items in a list
list1.clear()

# adds the given list to the end of the other list
list1.extend([1,2,3,4,5,6,7,8,9,10])

# inserting an element at a specific index
list1.insert(2,10)

# removes the first occurance of 5
list1.remove(5)

# removes element at a specific index
list1.pop(3)

# finds the index of the first occurance of 5

list1.index(1)

# counts the occurances of a specific value
list1.count(2)

# copying the list

elisti_enyia = list1.copy

print (elisti_enyia)

# retyurning the length of the list - len

size = len(list1)

# minimum value
min_value = min(list1)

# maximum value
max_value = max(list1)

# sum of all the values in the list

values_sum = sum(list1)

# accessing specific section za the list

sliced_list = list1[1:5]

# concatenating a list

combined_list = list1 + [1,2,3,4,5,6]

# checking whether an element is in a list

names = ['caleb', 'mayaka', 'ombogo']

name_status = 'caleb' in names

print(name_status)













# deleting the whole list
del list1