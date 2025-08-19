# Python refers to values that cannot change as immutable,and an immutable list is called a tuple.

# A tuple looks just like a list, except you use parentheses instead of square brackets.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 500

# Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:
constant_number = (3,)

for dimension in dimensions:
    print(dimension)
    
# Writing Over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple. For example, if we wanted to change the dimensions of this rectangle, we could redefine the entire tuple:
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
    
dimensions = (300, 400)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)