# Write a Python program to calculate the nth Fibonacci number using recursion.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num = int(input("Enter a number: "))

print(f"The {num}th Fibonacci number is: {fibonacci(num)}")