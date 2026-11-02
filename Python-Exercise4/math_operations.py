def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

import math_operations as math_op

print("=== Welcome to the Custom Module Calculator ===")

while True:
  print("\nSelect an operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = input("Enter choice (1-5): ").strip()

  if choice == '5' :
      print("Exiting calculator. Goodbye!")
      break

  if choice in ['1', '2', '3', '4']:
        try:
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            continue

        if choice == '1':
            result = math_op.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = math_op.subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = math_op.multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = math_op.divide(num1, num2)
            print(f"Result: {result}")

        else:
            print("Invalid choice! Please select a vaild option from 1 to 5.")