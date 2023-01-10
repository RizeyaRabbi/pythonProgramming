# Python Sets

# Set items are unordered, unchangeable,
# and do not allow duplicate values.
# But can remove and add items.
# A set can contain different data types:
'''
set0 = {"one", "two", "Three", 1, 2, 3, True, False}
print(set0)
print(1 in set0)
'''
# Loop through the set
'''
for x in set0:
    print(x)
'''
# Add Set Items
'''
set0 = {"one", "two", "Three", 1, 2, 3, True, False}
set0.add("newItem")
print(set0)
'''
# Add sets
# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
'''
set0 = {1, 2, 3, "one"}
set1 = [2, 5, 6]
set0.update(set1)
print(set0)
'''
# Remove and delete items
# Items can also be removed by using pop.
# But being unordered random values are deleted.Not useful.
'''
set0 = {1, 2, 3, "one"}
set0.remove(1)  # item  does not exist, remove() will raise an error.
print(set0)
set0.discard(3)  # item  does not exist, will not raise an error.
print(set0)
set0.clear()  # empties the set
print(set0)
del set0
print(set0)
'''
# Join Sets
'''
set0 = {1, 2, 3}
set1 = {"ONE", "TWO", "THREE"}
set3 = set1.union(set1)
print(set3)
set1.update(set0)  # type:ignore
print(set1)
'''
# intersection and  update
'''
set0 = {1, 2, 3, 4, 5}
set1 = {3, 4, 7}
set0.intersection_update(set1)
print(set0)
set3 = set0.intersection(set1)
print(set3)
'''
'''
set0 = {1, 2, 3, 4, 5}
set1 = {3, 4, 7}
set0.symmetric_difference_update(set1)
print(set0)
set3 = set0.symmetric_difference(set1)
print(set3)
'''
# Set Methods
'''
Method	                                   Description
add()	                              Adds an element to the set
clear()	                              Removes all the elements from the set
copy()	                              Returns a copy of the set
difference()	                      Returns a set containing the difference between two or more sets
difference_update()	                  Removes the items in this set that are also included in another, specified set
discard()	                          Remove the specified item
intersection()	                      Returns a set, that is the intersection of two other sets
intersection_update()	              Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                      Returns whether two sets have a intersection or not
issubset()	                          Returns whether another set contains this set or not
issuperset()	                      Returns whether this set contains another set or not
pop()	                              Removes an element from the set
remove()	                          Removes the specified element
symmetric_difference()	              Returns a set with the symmetric differences of two sets
symmetric_difference_update()	      inserts the symmetric differences from this set and another
union()	                              Return a set containing the union of sets
update()	                          Update the set with the union of this set and others
'''
