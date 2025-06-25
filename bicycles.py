bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#Accessing Elements in a List using Indexes
print(bicycles[0])  # trek
#You can also apply string methods to each element in a list.
print(bicycles[0].title())  # Trek
#indexes start at 0, so the first item in a list is at index 0.
#The second item is at index 1, and so on.
#You can access the last element in a list by using the index -1.
#Using negative indexes allows you to access elements from the end of the list.
print(bicycles[-1])  # specialized
#You can use any integer expression, as long as it can be evaluated to a nonnegative integer representing an index in the list.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)  # My first bicycle was a Trek.