# Python dictionaries:

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*(As of Python version 3.7),
# changeable and do not allow duplicates.
'''
dic0 = {"name": "Aaaa",
        "year": "2022",
        "price": "200$"}
print(dic0)
print(dic0["price"])
dict1 = dict(name="Bbbb", year=2022, price=300, active=False)
print(dict1)
'''
# Accessing Items
'''
dict0 = dict(name="Bbbb", year=2022, price=300, active=False)
print(dict0.keys())
x = dict0["name"]
print(x)

y = dict0.get("name")
print(y)

dict0["color"] = "black"
print(dict0.keys())
print(dict0.values())
print(dict0.items())
'''
# Change Values
'''
dic0 = {"name": "Aaaa",
        "year": "2022",
        "price": "200$"}
dic0["name"] = "newName"
print(dic0["name"])

dic0.update({"year": "2023"})
print(dic0["year"])
'''
# Adding Items
'''
dic0 = {"name": "Aaaa",
        "year": "2022",
        "price": "200$"}
dic0["color"] = "red"
print(dic0)
dic0.update({"color": "green"})
print(dic0)
dic0.update({"active": "positive"})
print(dic0)
'''
# Remove Dictionary Items
'''
dic0 = {"name": "Aaaa",
        "year": "2022",
        "model": "new",
        "price": "200$",
        "color": "green"}
dic0.pop("model")
print(dic0)
dic0.popitem()  # removes the last inserted item(python 3.7 and up)
print(dic0)
del dic0["year"]
print(dic0)
dic0.clear()
print(dic0)
del dic0
print(dic0)
'''
# Loop Dictionaries
'''
dic0 = {"name": "Aaaa",
        "year": "2022",
        "model": "new",
        "price": "200$",
        "color": "green"}
for x in dic0:  # Looping the keys
    print(x)
for x in dic0:   # Looping the values
    print(dic0[x])
for x in dic0.values():
    print(x)
for x in dic0.keys():
    print(x)
for x, y in dic0.items():
    print(x, y)
'''

# Copy Dictionaries
'''
dic0 = {"name": "Aaaa",
        "year": "2022",
        "model": "new",
        "price": "200$",
        "color": "green"}
dic1 = dic0.copy()
print(dic1)
dic2 = dict(dic0)
print(dic2)
'''
# Nested Dictionaries
'''
device = {
    "pc": {"brand": "asus",
           "Price": 2000,
           "Year": 2022
           },

    "Phone": {"brand": "samsung",
              "Price": 1000,
              "Year": 2020
              },
    "Tab": {"brand": "apple",
            "Price": 1500,
            "Year": 2023
            }
}
newPC = device["Tab"]
print(newPC["brand"])
newPC["brand"] = "MSI"
print(newPC["brand"])
print(newPC)
'''
# Dictionary Methods
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''
