# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 14 – Cash withdrawal (//, %) 

money = int(input("Enter your money: "))

note_500k = money // 500000
remainder = money % 500000

note_200k = remainder // 200000
remainder = remainder % 200000

note_100k = remainder // 100000
remainder = remainder % 100000

note_50k = remainder // 50000
remainder = remainder % 50000

print("Amount (VND): ", money)
print("500,000 x ", note_500k)
print("200,000 x ", note_200k)
print("100,000 x ", note_100k)
print("50,000 x ", note_50k)