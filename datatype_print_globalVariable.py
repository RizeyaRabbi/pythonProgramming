# Python Getting started

# Single line comment is this line and Multiline comment is given below
"""
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# variable declarations
"""
string1 = "test"
string2 = "is"
string3 = "going"
integer = 10
floating = 7.5
sum = integer+floating
"""
# printing individual variables
"""
string1 = "test"
string2 = "is"
string3 = "going"
integer = 10
floating = 7.5
sum = integer+floating
print(string1)
print(integer)
print(floating)
print(sum)
"""
# printing same type variables with single command
# + operator to output multiple variables
# For numbers, the + character works as a mathematical operator
"""
string1 = "test"
string2 = "is"
string3 = "going"
integer = 10
floating = 7.5
sum = integer+floating
print(string1+string2+string3)
print(floating+sum)
"""
# printing different type variables with single command
# separate them with commas
# space between variables are generated automatically
"""
string1 = "test"
string2 = "is"
string3 = "going"
integer = 10
floating = 7.5
sum = integer+floating
print(string1, string2, string3, sum)
print(integer, floating, sum)
"""
# getting the type of variable
"""
string1 = "test"
string2 = "is"
string3 = "going"
integer = 10
floating = 7.5
sum = integer+floating
print(type(string1))
print(type(integer))
print(type(floating))
"""
# Assigning values of different type of variables with single command
# separated with comma
"""
a, b, c = "string", 2, 2.5
print(a)
print(b)
print(c)
"""
# Assigning same value in multiple variables
"""
a = b = c = 2
print(a)
print(b)
print(c)
"""
# Global variables
"""
a = "Started learning Python"


def func():
    print(a)


func()
"""
# Global variables can be created inside a function
# global keyword

"""
def func():
    global a
    a = "Started learning Python"


func()

print("Value of global variable is:", a)
"""
# Global and local variable can have same name with different value
"""
Variable = "GLOBAL_VARIABLE"


def func():
    Variable = "LOCAL_VARIABLE"
    print("Local", Variable)


func()
print("Global", Variable)
"""
# Global variable value can be changed using global keyword
"""
Variable = "GLOBAL_VARIABLE"
print("Printing Global: ", Variable)


def func():
    global Variable
    Variable = "LOCAL_VARIABLE"
    print("Printing locally after changing: ", Variable)


func()

print("Printing globally after changing: ", Variable)
"""
# Python Casting
# Integer casting
"""
x = int(1)
y = int(7.1)
z = int("2")
print(x, y, z)
print(type(x), type(y), type(z))
"""
# Float casting
"""
x = float(1)
y = float(2.5)
z = float("3")
z1 = float("3.5")
print(x, y, z, z1)
print(type(x), type(y), type(z),type(z1))
"""
# String casting
"""
x = str(1)
y = str(2.5)
z = str("aa")
print(x, y, z)
print(type(x), type(y), type(z))
"""
