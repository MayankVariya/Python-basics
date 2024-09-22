# Write a Python program to count the frequency of each word in a given sentence using a dictionary.

sentence = input("Enter any snetense :")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(f"World of frequency is :{frequency}")