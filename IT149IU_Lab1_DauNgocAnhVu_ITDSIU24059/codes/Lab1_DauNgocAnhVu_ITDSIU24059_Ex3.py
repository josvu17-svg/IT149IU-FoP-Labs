# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 3 – Arithmetic operators


left_operands = [-5, 0, 5, 7.5] 
right_operand = 2 
  
for a in left_operands: 
    print(f"\nTesting with left operand = {a}") 
    print(a, "+", right_operand, "=", a + right_operand) 
    print(a, "-", right_operand, "=", a - right_operand) 
    print(a, "*", right_operand, "=", a * right_operand) 
    print(a, "/", right_operand, "=", a / right_operand) 
    print(a, "//", right_operand, "=", a // right_operand) 
    print(a, "**", right_operand, "=", a ** right_operand)
    print(a, "**", "0.5", "=", a ** 0.5)


left_operands = [-5, 0, 5, 7.5]
right_operand = 2

print(f"{'a':>6}{'a + 2':>10}{'a - 2':>10}{'a * 2':>10}{'a / 2':>10}{'a // 2':>10}{'a ** 2':>10}")
print("-" * 66)

for a in left_operands:
    print(f"{a:>6}"
          f"{a + right_operand:>10}"
          f"{a - right_operand:>10}"
          f"{a * right_operand:>10}"
          f"{a / right_operand:>10}"
          f"{a // right_operand:>10}"
          f"{a ** right_operand:>10}")