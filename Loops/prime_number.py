# Write a Python program to print all prime numbers between 1 and 100.

for num in range(1, 101):
    if num > 1:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                print(f"{num} is not prime number")
                break
        else:
            print(f"{num} is prime number")
    else:
       print(f"{num} is not prime number") 
    

