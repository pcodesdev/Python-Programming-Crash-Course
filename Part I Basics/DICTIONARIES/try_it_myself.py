my_supervisor_details = {
    'first_name': 'Alexon',
    'last_name': 'Mwasi',
    'age': 50,
    'city': 'Taita Taveta',
}

print(f"My supervisor details are as followw; his name is {my_supervisor_details['first_name']} {my_supervisor_details['last_name']}, he is {my_supervisor_details['age']} years old and he comes from {my_supervisor_details['city']}")

friends_favorite_number = {
    'Samuel': 24,
    'Dan': 37,
    'Pius': 59,
    'Lavenda': 10,
    'Mercy': 1,
}

for key, value in friends_favorite_number.items():
    print(f"{key} favorite number is {value}.")
    
    
glossary = {
    "for": "Creates a loop to iterate over a sequence (e.g., list, dictionary, or range), used for repeating tasks over multiple items",
    "if": "Introduces a conditional statement to execute code only when a specified condition is true, enabling decision-making",
    "def": "Defines a function, specifying its name and parameters to create reusable code blocks for specific tasks",
    "return": "Exits a function and sends a value back to the caller, used to output results for further use",
    "import": "Brings external modules or libraries into a program, providing access to additional functions and tools",
}

for key, value in glossary.items():
    print(f"{key}: {value}.\n")
    
# PART II
major_rivers = {
    "Amazon": "Brazil",
    "Nile": "Egypt", 
    "Yangtze": "China"
}

for river, country in major_rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")
    
for river in  major_rivers.keys():
    print(river.title())
    
for country in major_rivers.values():
    print(country.title())
    
favorite_languages = {
    "Alice": "Python",
    "Bob": "JavaScript", 
    "Charlie": "Java",
    "Diana": "C++",
    "Emma": "Go",
    "Frank": "Rust",
    "Grace": "TypeScript",
    "Henry": "Swift",
}

poll_participants = [
    "Alice",      # Already in dictionary
    "Bob",        # Already in dictionary
    "Charlie",    # Already in dictionary
    "Grace",      # Already in dictionary
    "Jessica",    # Not in dictionary
    "Mike",       # Not in dictionary
    "Sarah",      # Not in dictionary
    "David",      # Not in dictionary
    "Lisa",       # Not in dictionary
    "Kevin",      # Not in dictionary
    "Emma",       # Already in dictionary
    "Rachel",     # Not in dictionary
    "Tom",        # Not in dictionary
]

for person in poll_participants:
    print(f"\nHi {person}.")
    if person in favorite_languages:
        print(f"{person} thank you for participating in the poll.")
        print(f"Your favorite language is {favorite_languages[person]}")
        
    else:
        print(f"{person} kindly take the poll.")