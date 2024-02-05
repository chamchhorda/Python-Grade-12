my_str = "Hello, World!"

my_multiline_str = '''
this is my new line 
this is another new line 
this is also another new line 
'''

print(my_str[0])

# this is a for loop this will
# loop through each character in a string 
# printing it out
for i in my_str: 
    print(i)

my_longer_str = '''
this is my multiline string 
i want to show how the len() function work for the long string one
'''

# the len function will show the number of character in a string
print(len(my_longer_str))

# checking if the word "or" is inside the phrase "Hello, World"

print("or" in my_str)

print(my_str.upper())
print(my_str.lower())

my_str = " Hello, World "
print(my_str)
# remove the spaces in our string
print(my_str.strip())
# replace old word with new word
print(my_str.replace('hello','bye bye'))
# split function will split your string 
print(my_str.split(" "))

# concatenation is adding two string together 
str_one = "Hello"
str_two = "World"

print(str_one + " " + str_two)
print("Bye Bye," + str_two)

# format string
print(f"Hello, {str_two}")

print("Hello, " + str_two + "add more string here")
print(f"{str_two} {str_two}")

# my name is name I'm here 
# escape character
print('my name is name I\'m here')
