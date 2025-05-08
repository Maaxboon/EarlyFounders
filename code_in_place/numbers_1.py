#!/usr/bin/env python3
def main():
    print("This program adds two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter the second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total is " + str(total) + ".")
main()