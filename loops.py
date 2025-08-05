# Looping allows you to take the same action, or set 
# of actions, with every item in a list.

# When you want to do the same action with every item in a list, you 
# can use Python’s for loop.

magicians = ['alice', 'david', 'carolina']
# This line tells Python to pull a name from the list magicians, 
# and associate it with the variable magician.
for magician in magicians:
# It might help to read this code as 
# “For every magician in the list of magicians, print the magician’s name.” 
    # print(magician)
    
# keep in mind when writing your own for loops that you can choose 
# any name you want for the temporary variable that will be associated with 
# each value in the list.
    print(f"{magician.title()}, that was a great trick!")
    # Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.
    print(f"I can't wait to see your next trick, {magician.title()}.\n") 
    
# Doing Something After a for Loop
# What happens once a for loop has finished executing? Usually, you’ll want 
# to summarize a block of output or move on to other work that your program must accomplish.   
print("Thank you, everyone. That was a great magic show!")

# Making Numerical Lists
# Using the range() Function
# Python’s range() function makes it easy to generate a series of number
for value in range(1, 10):
    print(value)
    
# You can also pass range() only one argument, and it will start the 
# sequence of numbers at 0.
for value in range(6):
    print(value)
# Using range() to Make a List of Numbers
# If you want to make a list of numbers, you can convert the results of range()
# directly into a list using the list() function. When you wrap list() around a 
# call to the range() function, the output will be a list of numbers.
numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a 
# given range. If you pass a third argument to range(), Python uses that value 
# as a step size when generating numbers.
# For example, here’s how to list the even numbers between 1 and 10:
even_numbers = list(range(0, 21, 2))
print(even_numbers)

squares = []

for value in range(1, 11):
    squared = value ** 2
    squares.append(squared)
    
print(squares)

# Simple Statistics with a List of Numbers
print(min(squares))
print(max(squares))
print(sum(squares))

# List Comprehensions
# A list comprehension allows you to generate this same list in just one line of code. 

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Slicing a List
# You can access any set of items in a list by using a slice.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
# Copying a List
# To copy a list, you can make a slice that includes the
# entire original list by omitting the first index and the second
# index ([:]). This tells Python to make a slice that starts at
# the first item and ends with the last item, producing a copy
# of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
freind_foods = my_foods[:]
my_foods.append("ice cream")
freind_foods.append("sunflower")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(freind_foods)
