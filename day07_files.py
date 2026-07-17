# Day 7 - Reading and Writing Files
from datetime import datetime

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Hello, this is my first file!\n")
    file.write("Python is awesome.\n")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("notes.txt", "a") as file:
    file.write("This line was appended later.\n")

# Exercise 01 Write a program that ask the user for their name and favorite hobby, then saves it to a file called profile.txt
name = input("Enter your name: ")
hobby = input("Enter your favorite hobby: ")
with open("profile.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Hobby: {hobby}\n")

# Exercise 02 read the profile.txt file and print its content nicely
with open("profile.txt", "r") as file:
    profile_content = file.read()
    print("Profile Information: ")
    print(f"{profile_content}")

# Exercise 03 Create a journal program
today = datetime.now().strftime("%Y-%m-%d")
while True:
    print("1. Make a new entry\n")
    print("2. Read your previous entries\n")
    print("3. Close your journal\n")

    choice = input(
        "Welcome to your Journal please choose from the provided options: \n"
    )

    if choice == "1":
        entry = input("What would you like to write: \n")
        with open("Journal.txt", "a") as file:
            file.write(f"{today}\n")
            file.write(f"{entry}\n")
    elif choice == "2":
        with open("Journal.txt", "r") as file:
            JournalContents = file.read()
            print("Here are the previous entries: \n")
            print(f"{JournalContents}")
    elif choice == "3":
        break
    else:
        print("Choice is invalid. Please select another option")
