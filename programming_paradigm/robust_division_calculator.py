# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle cases where input cannot be converted to float
        return "Error: Please enter numeric values only."
    
    except Exception as e:
        # Catch any other unexpected errors
        return f"Unexpected error: {e}"

# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        # Ensure the user provides exactly two arguments (numerator and denominator)
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get the numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function with the user inputs
    result = safe_divide(numerator, denominator)

    # Print the result (either the division result or an error message)
    print(result)

if __name__ == "__main__":
    main()

