# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 9 – Course grades (average, best, worst)

courses = {} 
courses['Math'] = int(input('Enter grade for Math: ')) 
courses['Physics'] = int(input('Enter grade for Physics: ')) 
courses['AI'] = int(input('Enter grade for AI: ')) 
  
avg = sum(courses.values()) / len(courses) 
best = max(courses, key=courses.get) 
worst = min(courses, key=courses.get) 
  
print('Average grade:', round(avg, 2)) 
print('Highest grade:', best, courses[best]) 
print('Lowest grade:', worst, courses[worst]) 

# Allow any number of courses until the user types 'done'. 

courses = {}

while True:
    course_name = input("Enter grade (or 'done' to finish): ")
    if course_name == 'done':
        break
    grade = int(input(f"Enter grade for {course_name}: "))
    courses[course_name] = grade

avg = sum(courses.values()) / len(courses) 
best = max(courses, key=courses.get) 
worst = min(courses, key=courses.get) 

print("\nAll courses:", courses)
print('Average grade:', round(avg, 2)) 
print('Highest grade:', best, courses[best]) 
print('Lowest grade:', worst, courses[worst]) 

# Save the results to CSV (course, grade) for later analysis.

import pandas as pd

courses = {}

while True:
    course_name = input("Enter course name (or 'done' to finish): ")
    if course_name == 'done':
        break
    grade = int(input(f"Enter grade for {course_name}: "))
    courses[course_name] = grade

if courses:
    avg = sum(courses.values()) / len(courses)
    best = max(courses, key=courses.get)
    worst = min(courses, key=courses.get)

    print("Average grade:", round(avg, 2))
    print("Highest grade:", best, courses[best])
    print("Lowest grade:", worst, courses[worst])

    df = pd.DataFrame({
        "Course": list(courses.keys()),
        "Grade": list(courses.values())
    })
    print(df)

    df.to_csv("grade_ahihi.csv", index=False)
    print("Saved")
else:
    print("No courses entered.")

# Use pandas.Series(courses).describe() to summarize statistics (mean, min, max, std). 

import pandas as pd

courses = {}

while True:
    course_name = input("Enter course name (or 'done' to finish): ")
    if course_name == 'done':
        break
    grade = int(input(f"Enter grade for {course_name}: "))
    courses[course_name] = grade

if courses:
    avg = sum(courses.values()) / len(courses)
    best = max(courses, key=courses.get)
    worst = min(courses, key=courses.get)

    print("Average grade:", round(avg, 2))
    print("Highest grade:", best, courses[best])
    print("Lowest grade:", worst, courses[worst])

    s = pd.Series(courses)
    print("\nSummary statistics:")
    print(s.describe())
else:
    print("No courses entered.")