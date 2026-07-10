# Day 5 - Functions and Lists

# Simple function
def greet(name):
    print(f"Hello, {name}! Welcome back.")


greet("Alex")


# Function with return value
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 15)
print("Sum:", result)

# Lists
fruits = ["apple", "banana", "cherry", "mango"]
print(fruits[0])  # First item
print(fruits[-1])  # Last item
fruits.append("orange")
print(fruits)


# Exercise 1: Write a function called calculate_average that takes a list of numbers as input and returns the average of those numbers.
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average)


# Exercise 2: Write a function is_even that takes a number and returns True if the number is even, and False otherwise.
def is_even(number):
    return number % 2 == 0


print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))

# Exercise 3: Create a shopping list manager:
# start with an empty list, give the user options, add item, remove item, view list, and quit, use a while loop + functions
shopping_list = []


def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to your shopping list.")


def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")


def view_list():
    if shopping_list:
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")


def quit_program():
    print("Exiting the shopping list manager. Goodbye!")
    exit()


while True:
    print("\n1. Add item\n2. Remove item\n3. View list\n4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter item you would like to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter item you would like to remove: ")
        remove_item(item)
    elif choice == "3":
        view_list()
    elif choice == "4":
        quit_program()
    else:
        print("Invalid choice. Please try again.")
