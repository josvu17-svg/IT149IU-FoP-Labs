# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 12 – Sorting runner times with if only 

a = float(input('Enter time for runner 1: ')) 
b = float(input('Enter time for runner 2: ')) 
c = float(input('Enter time for runner 3: ')) 
  
print('Times in ascending order:') 
if a <= b and b <= c: print(a, b, c) 
if a <= c and c <= b: print(a, c, b) 
if b <= a and a <= c: print(b, a, c) 
if b <= c and c <= a: print(b, c, a) 
if c <= a and a <= b: print(c, a, b) 
if c <= b and b <= a: print(c, b, a) 

# Extension: remove the duplicate-printing problem by using strict comparisons for some of the conditions (e.g. a <= b and b < c) or a variable printed = False; then print which runner (1, 2 or 3) won.

a = float(input('Enter time for runner 1: '))
b = float(input('Enter time for runner 2: '))
c = float(input('Enter time for runner 3: '))

printed = False

print('Times in ascending order:')
if a <= b and b <= c and not printed:
    print(a, b, c)
    printed = True
if a <= c and c <= b and not printed:
    print(a, c, b)
    printed = True
if b <= a and a <= c and not printed:
    print(b, a, c)
    printed = True
if b <= c and c <= a and not printed:
    print(b, c, a)
    printed = True
if c <= a and a <= b and not printed:
    print(c, a, b)
    printed = True
if c <= b and b <= a and not printed:
    print(c, b, a)
    printed = True