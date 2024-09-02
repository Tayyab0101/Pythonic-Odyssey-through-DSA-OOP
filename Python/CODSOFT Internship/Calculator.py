import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
        return None
    else:
        return a / b
    
def calculator():
    clear_screen()
    a = int(input("Enter first number: "))  # Ask for the first number initially
    while True:
        operation = input("Enter operation: ")
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation")
            continue
        b = int(input("Enter 2nd number: "))
        
        if operation == "+":
            result = sum(a, b)
            print(f"Sum of {a} and {b} is {result}")
        elif operation == "-":
            result = subtract(a, b)
            print(f"Subtraction of {a} and {b} is {result}")
        elif operation == "*":
            result = multiply(a, b)
            print(f"Multiplication of {a} and {b} is {result}")
        elif operation == "/":
            if b != 0:
                result = divide(a, b)
                if result is not None:  # Update a only if division is successful
                    print(f"Division of {a} and {b} is {result}")
            else:
                print("Cannot divide by zero.")
                continue
        a = result
        choice = input("Press any key to continue with result? If not press x:\n").lower()
        if choice == 'x':
            exit()
        clear_screen()

calculator()
