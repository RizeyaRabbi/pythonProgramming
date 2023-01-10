# Python loops

# for loop
# for loop with range() function
'''
for x in range(2, 5):
    print("*")

for x in range(5):
    print("*")

for x in range(1, 10, 2):
    print(x)
'''
# for loop is used for iterating over a sequence
'''
a = ["a", "b", "c", "d"]
b = "abcdefgh"
for x in (a):
    print(x)
for x in b:
    print(x)
'''
# break statement to exit the loop
# continue statement to stop the current iteration and go to nex iteration
a = ["a", "b", "c", "d"]
b = "abcdefgh"
'''
for x in a:
    if x == "c":
        continue
    print(x)
'''
'''
for x in a:
    if x == "c":
        break
    print(x)
'''
# else with for loop
# else executes after looping is finished
'''
for x in a:
    print(x)
else:
    print("Finished")
'''
# else will not be executed if loop is stopped by break
'''
for x in a:
    print(x)
    if x == "c":
        break
else:
    print("Finished")
'''
# Nested loops
'''
for x in range(5):
    for y in range(x+1):
        print("*", end="")
    print("\r")
'''
# loops cant be empty. Need to use pass statement if nothing in loop
'''
for x in a:
    pass
'''

### While loop ###
# same as for loop, only syntex is changed.
'''
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        continue
       # break
    print(i)
else:
    print("i is greater than 5")
'''
