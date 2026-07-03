# Day 2 - Numbers and Math

# Basic numbers
age = 23
height = 5.11
temperature = -3

print(f"I am {age} years old")
print(f"My height is {height} feet")

# Simple math
print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("6 * 7 =", 6 * 7)
print("20 / 4 =", 20 / 4)
print("10 ** 2 =", 10**2)  # exponent (power)

# Variables with math
years_until_30 = 30 - age
print(f"I will be 30 in {years_until_30} years")

# 1 Exercise: Calculate how many days old you are (assume 365 days in a year. Print it nicely
daysOld = age * 365
print(f"I am {daysOld} days old.")

# 2 Exercise: Ask the User for two numbers and print thier sum, difference, and product.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(f"The sum of {number1} and {number2} is: {number1 + number2}")
print(f"The difference between {number1} and {number2} is : {number1 - number2}")
print(f"The product of {number1} and {number2} is: {number1 * number2}")

# 3 Exercise: Create a tip calculator
billAmount = float(input("Enter the bill amount: "))
tipPercentage = float(
    input("Enter the percentage you would like to tip (e.g., 15 for 15%): ")
)
tipAmount = billAmount * (tipPercentage / 100)
totalAmount = billAmount + tipAmount
print(f"Total amount to pay: ${totalAmount:.2f}(including a tip of ${tipAmount:.2f})")
