# Day 4 - Loops
import random

# For loop - repeat a fixed number of times
for i in range(5):
    print(f"Count: {i + 1}")

# While loop - repeat while a condition is true
count = 0
while count < 3:
    print("Learning is fun!")
    count += 1

# Exercise 01: Use a for loop to print the multiplication table of 7 from 1 to 10.
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Exercise 02: Use a while loop to keep asking for user input until they type 'stop'.
user_input = input("What is your favorite food? (Type 'stop' to end): ")
while user_input.lower() != "stop":
    print(f"Yum! {user_input} sounds good!")
    user_input = input("What is your favorite food? (Type 'stop' to end): ")
else:
    print("Thanks for sharing your favorite foods!")

# Exercise 03: Build a number guessing game

secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 6
print("I'm thinking of a number between 1 and 20. You have 6 tries to guess it.")
while guesses < max_guesses:
    guess = int(input("Take a guess: "))
    guesses += 1
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed my number in {guesses} tries!")
        break

if guesses == max_guesses and guess != secret_number:
    print(
        f"Sorry, you've used up all your guesses. The number I was thinking of was {secret_number}."
    )
