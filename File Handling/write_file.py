# Write a Python program to write a list of numbers to a file.

list = [23, 34, 55, 12, 78, 63]

with open('File Handling/numbers.txt','w') as file:
    for number in list:
        file.write(str(number)+'\n')

print("Numbers written to file successfully.")