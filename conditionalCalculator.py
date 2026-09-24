"""
Filename: conditional_calculator.py
Author: <Cortez, Ethan>
Created: <09/22/2026>
Instructor: Burgess
"""

print("Hello! Welcome to Conditional Calculator!")
print("Please enter a number down below:")
n1=int(input("Number 1:"))
n2=int(input("Number 2:"))

print("Please enter your choice of operation:")
print("For addition enter: add")
print("For subtraction enter: sub")
print("For multiplication enter: mult")
print("For division enter: div")

operation = input("Enter operation (+, -, *, /): ")

if operation =="+":
    print("The sum is",n1+n2)
if operation =="-":
    print("The difference is",n1-n2)
if operation =="*":
    print("The product is",n1*n2)
if operation =="/":
    print("The quotient is",n1/n2)
    if n2 == 0:
        print("Error: Cannot divide by zero")
