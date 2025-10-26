import calendar
from datetime import datetime
valid_months = list(calendar.month_name)[1:]

date = int(input("Enter your date of birth: "))

if date > 31 or date < 1:
    print("Invalid date. ")
    exit()
else:
    year = int(input("Enter your year of birth: "))

if year > 2025 or year < 1900:
    print("Invalid year. ")
    exit()
else:
    month_name = input("Enter your month of birth: ").capitalize()
try:
    month_number = datetime.strptime(month_name, "%B").month  # full name
except ValueError:
    try:
        month_number = datetime.strptime(month_name, "%b").month  # short name
    except ValueError:
        print("Invalid month name.")
        exit()
else:
    print(date, ":", month_number, ":", year, sep='')

    print(month_number, ":", date, ":", year, sep='')

    print(year, ":", month_number, ":", date, sep='')