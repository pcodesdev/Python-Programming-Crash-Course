# Using Variables in Strings
first_name = "John"
last_name = "Doe"
# Using f-strings to format strings
# F-strings are a way to embed expressions inside string literals, using curly braces `{}`.
full_name = f"{first_name} {last_name}"
print(full_name)  # John Doe

# Adding Whitespace to Strings with Tabs or Newlines
print("\tPython")  # Adds a tab space before Python 
print("Languages:\nPython\nC\nJavaScript")  # Adds a new line before each string
print("Languages:\n\tPython\n\tC\n\tJavaScript")  # Adds a new line and tab space before each string

# syntax error is when you write code that Python cannot understand.
# For example, if you forget to close a string with a quote, Python will raise a syntax error.
# Example of a syntax error:# print("Hello World!   # This line is missing a closing quote
# print("Hello World!")  # This line is correct 