# Write a Python program to create a function that checks whether a string is a palindrome

def is_palindrome(string):
    if string == string[::-1]:
        print(f"{string} is palindrome string")
    else:
        print(f"{string} is not palindrome string") 

input_string = input("Enter string :")

is_palindrome(input_string)