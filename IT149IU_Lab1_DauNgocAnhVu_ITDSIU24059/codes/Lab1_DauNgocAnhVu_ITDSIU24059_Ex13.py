# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 13 – BMI calculator 

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    type_body = 'Underweight'
elif 18.5 <= BMI < 25:
    type_body = 'Normal'
elif 25 <= BMI < 30:
    type_body = 'Overweight'
elif BMI >= 30:
    type_body = 'obese'
print('Weight (kg): ', weight)
print('Height (m): ', height)
print(f"BMI = {BMI:.1f} -> {type_body}")