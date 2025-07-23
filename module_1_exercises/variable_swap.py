"""
File name: variable_swap.py
Purpose: Swap two user-input numbers
Author: Maxwel Okoth
Date: 2025-07-07
"""
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

# Swap logic
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# Assigning original values 
temp = b
b = a
a = temp

print("After reassigning:")
print("a =", a)
print("b =", b)