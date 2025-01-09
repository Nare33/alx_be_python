import datetime

def display_current_datetime():
  """
  Prints the current date and time in YYYY-MM-DD HH:MM:SS format.
  """
  current_date = datetime.datetime.now()
  print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days):
  """
  Calculates the future date by adding a specified number of days to the current date.

  Args:
      days: The number of days to add (integer).

  Returns:
      A datetime object representing the future date.
  """
  current_date = datetime.datetime.now()
  future_date = current_date + datetime.timedelta(days=days)
  return future_date

def main():
  """
  The main function that calls the other functions and interacts with the user.
  """
  display_current_datetime()
  days = int(input("Enter the number of days to add to the current date: "))
  future_date = calculate_future_date(days)
  print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
  main()
