"""
Calculator module.

This module provides functions to perform basic calculations.
"""
import os

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

def sum_values(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The difference of the two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of the two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The quotient of the two numbers, or None if division by zero occurs.
    """
    if b == 0:
        print("Cannot divide by zero.")
        return None
    return a / b

def calculator():
    """
    Runs a simple calculator application.
    """
    clear_screen()

    while True:
        try:
            a = int(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        operation = input("Enter type of operation (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue

        try:
            b = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operation == "+":
            result = sum_values(a, b)
            print(f"Sum of {a} and {b} is {result}")
        elif operation == "-":
            result = subtract(a, b)
            print(f"Subtraction of {a} and {b} is {result}")
        elif operation == "*":
            result = multiply(a, b)
            print(f"Multiplication of {a} and {b} is {result}")
        elif operation == "/":
            result = divide(a, b)
            if result is not None:  # Update a only if division is successful
                print(f"Division of {a} and {b} is {result}")
            else:
                continue

        a = result
        choice = input("Press any key to continue with result or 'x' to exit: ").lower()
        if choice == 'x':
            print("Exiting the calculator. Goodbye!")
            break

        clear_screen()

calculator()