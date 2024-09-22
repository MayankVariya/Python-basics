# Write a Python program to read a file and count the number of words.

def countWords(fileName):
    with open(fileName, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

print(f"sample.txt file words count is: {countWords('File Handling/sample.txt')}")