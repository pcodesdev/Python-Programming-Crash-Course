#Making numerical lists
# A numerical list is a list that contains numbers.
# In Python, you can create a numerical list using the range() function.
# The range() function returns a sequence of numbers, which can be converted to a list using the list() function.
# For example, you can create a list of numbers from 1 to 10 using the range() function:
for value in range(1, 6):
    print(value)

#using range() to make a list of numbers
# You can use the range() function to generate a list of numbers.       
# For example, you can generate a list of numbers from 1 to 10 using the range() function:
numbers = list(range(1, 11))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use range() to skip numbers in a range
# You can use the range() function to generate a list of numbers, and you can use the step parameter to specify how many numbers to skip.
# For example, you can generate a list of numbers from 1 to 10, skipping every other number using the range() function:
numbers = list(range(1, 11, 2))
print(numbers)  # [1, 3, 5, 7, 9]

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Simple Statistics with a List of Numbers
# You can use the min(), max(), and sum() functions to find the minimum, maximum, and sum of a list of numbers.
numbers = [1, 2, 3, 4, 5]   
print(min(numbers))  # 1
print(max(numbers))  # 5    
print(sum(numbers))  # 15

##List Comprehensions
# A list comprehension is a concise way to create a list based on an existing list. 
# It allows you to generate a new list by applying an expression to each item in the original list.
# For example, you can create a list of squares of numbers from 1 to 10using a list comprehension:
squares = [x**3 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]