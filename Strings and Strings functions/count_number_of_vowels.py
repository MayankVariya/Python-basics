# Write a Python program to count the number of vowels in a given string.

vowels = "aeiouAEIOU"

input_string = input("Enter a string :")

count = 0

for char in input_string :
    if(char in vowels) :
        count += 1

print(f"Number of vowels available in your string :{count}")