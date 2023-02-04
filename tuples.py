# Python Tuples
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

tuple0 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple0)
print("banana" in tuple0)

# have to include a comma, even though there is only one value
tupleWithSingleValue = (1,)
print(len(tupleWithSingleValue))
print(tupleWithSingleValue[0])

# Access Tuple Items
'''
tuple0 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple0[0])
print(tuple0[-1])  # last item(negative indexing)
print(tuple0[-2])  # 2nd last item.
print(tuple0[0:3])  # Range of Indexes
print(tuple0[:2])
print(tuple0[2:])
print(tuple0[-5:-1])  # Negative range of indexes
'''
# Check if Item Exists
'''
if "apple" in tuple0:
    print("Yes")
else:
    print("No")
'''
# Tuples are unchangeable but we can convert touples into list
# make necessary changes and convert it back to touple.
'''
tuple0 = ("apple", "banana", "cherry", "apple", "cherry")
tupleToList = list(tuple0)
print(tupleToList)
tupleToList[0] = "changedAppleToAnother"
tupleToList.append("appendItem")
tupleToList.remove("banana")
toupleNew = tuple(tupleToList)
print(toupleNew)
'''
# Multiple tuples can be added using + operator
# del keyword to delete the touple
# We can also multiply tuples
'''
tuple0 = ("apple", "banana", "cherry")
tuple1 = ("apple", "cherry")
newTuple = tuple0+tuple1
print(newTuple)
print(newTuple*2)
del (newTuple)
print(newTuple)
'''
# Touple packing and unpacking
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
'''
tuple0 = ("apple", "banana", "cherry", "orange")
(f1, f2, f3, *f4) = tuple0  # added as list
print(f1)
print(f2)
print(f3)
print(f4)
'''
# The number of variables must match the number of values in the tuple
# if not, you must use an asterisk to collect the remaining values as a list.
# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.

# Loop tuples
'''
tuple0 = ("apple", "banana", "cherry", "orange")
for x in tuple0:  # Loop Through a Tuple
    print(x)
print("\n")
for i in range(len(tuple0)):  # Loop Through the Index Numbers
    print(tuple0[i])
print("\n")
j = 0
while (j < len(tuple0)):  # Loop Through a Tuple using while loop
    print(tuple0[j])
    j += 1
'''
# Tuple Methods
'''
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
        tuple.count(value)
index()	Searches the tuple for a specified value and returns the position of where it was found
        tuple.index(elmnt)
'''
