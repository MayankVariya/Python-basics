# Write a Python program to print the Fibonacci sequence up to a given number.

a, b =0, 1

n = int(input("Enter number :"))

while a <= n:
    print(f" {a}",end='')
    a, b = b, a + b