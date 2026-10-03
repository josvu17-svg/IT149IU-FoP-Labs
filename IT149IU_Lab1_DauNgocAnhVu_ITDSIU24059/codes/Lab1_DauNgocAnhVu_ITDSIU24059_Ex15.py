# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 15 – Digits of a number

number = int(input("Enter a three-digit integer: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

digit_sum = hundreds + tens + units
reversed_number = units * 100 + tens * 10 + hundreds

print("Hundreds digit:", hundreds)
print("Tens digit:", tens)
print("Units digit:", units)
print("Sum of digits:", digit_sum)
print("Reversed number:", reversed_number)

if number == reversed_number:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")