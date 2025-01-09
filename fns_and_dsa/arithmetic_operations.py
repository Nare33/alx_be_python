def perform_operation(num1, num2, operation):
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1: The first number (float).
      num2: The second number (float).
      operation: The operation to perform (string, one of 'add', 'subtract', 'multiply', or 'divide').

  Returns:
      The result of the arithmetic operation (float), or a message for division by zero.
  """

  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operation"

# This part is for testing purposes only and will not be included in the final script
if __name__ == "__main__":
  print("Arithmetic Operations")
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

  result = perform_operation(num1, num2, operation)
  print(f"Result: {result}")

