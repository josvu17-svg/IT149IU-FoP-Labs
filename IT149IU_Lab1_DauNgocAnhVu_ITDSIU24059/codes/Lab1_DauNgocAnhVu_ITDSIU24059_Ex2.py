# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 2 - Fixing the input type


#Correct code
number = int(input("Input a number between 1 and 10: ")) 
square = number * number 
print("The square is:", square)

# Extension 
# Check the range [1, 10] and print an error if the number is out of range.

number = int(input("Input a number between 1 and 10: "))
if 1 <= number <= 10:
    square = number * number
    print("The square is:", square)
else:
    print("ERROR, number out of the range! ")

# Allow multiple numbers (loop from 1 to 5 and print the squares).

for number in range(1,6):
    square = number * number
    print(f"{number} squared is {square}")