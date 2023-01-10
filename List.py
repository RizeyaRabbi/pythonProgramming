# Lists
# List is a collection which is ordered and changeable.
# Allows duplicate members.
# Lists are used to store multiple items in a single variable.
liststring = ["One", "two", "Three", "four", "Five"]
listint = [1, 2, 3, 4, 5]
listbool = [True, False, True, False, True]
listUsinglistConstructor = list((1, 2, 3, 4, 5))
'''
print(liststring)
print(listint)
print(listbool)
print(listUsinglistConstructor)
'''
'''
print(len(liststring))
print(len(listint))
print(len(listbool))
print(len(listUsinglistConstructor))
'''
# Access List Items(Starts from the beginning)
'''
print(liststring[0]) # First item
print(listUsinglistConstructor[2])
'''
# Access List Items(Starts from the end)
'''
print(listint[-1])  # last item in the list
print(listbool[-3])  # 3rd item from the last
'''
# Range of Indexes
'''
print(liststring[2:4])  # from 2nd to 3rd position(n to n-1)
print(liststring[:4])  # from 0 to 3rd position(0 to n-1)
print(liststring[3:])  # from 3rd position to the end
print(liststring[-4:-1]) 
'''
# Check if Item Exists
'''
if 2 in listint:
    print("Yes")
else:
    print("No")
'''
# Change item value
'''
print(listint)
listint[0] = 0
print(listint)
listint[0:2] = [0, 0, 0]
print(listint)
'''
# Insert Item
'''
# inserts an item in a desired position
listint.insert(1, "New item")
print(listint)
'''
'''
# Insert item at the end of the list
listint.append("inserted item")
print(listint)
'''
# Extend item
# adds any iterable object (tuples, sets, dictionaries etc.).
'''
listint.extend(liststring)
print(listint)
'''
# Remove item
'''
print(listint)
listint.remove(1)
print(listint)
'''
# Remove Specified Index
'''
print(listint)
listint.pop(0)  # removes the passed index
print(listint)
listint.pop()  # if no index is given it removes the last index
print(listint)
'''
'''
print(listint)
del listint[0]  # removes the passed index
print(listint)
del listint  # deletes the list completely
print(listint)
'''
'''
print(listint)
listint.clear() # clears the list
print(listint)
'''
# loop through a list
'''
for x in listint:
    print(x)
'''
'''
i = 0
while i < len(listint):
    print(listint[i])
    i = i+1
'''
'''
for i in range(len(listint)):
    print(listint[i])
'''
# List Comprehension
'''
newlist = [x for x in listint]
print(newlist)
newlist = [x for x in listint if x != 1]
print(newlist)
newlist = [x for x in listint if x > 2]
print(newlist)
newlist = [0 for x in listint]  # Changes all the values to 0
print(newlist)
'''
# sort() method  sort the list alphanumerically, ascending, by default
# case sensitive
'''
list = [21, 44, 1, 65, 86, 74, 12, 3, 2, 10]
list.sort()
print(list)
list.sort(reverse=True)  # descending order
print(list)
liststring.sort()  # case sensitive
print(liststring)
liststring.sort(key=str.lower)  # case insensitive
print(liststring)
liststring.reverse()  # reverse order
print(liststring)
'''
# Copy list
'''
newintlist = listint.copy()
print(newintlist)
newstringlist = list(liststring)
print(newstringlist)
'''
# join list
'''
print(listint)
print(liststring)
'''
'''
newlist = listint + liststring  # using the + operator.
print(newlist)
'''
'''
for x in liststring:
    listint.append(x)    # using append function
print(listint)
'''
'''
liststring.extend(listint)
print(liststring)
'''
# list methods
'''
Method	     Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()  	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''
