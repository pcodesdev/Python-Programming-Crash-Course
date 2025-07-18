# A string is a series of characters. Anything inside quotes is considered 
# a string in Python, and you can use single or double quotes around your 
# strings like this:
# "This is a string."
# 'This is also a string.'

# Changing Case in a String with Methods

full_name = "peter njuguna"
print(full_name.title())

# ou can change a string to all uppercase or all lowercase letters like this:
print(full_name.upper())
print(full_name.lower())

# Using Variables in Strings
first_name = "peter"
last_name = "njuguna"
# The f is for format, because Python formats the string by replacing the name of any variable in braces with its value
print(f"My name is {first_name.title()} {last_name.title()}")

# Adding Whitespace to Strings with Tabs or Newlines
# In programming, whitespace refers to any nonprinting characters, such as 
# spaces, tabs, and end-of-line symbols. You can use whitespace to organize 
# your output so it’s easier for users to read.

# To add a tab to your text, use the character combination \t:

print("\tI love programming using python")

# To add a newline in a string, use the character combination \n:
print("Examples of programming languages:\nC\nC++\nJava\nPython")

# You can also combine tabs and newlines in a single string. The string 
# "\n\t" tells Python to move to a new line, and start the next line with a tab.

print("Example of frontend frameworks includes:\n\tReact\n\tAngular\n\tBootstrap")

# Stripping Whitespace
name_one = "Peter "
name_two = "Peter"
print(name_one == name_two)

# You can also strip whitespace from the left side of a string using the lstrip() method, rstrip() mentod to the right or from both sides at once using strip():
print(name_one.rstrip())

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

# Avoiding Syntax Errors with Strings
# One kind of error that you might see with some regularity is a syntax error. 
# A syntax error occurs when Python doesn’t recognize a section of your program as valid Python code. For example, if you use an apostrophe within 
# single quotes, you’ll produce an error.

message = 'One of Python's strengths is its diverse community.'
print(message)