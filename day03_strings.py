# Day 3 - Strings and Decisions

name = "Alex"
greeting = "Hello, " + name + "!"
print(greeting)

# Better way with f-strings
print(f"Welcome back, {name.upper()}!")

# String methods
message = "  python is fun  "
print(message.strip().title())

# Length and checking
print(f"Length of name: {len(name)} characters")

# Exercises for me
# 01 - Ask the user for full name and return how many characters it has, it in upper and lowercase.
full_name = input("Please provide your full name: ")
print(f"Your full name has {len(full_name)} characters.")
print(f"Your full name in uppercase: {full_name.upper()}")
print(f"Your full name in lowercase: {full_name.lower()}")
# 02 - Create a simple password checker based on length
password = input("Please create a password(must be at least 8 characters long): ")
if len(password) < 8:
    print("Password is too short")
else:
    print("Password looks good!")

# 03 - Create a mad libs story generator using user input for nouns, verbs, and adjectives, and place.
noun = input("Please provide a noun: ")
verb = input("Please provide a verb: ")
adjective = input("Please provide an adjective: ")
place = input("Please provide a place: ")

print(
    f"Once upon a time in faraway {place}, there was a {adjective} {noun} that loved to {verb} like crazy. Everyone in {place} was astonished by the {adjective} {noun}'s ability to {verb} and they all lived happily together in {place}."
)
