import datetime

def display_current_datetime():
  """
  Displays the current date and time in YYYY-MM-DD HH:MM:SS format.
  """
  current_date = datetime.datetime.now()
  print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(number_of_days):
  """
  Calculates the future date by adding the specified number of days to the current date.

  Args:
      number_of_days: The number of days to add to the current date (integer).

  Returns:
      The future date in YYYY-MM-DD format.
  """
  current_date = datetime.datetime.now()
  future_date = current_date + datetime.timedelta(days=number_of_days)
  print(f"Enter the number of days to add to the current date: {number_of_days}")
  print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date(10)
