# Python if else

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
a = 60
b = 60
c = 50
'''
if a < b:
    print("a is less than b")
elif a == b:  # if the previous conditions were not true, then try this condition
    print("a is equal b")
else:
    print("a is greater than b")
'''
# Short Hand If
'''
if a < b:
    print("a is less than b")
'''
'''
# Short Hand If ... Else
# This technique is known as Ternary Operators, or Conditional Expressions.
print("a is greater than b") if a > b else print("a is less than b")
print("A") if a > b else print("==") if a == b else print("b")
'''
# And Or keyword
'''
if a == b and b > c:
    print("a==b and b is greater than c")
if a == b or b < c:
    print("at least one condition is true")
'''
# Nested if
'''
if a == b:
    print("==")
    if b > c:
        print(">>")
'''
# pass statement
# if statement can not be empty. For no statement just need to use pass
'''
if a == b:
    pass
'''
