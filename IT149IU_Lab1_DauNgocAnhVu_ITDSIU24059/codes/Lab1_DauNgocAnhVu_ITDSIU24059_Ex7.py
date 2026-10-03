# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 7 – Right-aligned bacteria growth table 

base = 200 
hours = [0, 5, 10, 15] 
print(f'{"Hour":>5}\t{"Number of Bacteria":>12}') 
for h in hours: 
    B = base * (2 ** h) 
    print(f'{h:>5}\t{B:>12}')

# Add more hours dynamically and keep the alignment consistent.

base = 200
max_hour = int(input("Enter Hour: "))
print(f'{"Hour":>5}\t{"Number of Bacteria":>12}') 
for h in range(1, max_hour +1): 
    B = base * (2 ** h) 
    print(f'{h:>5}\t{B:>20}')

# Export the table to CSV/Excel for analysis in pandas. 

import pandas as pd

base = 200
max_hour = int(input("Enter Hour: "))

hours = []
bacteria = []

for h in range(0, max_hour + 1):
    hours.append(h)
    bacteria.append(base * (2 ** h))

df = pd.DataFrame({"Hour": hours, "Number of Bacteria": bacteria})
print(df)

df.to_csv("bacteria_growth.csv", index=False)
print("Saved to bacteria_growth.csv")