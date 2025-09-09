alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# A dictionary in Python is a collection of key-value pairs. Each key is connected to  a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. In Python, a dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces, as shown in the earlier example: alien_0 = {'color': 'green', 'points': 5}

# Adding New Key-Value Pairs
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying Values in a Dictionary
alien_0['color'] = 'green'
print(alien_0)
alien_0['speed'] = 'medium'
print(alien_0)
if alien_0['speed'] == 'slow':
    x_increment = 1
else:
    x_increment = 2
    
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
# When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair. All del needs is the name of the dictionary and the key that you want to remove.

del alien_0['points']
# Be aware that the deleted key-value pair is removed permanently.
print(alien_0)

# Using get() to Access Values
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping Through a Dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping Through All the Keys in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# Looping Through a Dictionary’s Keys in a Particular Order
# Looping through a dictionary returns the items in the same order they 
# were inserted. Sometimes, though, you’ll want to loop through a dictionary in a different order

# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for value in set(favorite_languages.values()):
    print(value.title())
    
# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. When you see braces but no key-value pairs, you’re probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific order.