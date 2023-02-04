from array import *
# Python Array

# from array import *
# arrayName = array(typecode, [Initializers])
# https://docs.python.org/3/library/array.html


# Array initialization
'''
array1 = array('i', [10, 20, 30, 40, 50])
for x in array1:
    print(x)
'''

# Accessing Array elements
'''
array1 = array('i', [10, 20, 30, 40, 50])
print(array1[0])
print(array1[-1])
'''
# Inserting elements on an Array
'''
array1 = array('i', [10, 20, 30, 40, 50])
array1.insert(0, 0)
array1.insert(6, 60)
for x in array1:
    print(x)
'''
# Deleting elements on an Array
'''
array1 = array('i', [10, 20, 30, 40, 50])
array1.remove(30)
for x in array1:
    print(x)
'''
# Searching elements
# Can be searched by value and it will return the index
'''
array1 = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(array1.index(70))
'''
# update operation
'''
array1 = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
array1[0] = 0
for x in array1:
    print(x)
'''
