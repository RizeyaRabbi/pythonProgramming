# Multiline String
# New lines and spaces are gnerated automatically according to the code.
# Double quotes or single quotes
"""
a = '''Learning Python
is very
easy.'''
print(a)
"""
# Slicing Strings
# start index and the end index separated by a colon, to return a part of the string.
# Prints position n to n-1
"""
a = "arduinoframeworkisveryeasy"
print(a[1:5])  # prints from 1 to 4
print(a[12:20])  # prints from 12 to 19
"""
# Slicing from start to desired position
"""
a = "arduinoframeworkisveryeasy"
print(a[:5])
"""
# Slicing to the end from desired position
"""
a = "arduinoframeworkisveryeasy"
print(a[0:])
"""
# Negative Indexing
# Negative indexes to start the slice from the end of the string
"""
a = "arduinoframeworkisveryeasy"
print(a[-10:-2])
"""
# Modify Strings
"""
a = "ArduinoFrameworkIsVeryEasy"
print(a.upper())
print(a.lower())
"""
# White space removing
"""
a = "  ArduinoFrameworkIsVeryEasy  "
print(a.strip())
"""
# Replace String
"""
a = "ArduinoFrameworkIsVeryEasy"
print(a.replace("a", "1"))
"""
# Split String
# splits the string into substrings if it finds instances of the separato
"""
a = "ArduinoFramework.,IsVeryEasy"
print(a.split(","))
print(a.split("."))
"""
# String Concatenation
# + operator to combine
# to add space need to add " "
"""
a = "Arduino framework"
b = "is very easy"
print(a+b)
print(a+" "+b)
"""
# Format - Strings
# index numbers can be used to be sure the arguments are placed in the correct placeholders
"""
increment = 4
salary = 1
statement = "My salary is {0} and increment is {1}"
print(statement.format(salary, increment))
"""
# Escape Characters
# Carriage return \r windows=line ending, linux = new line, osx=carriage return only
# Carriage return replaces the amount of characters from start after /r
"""
print("\"ArduinoFramework\"IsVeryEasy")  # "ArduinoFramework"
print("\'ArduinoFramework\'IsVeryEasy")  # 'ArduinoFramework'
print("\\ArduinoFramework\\IsVeryEasy")  # \ArduinoFramework\
print("ArduinoFrameworkIsVeryEasy\r123")  # Wroking on command line.
print("ArduinoFramework\tIsVeryEasy")    # Tab
print("ArduinoFramework\bisveryeasy")  # backspace
# A backslash followed by three integers will result in a octal value
print("\110\145\154\154\157")
# A backslash followed by an 'x' and a hex number represents a hex value
print("\x48\x65\x6c\x6c\x6f")
"""
"""
Method	           Description
capitalize()	   Converts the first character to upper case
casefold()	       Converts string into lower case
center()	       Returns a centered string
count()	           Returns the number of times a specified value occurs in a string
encode()	       Returns an encoded version of the string
endswith()	       Returns true if the string ends with the specified value
expandtabs()	   Sets the tab size of the string
find()	           Searches the string for a specified value and returns the position of where it was found
format()	       Formats specified values in a string
format_map()	   Formats specified values in a string
index()	           Searches the string for a specified value and returns the position of where it was found
isalnum()	       Returns True if all characters in the string are alphanumeric
isalpha()	       Returns True if all characters in the string are in the alphabet
isdecimal()	       Returns True if all characters in the string are decimals
isdigit()	       Returns True if all characters in the string are digits
isidentifier()	   Returns True if the string is an identifier
islower()	       Returns True if all characters in the string are lower case
isnumeric()	       Returns True if all characters in the string are numeric
isprintable()	   Returns True if all characters in the string are printable
isspace()	       Returns True if all characters in the string are whitespaces
istitle()	       Returns True if the string follows the rules of a title
isupper()	       Returns True if all characters in the string are upper case
join()	           Joins the elements of an iterable to the end of the string
ljust()	           Returns a left justified version of the string
lower()	           Converts a string into lower case
lstrip()	       Returns a left trim version of the string
maketrans()	       Returns a translation table to be used in translations
partition()    	   Returns a tuple where the string is parted into three parts
replace()	       Returns a string where a specified value is replaced with a specified value
rfind()	           Searches the string for a specified value and returns the last position of where it was found
rindex()	       Searches the string for a specified value and returns the last position of where it was found
rjust()	           Returns a right justified version of the string
rpartition()	   Returns a tuple where the string is parted into three parts
rsplit()	       Splits the string at the specified separator, and returns a list
rstrip()	       Returns a right trim version of the string
split()	           Splits the string at the specified separator, and returns a list
splitlines()	   Splits the string at line breaks and returns a list
startswith()	   Returns true if the string starts with the specified value
strip()	           Returns a trimmed version of the string
swapcase()	       Swaps cases, lower case becomes upper case and vice versa
title()	           Converts the first character of each word to upper case
translate()	       Returns a translated string
upper()	           Converts a string into upper case
zfill()	           Fills the string with a specified number of 0 values at the beginning
"""
