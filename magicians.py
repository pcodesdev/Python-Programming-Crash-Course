#Looping allows you to take a single code block and run it over and over again.
# for loop in Python is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# It allows you to execute a block of code multiple times, once for each item in the sequence.
# The syntax is:
# for variable in sequence:
#     # code block to execute for each item in the sequence 
# The variable is assigned the value of each item in the sequence in turn, and the code block is executed for each item.
# The for loop continues until all items in the sequence have been processed.
# The for loop is a powerful tool for iterating over sequences and performing operations on each item.
# It is commonly used in Python for tasks such as iterating over lists, tuples, and dictionaries, as well as for looping over a range of numbers.
# The for loop is a fundamental part of Python programming and is widely used in many applications.
# 
# # Looping through a list
# Looping through a list allows you to perform an action for each item in the list.
# This is useful when you want to process each item in the list individually.
# For example, you can print each item in the list, or perform some operation on each item.
# The for loop is a powerful tool for iterating over lists and performing operations on each item.
# It is commonly used in Python for tasks such as iterating over lists, tuples, and dictionaries, as well as for looping over a range of numbers.
# The for loop is a fundamental part of Python programming and is widely used in many applications.
magicians = ['alice', 'david', 'carolina']
# Looping through a list of magicians
# This code iterates through each magician in the list and prints a message for each one.
# The title() method is used to capitalize the first letter of each magician's name.
# The output will be a personalized message for each magician.
for magician in magicians:
    # Print a message for each magician
    print(magician.title()  + ", that was a great trick!")  
    print(f"I can't wait to see your next trick, {magician.title()} \n")
    
print("Thank you, everyone. That was a great magic show!")

#
#Avoiding Indentation Errors
# Indentation is crucial in Python, as it defines the blocks of code.
# If you forget to indent a line of code, or if you indent it incorrectly, you will get an IndentationError.    
# For example, the following code will raise an IndentationError:
# for magician in magicians:
# print(magician.title() + ", that was a great trick!")  
# IndentationError: expected an indented block

#
#logical error
# A logical error is a mistake in the code that does not produce an error message, but produces incorrect results.
# For example, if you forget to capitalize the first letter of each magician's name, you will get a logical error:# for magician in magicians:  
#     print(magician + ", that was a great trick!")
# This will print the names of the magicians without capitalizing the first letter, which is not the intended behavior.
# To fix this, you can use the title() method to capitalize the first letter of each magician's name:
# for magician in magicians:  
#     print(magician.title() + ", that was a great trick!") 

#
# Indemting Unnecessary Lines
# Indenting an unnecessary line of code will raise an IndentationError.
# For example, the following code will raise an IndentationError:   
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")  
#     print(f"I can't wait to see your next trick, {magician.title()} \n")  
#     print("Thank you, everyone. That was a great magic show!")
# IndentationError: unexpected indent
# To fix this, you can remove the unnecessary indentation:  

# message = "Hello, world!"
# print(message)  # Hello, world!

#
#Forgetting the Colon
# Forgetting the colon at the end of the for loop will raise a SyntaxError.
# For example, the following code will raise a SyntaxError:# 
for magician in magicians:
     print(magician.title() + ", that was a great trick!")  
