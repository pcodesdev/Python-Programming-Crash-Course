#Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Modifying an element
motorcycles[1] = 'bmw'
print(motorcycles)  # ['honda', 'bmw', 'suzuki']
#Adding elements to a list
motorcycles.append('ducati')
print(motorcycles)  # ['honda', 'bmw', 'suzuki', 'ducati']
#Appending elements to a list using the append() method
#The append() method adds an item to the end of a list.
#You can append multiple items to a list using a loop.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')    
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
#Inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'evakuga')
print(motorcycles)  # ['evakuga', 'honda', 'yamaha', 'suzuki']

#Removing elements from a list
#Removing an item using the del statement
#The del statement removes an item from a list by its position in the list using its index.
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # ['yamaha', 'suzuki']

#Removing an item using the pop() method
#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
removed_motorcycle = motorcycles.pop()
print(motorcycles)  # ['honda', 'yamaha']
print(removed_motorcycle)  # suzuki
print(f"The last motocycle that I owned was a, {removed_motorcycle.title()}.")  # The last motocycle that I owned was a Suzuki.
#You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.
first_motorcycle = motorcycles.pop(0)
print(f"The first motorcycle that I owned was a {first_motorcycle.title()}.")  # The first motorcycle that I owned was a Honda.

#Removing an item by value using the remove() method
#The remove() method removes the first occurrence of a value in a list.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
removed_motorcycle = 'ducati'
motorcycles.remove(removed_motorcycle)
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
print(f"I removed {removed_motorcycle.title()} from my list of motorcycles because it's too expensive to maintain.")  # I removed Ducati from my list of motorcycles.