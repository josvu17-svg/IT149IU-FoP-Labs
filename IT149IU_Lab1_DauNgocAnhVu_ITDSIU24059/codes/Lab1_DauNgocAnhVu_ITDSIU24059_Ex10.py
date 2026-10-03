# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 10 – Seconds to hours – minutes – seconds

total_seconds = int(input("Enter a number of seconds (> 3600): ")) 
hours = total_seconds // 3600 
# TODO: compute minutes and seconds using // and % 
minutes = (total_seconds - (3600 * hours)) // 60  
seconds = ( total_seconds - (3600 * hours) - (60 * minutes)) // 60
print(f"{hours} - {minutes} - {seconds}") 

total_seconds = int(input("Enter a number of seconds (> 3600): ")) 
hours = total_seconds // 3600 
# TODO: compute minutes and seconds using // and % 
minutes = (total_seconds - (3600 * hours)) // 60  
seconds = ( total_seconds - (3600 * hours) - (60 * minutes)) // 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}") 