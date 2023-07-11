import datetime

# Read the input
month, day, year = map(int, input().split())

# Create a datetime object for the given date
date = datetime.date(year, month, day)

# Get the day of the week (Monday=0, Sunday=6)
day_of_week = date.weekday()

# Define a list of weekdays
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

# Print the corresponding weekday
print(weekdays[day_of_week])
