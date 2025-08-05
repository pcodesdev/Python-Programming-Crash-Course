pizzas = ['mkate', 'mayai', 'sousage']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("\nI love Mayai pizza.\nI really love pizza.")

cattle = ['sheep', 'goat', 'cow']
for animal in cattle:
    print(f"{animal.title()} would be a great farm animal.")
    
print("\nAny of this animal is good for meat and milk production.")

for number in range(1, 21):
    print(number)
    
one_million_numbers = []

for number in range(1, 10000001):
    one_million_numbers.append(number)
    
# print(one_million_numbers)

print(min(one_million_numbers))
print(max(one_million_numbers))
print(sum(one_million_numbers))

odd_numbers = []
for number in range(1, 20, 2):
    odd_numbers.append(number)
    
print(odd_numbers)

three_multiples = []
for number in range(3, 30, 3):
    three_multiples.append(number)
print(three_multiples)

cubes = []
for cube in range(1, 10):
    cubes.append(cube **3)
    
print(cubes)

# list comprehension
cubes = [cube ** 3 for cube in range(1, 10)]
print(cubes)

motorcycles = ['honda', 'suzuki', 'yamaha', 'bmw', 'ducati', 'roice roys']
print("The first three items are:")
for motorcycle in motorcycles[:3]:
    print(motorcycle.title())
    
print("Three items from the middle of the list are:")
for middle_motorcycles in motorcycles[1:4]:
    print(middle_motorcycles.title())
    
print("The last three items in the list are:")
for last_motorcycles in motorcycles[3:]:
    print(last_motorcycles.title())
    
my_pizzas = ['Neapolitan', 'Chicago Deep-Dish', 'New York-Style', 'Sicilian', 'Detroit-Style']

friend_pizzas = my_pizzas[:]
my_pizzas.append('Beef-Stake Pizza')
friend_pizzas.append('Pizza Fry')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)