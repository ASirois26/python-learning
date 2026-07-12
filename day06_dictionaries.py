# Day 6 - Dictionaries (Key-Value storage)

person = {"name": "Alex", "age": 23, "city": "Haw River", "skills": ["Python", "Git"]}

print(person["name"])
print(person.get("age"))  # Safer way to access

# Adding or updating
person["job"] = "Developer"
person["age"] = 26

# Looping through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Exercise 01: Create a dictionary called student that contains name, grade (int), and subjects (list of 3 subjects). Then print it all in a nice format
student = {
    "name": "Alexander",
    "grade": 12,
    "subjects": ["Python", "Orderfilling", "Git"],
}
for key, value in student.items():
    print(f"{key}: {value}")


# Exercise 02: Create a function called wordfrequency(sentence) that takes a sentence and returns a dictionary with the frequency of each word in the Sentence.
def wordfrequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


sentence = "This is a test. This is a test."
print(wordfrequency(sentence))

# Exercise 03: Build a simple contact book where key is the name and phone number is the value. Menu options add contact, view all contacts, search contact, quit.
contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")


def quit():
    print("Exiting contact book.")
    exit()


while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == "4":
        quit()
    else:
        print("Invalid choice. Please try again.")
