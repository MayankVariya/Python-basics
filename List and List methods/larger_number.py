# Write a Python program to find the largest number in a list.

list = [ 1, 4, 7, 23, 5, 3, 15]

largest = 0

for number in list :
    if number > largest :
        largest = number


print(f"Largest number is :{largest}")
