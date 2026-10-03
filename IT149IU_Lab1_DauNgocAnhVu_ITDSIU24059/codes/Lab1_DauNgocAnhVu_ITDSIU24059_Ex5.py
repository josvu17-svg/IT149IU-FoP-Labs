# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 5 – Odd or even with the remainder operator

number = int(input("Enter an integer: ")) 
  
if number % 2 == 0: 
    print(number, "is even") 
else: 
    print(number, "is odd") 


#Use a for-loop to print the odd/even classification for the numbers 1–10.
even= []
odd= []

for i in range(1,11):
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
print("Numbers are even: ", even)
print("Numbers are odd: ", odd)


#In pandas, filter DataFrame rows by even/odd index using df.index % 2. 
import pandas as pd

data = {"number": list(range(1, 11))}
df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)

even_rows = df[df.index % 2 == 0]
odd_rows = df[df.index % 2 != 0]

print("\nRows with even index:")
print(even_rows)

print("\nRows with odd index:")
print(odd_rows)