def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations (add, subtract, multiply, divide).

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the operation, or a message if there is an error (e.g., division by zero).
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"

