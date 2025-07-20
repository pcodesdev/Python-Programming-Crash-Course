# A list is a collection of items in a particular order
# In Python, square brackets ([]) indicate a list, and individual elements 
# in the list are separated by commas. Here’s a simple example of a list that 
# contains a few kinds of bicycles:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# list items are accessed through index
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
# Python considers the first item in a list to be at position 0, not position 1. 
# This is true of most programming languages, and the reason has to do with 
# Introducing Lists   35
# how the list operations are implemented at a lower level

print(bicycles[3])

# Python has a special syntax for accessing the last element in a list. If you ask for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1])

# Using Individual Values from a List
print(f"My first bicycle was {bicycles[0].title()}.")