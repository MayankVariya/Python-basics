# Write a Python program to create a function that takes two numbers as arguments and returns their sum.

def sum(num1,num2):
    return num1 + num2


num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

sum = sum(num1, num2)

print(f"Sum of two number is :{sum}")