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