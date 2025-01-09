# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Converts a temperature in Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Converts a temperature in Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to interact with the user
def main():
    print("Welcome to the Temperature Conversion Tool!")
    
    # Prompt the user to enter a temperature and unit
    try:
        temperature = input("Enter the temperature followed by the unit (e.g., 32F or 0C): ").strip()
        
        if temperature[-1].upper() == 'F':
            # Convert Fahrenheit to Celsius
            fahrenheit = float(temperature[:-1])  # Extract the number part
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        
        elif temperature[-1].upper() == 'C':
            # Convert Celsius to Fahrenheit
            celsius = float(temperature[:-1])  # Extract the number part
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
        else:
            print("Invalid input. Please enter the temperature followed by 'C' or 'F'.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

