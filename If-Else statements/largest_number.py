num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is largest number")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is largest number")
else:
    print(f"{num3} is largest number")