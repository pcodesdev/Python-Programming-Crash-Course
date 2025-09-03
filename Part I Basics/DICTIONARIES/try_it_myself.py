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