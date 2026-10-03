# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 6 – Bacteria growth table 

base = 200
hours = [0, 5, 10, 15]
print("Hour\tNumber of Bacteria")
for h in hours:
    B = base * (2 ** h)
    print(f"{h}\t{B}")

# Allow the user to input a maximum hour and print the table for 0..max.

base = 200
max_hour = int(input("Enter Hour: "))
print("Hour\tNumber of Bacteria")
for h in range(1, max_hour+1):
    B = base * (2 ** h)
    print(f"{h}\t{B}")

# Add a step size to control how often results are printed.

base = 200
max_hour = int(input("Enter Hour: "))
print("Hour\tNumber of Bacteria")
for h in range(1, max_hour+1, 5):
    B = base * (2 ** h)
    print(f"{h}\t{B}")

# Plot the bacteria growth curve using matplotlib.

import matplotlib.pyplot as plt

base = 200
max_hour = int(input("Enter Hour: "))

hours = []
bacteria = []

print("Hour\tNumber of Bacteria")
for h in range(0, max_hour + 1):
    B = base * (2 ** h)
    print(f"{h}\t{B}")
    hours.append(h)
    bacteria.append(B)

plt.plot(hours, bacteria, marker="o")
plt.xlabel("Hour")
plt.ylabel("Number of Bacteria")
plt.title("Bacteria Growth Over Time")
plt.grid(True)
plt.show()