# Write a Python program to check if a number is positive, negative, or zero.

number = int(input("Enter a number :"))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")