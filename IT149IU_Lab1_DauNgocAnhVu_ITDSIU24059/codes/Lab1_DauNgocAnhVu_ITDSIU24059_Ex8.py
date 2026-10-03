# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 8 – Name score with ord() 

def name_score(name): 
    return sum(ord(c) for c in name) 
  
tom_score = name_score("Tom") 
jim_score = name_score("Jim") 
print("Tom score:", tom_score) 
print("Jim score:", jim_score) 
  
if tom_score > jim_score: 
    print("Tom goes first!") 
elif jim_score > tom_score: 
    print("Jim goes first!") 
else: 
    print("It's a tie!") 

# Allow user input of multiple names and compute their scores.

def name_score(name):
    return sum(ord(c) for c in name)

n= int(input("How many names do you wanna enter? "))

for i in range(n):
    name =input(f"Enter name {i+1}: ")
    score = name_score(name)
    print(f"{name} Score: {score}")

# Write a function winner(names_list) that finds the name with the highest score.

def name_score(name):
    return sum(ord(c) for c in name)

def winner(names_list):
    return max(names_list, key=name_score)

names = ["Tom", "Jim", "Anh", "Vu"]

for name in names:
    print(f"{name} score: {name_score(name)}")

print("Winner:", winner(names))

# Compare results across different names to observe how ASCII values affect outcomes.

def name_score(name):
    return sum(ord(c) for c in name)

def winner(names_list):
    return max(names_list, key=name_score)

test_cases = [
    ["Tom", "Jim"],
    ["tom", "jim"],
    ["Anna", "Ann"],
    ["Zed", "Abby"],
]

for names in test_cases:
    print(f"\nComparing: {names}")
    for name in names:
        print(f"  {name} -> score {name_score(name)}")
    print("  Winner:", winner(names))