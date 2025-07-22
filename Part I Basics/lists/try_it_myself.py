my_friends_names = ['Kuria', 'John', 'Lavenda', 'Mercy']
print(my_friends_names)
print(my_friends_names[0])
print(my_friends_names[1])
print(my_friends_names[2])
print(my_friends_names[3])

message = f"My freinds names are as follows:\n {my_friends_names[0]}\n {my_friends_names[1]}\n {my_friends_names[2]}\n {my_friends_names[3]}. They have been my friends for the past 10 years. "
print(message)

my_mode_of_trabsportation = ['Motorbike', 'Train', "Aeroplane"]

print(f"My favorite mode of transport is by {my_mode_of_trabsportation[2]}.")

dinner_guest_list = ['Jememiah', 'Samuel', 'Lavenda']
guest_one_message = f"Hi {dinner_guest_list[0]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_two_message = f"Hi {dinner_guest_list[1]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_three_message = f"Hi {dinner_guest_list[2]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"

print(guest_one_message)
print(guest_two_message)
print(guest_three_message)
cannot_attend = dinner_guest_list.pop(0)
print(f"Unfortunately {cannot_attend} will not be attending the party.")
print(dinner_guest_list)
dinner_guest_list.insert(0, 'Emmah')
print(dinner_guest_list)

guest_one_message = f"Hi {dinner_guest_list[0]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
print(f'{guest_one_message}\n{guest_two_message}\n{guest_three_message}\n')

print("I have some good news. I found a bigger table and this more guest!")
dinner_guest_list.insert(0, 'Stephen')
dinner_guest_list.insert(2, 'Esther')
dinner_guest_list.append("Ann")
print(dinner_guest_list)

guest_one_message = f"Hi {dinner_guest_list[0]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_two_message = f"Hi {dinner_guest_list[1]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_three_message = f"Hi {dinner_guest_list[2]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_four_message = f"Hi {dinner_guest_list[3]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_five_message = f"Hi {dinner_guest_list[4]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_six_message = f"Hi {dinner_guest_list[5]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"

# 

print(f'{guest_one_message}\n{guest_two_message}\n{guest_three_message}\n{guest_four_message}\n{guest_five_message}\n{guest_six_message}\n')

print("Friends sorry for communicating this rate, unfortunately the table won't be arriving on time and I will have a table that can only accomodate 2 people.")
removed_guest = dinner_guest_list.pop()
print(f"{removed_guest} I can't manage to invite you for the dinner due to space constraints.")
removed_guest = dinner_guest_list.pop()
print(f"{removed_guest} I can't manage to invite you for the dinner due to space constraints.")
removed_guest = dinner_guest_list.pop()
print(f"{removed_guest} I can't manage to invite you for the dinner due to space constraints.")
removed_guest = dinner_guest_list.pop()
print(f"{removed_guest} I can't manage to invite you for the dinner due to space constraints.")
print(dinner_guest_list)

guest_one_message = f"Hi {dinner_guest_list[0]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"
guest_two_message = f"Hi {dinner_guest_list[1]}, I hope you are doing well I am officially inviting you to a dinner party at Panari hotel today at 7:30 PM"

print(f'{guest_one_message}\n{guest_two_message}\n')

del dinner_guest_list[0]
del dinner_guest_list[0]
print(dinner_guest_list)

places_to_visit = ['zanzibar', 'rwanda', 'usa', 'liverpool', 'china']
print(places_to_visit)

print(sorted(places_to_visit))

print(places_to_visit)

print(sorted(places_to_visit, reverse=True))

print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.sort(reverse=True)
print(places_to_visit)

print(len(places_to_visit))