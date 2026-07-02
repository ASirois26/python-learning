# Day 1 - Python Basics
# 1. Print Statements
print("Hello, Python!")
print("I am learning to code")

# 2. Variables
name = "Alexander"
age = 23
height = "5'10\""

print("My name is", name)
print("I am", age, "years old")
print("I am", height, "feet tall")

# 3. f-strings (modern)
print(f"My name is {name} and I am {age} years old. I am {height} feet tall.")

# 4. User Inputs
favorite_color = input("What is your favorite color? ")
print(f"Your favorite color is {favorite_color}.")

# 5. Some more practice with variables and f-strings
city = "Boston"
print(f"I love {city}.")
favorite_food = "Mac and Cheese"
print(f"My favorite food is {favorite_food}.")

# 6. user inputs and calculations
birth_year = int(input("What year were you born? "))
current_year = 2026
age = current_year - birth_year
print(f"You are {age} years old.")

# 7. A short story using variables
name = "Alexander"
favorite_color = "orange"
favorite_food = "Mac and Cheese"
car = "Kia K4"

print(f"Once upon a time, there was a person named {name}.")
print(f"{name} loved the color {favorite_color} and enjoyed eating {favorite_food}.")
print(f"One day, {name} bought a new car, a {car}, and went on an adventure.")
