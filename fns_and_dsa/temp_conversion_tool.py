FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """
  Converts a temperature in Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit (float).

  Returns:
      The temperature converted to Celsius (float).
  """
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """
  Converts a temperature in Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius (float).

  Returns:
      The temperature converted to Fahrenheit (float).
  """
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """
  The main function that interacts with the user and performs the conversion.
  """
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "°C"
        converted_unit_label = "°F"
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = "°F"
        converted_unit_label = "°C"
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      print(f"{temperature}{unit_label} is equivalent to {converted_temp:.2f}{converted_unit_label}")
      break
    except ValueError as e:
      print(f"Error: {e}. Please enter a valid numeric temperature.")

if __name__ == "__main__":
  main()
