cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# Checking Multiple Conditions or & and
# Checking Whether a Value Is in a List
# To find out whether a particular value is already in a list, use the keyword in
# Checking Whether a Value Is Not in a List
# Other times, it’s important to know if a value does not appear in a list. You 
# can use the keyword not in this situation.
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
# if Statements
age = 90
if age >= 18:
    # Indentation plays the same role in if statements as it did in for loops
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
    
# if-else Statements
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
    # The if-elif-else Chain
    
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
# The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data
    price = 20
    
print(f"Your admission cost is ${price}.")

# sometimes it’s important to check all conditions of interest. In 
# this case, you should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True

requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
    
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")

# In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements

# Using if Statements with Lists