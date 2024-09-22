# Write a Python program to check if a number is divisible by both 5 and 7.

number = int(input("Enter number :"))

if number % 5 == 0 and number % 7 ==0 :
    print(f"{number} is divisible by both 5 and 7")
else :
    print(f"{number} is not divisible by both 5 and 7")