friends_name = ["John","Samuel","Pius","Emmanuel","David"]
print(friends_name[0])  # John
print(friends_name[1])  # Samuel
print(friends_name[2])  # Pius
print(friends_name[3])  # Emmanuel
print(friends_name[4])  # David

greeting_1 = f"Hello {friends_name[0]}!"
greeting_2 = f"Hello {friends_name[1]}!"
greeting_3 = f"Hello {friends_name[2]}!"
greeting_4 = f"Hello {friends_name[3]}!"
greeting_5 = f"Hello {friends_name[4]}!"
print(greeting_1)  # Hello John!
print(greeting_2)  # Hello Samuel!
print(greeting_3)  # Hello Pius!
print(greeting_4)  # Hello Emmanuel!
print(greeting_5)  # Hello David!

modes_of_transportation = ["car", "bus", "bicycle", "train", "airplane"] 

travel_message = f"I would like to own an {modes_of_transportation[4]} for long distance travel."
print(travel_message)  # I would like to own an airplane for long distance travel.  

# Try it yourself
friends_dinner_invite = ["John", "Samuel", "Pius", "Emmanuel", "David"]
message_1 = f"Hello {friends_dinner_invite[0]}, I would like to invite you to dinner."
message_2 = f"Hello {friends_dinner_invite[1]}, I would like to invite you to dinner."
message_3 = f"Hello {friends_dinner_invite[2]}, I would like to invite you to dinner."
message_4 = f"Hello {friends_dinner_invite[3]}, I would like to invite you to dinner."
message_5 = f"Hello {friends_dinner_invite[4]}, I would like to invite you to dinner."
print(message_1)  # Hello John, I would like to invite you to dinner.
print(message_2)  # Hello Samuel, I would like to invite you to dinner.
print(message_3)  # Hello Pius, I would like to invite you to dinner.
print(message_4)  # Hello Emmanuel, I would like to invite you to dinner. 
print(message_5)  # Hello David, I would like to invite you to dinner. 
print(f"{friends_dinner_invite[4]} can't make it to the dinner.")  # David can't make it to the dinner. 
# Removing David from the list of friends
friends_dinner_invite.remove("David")
print(friends_dinner_invite)
# Adding a new friend to the list
friends_dinner_invite.append("Michael")
print(friends_dinner_invite)
# Inviting the remaining friends to dinner
message_1 = f"Hello {friends_dinner_invite[0]}, I would like to invite you to dinner."
message_2 = f"Hello {friends_dinner_invite[1]}, I would like to invite you to dinner."      
message_3 = f"Hello {friends_dinner_invite[2]}, I would like to invite you to dinner."
message_4 = f"Hello {friends_dinner_invite[3]}, I would like to invite you to dinner."
print(message_1)  # Hello John, I would like to invite you to dinner.
print(message_2)    # Hello Samuel, I would like to invite you to dinner.                   
print(message_3)  # Hello Pius, I would like to invite you to dinner.
print(message_4)  # Hello Emmanuel, I would like to invite you to dinner.
print(f"\nGreat news! I found a bigger dinner table, so I can invite more friends!")
# Inserting a new guest at the beginning of the list
friends_dinner_invite.insert(0, "Peter")
# Inserting a new guest in the middle of the list   
friends_dinner_invite.insert(2, "Simon")
# Inserting a new guest at the end of the list  
friends_dinner_invite.append("Joseph")
print(friends_dinner_invite)  # ['Peter', 'John', 'Simon', 'Samuel', 'Pius', 'Emmanuel', 'Joseph']o
# Inviting the updated list of friends to dinner
message_1 = f"Hello {friends_dinner_invite[0]}, I would like to invite you to dinner."
message_2 = f"Hello {friends_dinner_invite[1]}, I would like to invite you to dinner."
message_3 = f"Hello {friends_dinner_invite[2]}, I would like to invite you to dinner."
message_4 = f"Hello {friends_dinner_invite[3]}, I would like to invite you to dinner."  
message_5 = f"Hello {friends_dinner_invite[4]}, I would like to invite you to dinner."
message_6 = f"Hello {friends_dinner_invite[5]}, I would like to invite you to dinner."
message_7 = f"Hello {friends_dinner_invite[6]}, I would like to invite you to dinner."
message_8 = f"Hello {friends_dinner_invite[7]}, I would like to invite you to dinner."
print(message_1)  # Hello John, I would like to invite you to dinner.
print(message_2)  # Hello Samuel, I would like to invite you to dinner. 
print(message_3)  # Hello Simon, I would like to invite you to dinner.
print(message_4)  # Hello Pius, I would like to invite you to dinner.
print(message_5)  # Hello Emmanuel, I would like to invite you to dinner.
print(message_6)  # Hello Joseph, I would like to invite you to dinner.
print(message_7)  # Hello John, I would like to invite you to dinner.
print(message_8)  # Hello Peter, I would like to invite you to dinner.
print("\nSorry, I can only invite two people for dinner.") 
# Removing guests from the list one at a time until only two names remain
uninvited_guest = friends_dinner_invite.pop()   
print(f"Sorry {uninvited_guest}, I can't invite you to dinner.")  # Sorry Joseph, I can't invite you to dinner.
uninvited_guest = friends_dinner_invite.pop()   
print(f"Sorry {uninvited_guest}, I can't invite you to dinner.")  # Sorry Emmanuel, I can't invite you to dinner.
uninvited_guest = friends_dinner_invite.pop()   
print(f"Sorry {uninvited_guest}, I can't invite you to dinner.")  # Sorry Pius, I can't invite you to dinner.
uninvited_guest = friends_dinner_invite.pop()   
print(f"Sorry {uninvited_guest}, I can't invite you to dinner.")  # Sorry Samuel, I can't invite you to dinner.
uninvited_guest = friends_dinner_invite.pop()   
print(f"Sorry {uninvited_guest}, I can't invite you to dinner.")  # Sorry Simon, I can't invite you to dinner.
uninvited_guest = friends_dinner_invite.pop()   
print(f"Sorry {uninvited_guest}, I can't invite you to dinner.")  # Sorry John, I can't invite you to dinner.
# Printing the names of the remaining guests
print(f"\n{friends_dinner_invite[0]} and {friends_dinner_invite[1]} are still invited to dinner.")  # Peter and John are still invited to dinner.
# Emptying the list of friends
del friends_dinner_invite[0]  # Remove Peter
del friends_dinner_invite[0]  # Remove John
# Printing the empty list
print(friends_dinner_invite)

places_to_visit = ["Paris", "Tokyo", "New York", "Sydney", "Cape Town"]

print("Original order:")
print(places_to_visit)  # ['Paris', 'Tokyo', 'New York', 'Sydney', 'Cape Town']
print("\nAlphabetical order:")
print(sorted(places_to_visit))  # ['Cape Town', 'New York', 'Paris', 'Sydney', 'Tokyo']
print("\nOriginal order after sorted():")
print(places_to_visit)  # ['Paris', 'Tokyo', 'New York', 'Sydney', 'Cape Town'] 
print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))  # ['Tokyo', 'Sydney', 'Paris', 'New York', 'Cape Town']
print("\nOriginal order after sorted(reverse=True):")
print(places_to_visit)  # ['Paris', 'Tokyo', 'New York', 'Sydney', 'Cape Town']
print("\nReversed order:")  
places_to_visit.reverse()
print(places_to_visit)  # ['Cape Town', 'Sydney', 'New York', 'Tokyo', 'Paris']
print("\nReversed back to original order:")
places_to_visit.reverse()
print(places_to_visit)  # ['Paris', 'Tokyo', 'New York', 'Sydney', 'Cape Town']
print("\nSorted in alphabetical order:")
places_to_visit.sort()
print(places_to_visit)  # ['Cape Town', 'New York', 'Paris', 'Sydney', 'Tokyo']
print("\nSorted in reverse alphabetical order:")
places_to_visit.sort(reverse=True)
print(places_to_visit)  # ['Tokyo', 'Sydney', 'Paris', 'New York', 'Cape Town']

#People to invite to dinner
print(len(friends_dinner_invite))  # 7 