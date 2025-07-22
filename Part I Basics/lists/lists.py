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

# Modifying, Adding, and Removing Elements
# Modifying Elements in a List
# The syntax for modifying an element is similar to the syntax for accessing 
# an element in a list. To change an element, use the name of the list followed 
# by the index of the element you want to change, and then provide the new 
# value you want that item to have.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[1] = 'kuga'

print(motorcycles)

# Adding Elements to a List
# ppending Elements to the End of a List
# The simplest way to add a new element to a list is to append the item to the 
# list. When you append an item to a list, the new element is added to the end 
# of the list. Using the same list we had in the previous example, we’ll add the 
# new element 'ducati' to the end of the list:

motorcycles.append("bmw")
print(motorcycles)

# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert()
# method. You do this by specifying the index of the new element and the 
# value of the new item:
motorcycles.insert(0, 'kingbird')
print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can 
# use the del statement:
del motorcycles[4]
print(motorcycles)

# Removing an Item Using the pop() Method
# The pop() method removes the last item in a list, but it lets you work 
# with that item after removing it. The term pop comes from thinking of a 
# list as a stack of items and popping one item off the top of the stack. In this 
# analogy, the top of a stack corresponds to the end of a list.

removed_motorcycle = motorcycles.pop()
print(motorcycles)
print(removed_motorcycle)
print(f"The last motorcycle that I bought was a {removed_motorcycle} from Japan.")

# Popping Items from Any Position in a List
# You can use pop() to remove an item from any position in a list by including 
# the index of the item you want to remove in parentheses:



first_motorcycle = motorcycles.pop(0)

print(f"The first motorcycle that I owned was a {first_motorcycle.title()} from China.")

# when you want to delete an item from a list 
# and not use that item in any way, use the del statement; if you want to use an 
# item as you remove it, use the pop() method.
# Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove 
# from a list. If you only know the value of the item you want to remove, you 
# can use the remove() method.
expensive_motorcycle = 'kuga'
motorcycles.remove(expensive_motorcycle)
print(motorcycles)
print(f"{expensive_motorcycle.title()} is a very expensive motorcycle with limited spareparts availability in the market.")

# Organizing a List
# Sorting a List Permanently with the sort() Method
# Python’s sort() method makes it relatively easy to sort a list. Imagine we 
# have a list of cars and want to change the order of the list to store them 
# alphabetically. 
cars = ['bmw', 'toyota', 'honda', 'mazda']
cars.sort()
print(cars)

# The sort() method is permanent
# You can also sort this list in reverse-alphabetical order by passing the 
# argument reverse=True to the sort() method

cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
print(sorted(cars))
print(cars)

# Printing a List in Reverse Order
# To reverse the original order of a list, you can use the reverse() method.

cars.reverse()
print(cars)

# The reverse() method changes the order of a list permanently, but you 
# can revert to the original order anytime by applying reverse() to the same 
# list a second time.

# Finding the Length of a List
# You can quickly find the length of a list by using the len() function. The list 
# in this example has four items, so its length is 4:

print(len(cars))

# Avoiding Index Errors When Working with Lists
print(cars[3])

# An index error means Python can’t find an item at the index you 
# requested.
# Keep in mind that whenever you want to access the last item in a list, 
# you should use the index -1
print(cars[-1])