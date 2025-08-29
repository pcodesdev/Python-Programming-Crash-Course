motorcycle = 'suzuki'
print("motorcycle == 'suzuki'? I predict True.")
print(motorcycle == 'suzuki')

print("motorcycle == 'bmw'? I predict False.")
print(motorcycle == 'bmw')

car_name = 'nissan'
print(car_name == 'nissan')
print(car_name == 'Nissan')

age_0 = 20
age_1 = 19
if age_0>=18 and age_1 >= 18:
    print("Adult")
    
if age_0>=20 or age_1 >= 20:
    print("Adult")
    
fruits = ['apple', 'mango', 'pineapple']
fruit = 'watermelon'
if fruit in fruits:
    print(f"{fruit.title()}")
else:
    print("fruit does not exist!")
    
if fruit not in fruits:
    print(f"{fruit.title()} does not exist!")
else:
    print("fruit does exist!")
    
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points")
if alien_color == 'red':
    print("You just earned 5 points")
    
alien_color = 'green'

if alien_color == 'green':
    print("player just earned 5 points for shooting the alien.")
else:
    print("player just earned 10 points.")
    
if alien_color == 'green':
    print("player just earned 5 points for shooting the alien.")
if alien_color != 'green':
    print("player just earned 10 points.")
    
    
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points")
elif alien_color == 'red':
    print("The player earned 15 points")
    
    
# Stage of life
age = 10
if age < 2:
    print("The person is a baby")
elif  age < 4:
    print("The person is a toddler")
elif age < 13:
    print("The person is a kid")
elif age < 20:
    print("The person is a teenager")
elif age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")
    
favorite_fruits = ['mangos', 'bananas', 'apples']
if 'mangos' in favorite_fruits:
    print("Mangos added to the toppings")
if 'oranges' in favorite_fruits:
    print("Oranges added to the toppings")
if 'apples' in favorite_fruits:
    print("Apples added to the toppings")
    
print("\n")
    
print("n\ere is your fruits salad!")

usernames = ['tech', 'admin', 'custsupport', 'uhuru', 'pesh']
current_users = ['pesh', 'emmah', 'mumbus', 'mwaosh', 'goat']
# if usernames:
    
#     for username in usernames:
#         if username == "admin":
#             print(f"Hello {username}, would you like to see a status report?")
#         else:
            
#             print(f"Hello, {username} welcome to pematech website.")
    
# else:
#      print("We need to find some users!") 

for username in usernames:
    if username in current_users:
        print(f"That {username} is available!")
    else:
        print(f"{username} is unique!")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")