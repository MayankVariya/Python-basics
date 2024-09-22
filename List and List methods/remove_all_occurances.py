# Write a Python program to remove all occurrences of a specified element from a list.

list = [ 1, 2, 5, 2, 4 ,2]

element = int(input("Enter number you want to remove in list :"))

updated_list = [number for number in list if number != element]

print(f"Your updated list is :{updated_list}")