# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 11 – Employee wage growth / decline

o = 10.0                 # original hourly wage ($/hour) 
  
p_good, n_good = 0.03, 5 
w_good = o * (1 + p_good) ** n_good 
print('After 5 years good reviews:', round(w_good, 2)) 
  
p_bad, n_bad = -0.03, 2 
w_bad = o * (1 + p_bad) ** n_bad 
print('After 2 years bad reviews:', round(w_bad, 2)) 


# Let the user input o, p, and n; compute the final wage.

o = float(input("Enter your begin wage: "))
p = float(input("Enter a percentage: "))
n = int(input("Enter your years in your job: "))

w = o * (1 + p) ** n

print(f"After {n} years, your wages are: ", round(w, 2))

# Accept a sequence of reviews like ['good', 'bad', 'good'] and apply 1.03 or 0.97 each year.

o = 10.0
reviews = ['good', 'bad', 'good']

wage = o
for year, review in enumerate(reviews, start=1):
    if review == 'good':
        wage = wage * 1.03
    else:
        wage = wage * 0.97
    print(f"After year {year} ({review}): {round(wage, 2)}")

print("Final wage:", round(wage, 2))

# Plot wage-by-year using matplotlib to visualize the compounding effect.

import matplotlib.pyplot as plt

o = 10.0
reviews = ['good', 'bad', 'good']

years = [0]
wages = [o]

wage = o
for year, review in enumerate(reviews, start=1):
    if review == 'good':
        wage = wage * 1.03
    else:
        wage = wage * 0.97
    years.append(year)
    wages.append(wage)
    print(f"After year {year} ({review}): {round(wage, 2)}")

print("Final wage:", round(wage, 2))

plt.plot(years, wages, marker="o")
plt.xlabel("Year")
plt.ylabel("Hourly wage ($)")
plt.title("Wage Over Time (Compound Growth/Decay)")
plt.grid(True)
plt.show()