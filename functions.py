# Python functions

'''
def func():
    print("This is a function")


func()
'''
# Functions with parameter

'''
def func(name): # one parameter
    print(name)


func("Argument passed")
'''
# if the number of argument is unknown * is used before parameter name
# Function receives a tuple

'''
def func(*param):
    print(param)


func("a", "b", "c")
'''
# Keyword Arguments
# if the number of keyword argument is unknown ** is used before parameter name
'''
def func(param1, param3, param2):
    print(param1)
    print(param2)
    print(param3)


func(param1="abc", param2="def", param3="ghi")
'''

'''
def func(**name):
    print(name["fname"]+name["lname"])


func(fname="aaa", lname="bbb")
'''
# defualt parameter value
# If nothing passed default value will be used

'''
def func(name="aaa"):
    print(name)


func("bcd")
func()
func("efg")
'''
# any datatype can be send as argument

'''
def func(dt):
    print(dt)
    print(type(dt))


lst = ["a", "b", "c"]
tpl = ("a", "b", "c")
st = {"a", "b", "c"}
dct = {"1": "a", "2": "b", "3": "c"}
func(lst)
func(tpl)
func(st)
func(dct)
'''
# return value

'''
def func(num1, num2):
    return num1*num2


x = func(4, 5)
print(x)
'''
# pass keyword
# to make function empty pass is used

'''
def func():
    pass
'''

# Recusrsion

'''
def recf(num):
    if num > 0:
        result = num+recf(num-1)
        print(result)
    else:
        result = 0
    return result


recf(4)
'''
