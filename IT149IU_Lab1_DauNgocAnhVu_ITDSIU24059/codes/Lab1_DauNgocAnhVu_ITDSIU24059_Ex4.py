# Name: Dau Ngoc Anh Vu
# Student ID: ITDSIU24059
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab: 1 - Python Basics
# Task: Exercise 4 - Eggs in boxes

eggs = int(input("Total eggs: "))
per_box = int(input("Eggs per box: "))

if per_box > 0 and eggs >= 0:
    full_boxes = eggs // per_box
    remainder = eggs % per_box

    if remainder > 0:
        boxes = full_boxes + 1
        need_to_fill_last = per_box - remainder
    else:
        boxes = full_boxes
        need_to_fill_last = 0

    print("Number of boxes:", boxes)
    print("Eggs in last box:", remainder if remainder > 0 else per_box)
    print("Eggs needed to fill last box:", need_to_fill_last)

# Draw an ASCII diagram showing boxes and eggs inside. 

    print("\nBox diagram:")
    for i in range(1, full_boxes + 1):
        print(f"Box {i}: [{'o' * per_box}]")

    if remainder > 0:
        box_number = full_boxes + 1
        print(f"Box {box_number}: [{'o' * remainder}{'.' * need_to_fill_last}]")
else:
    print("ERROR")