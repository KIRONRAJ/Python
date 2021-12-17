from datetime import datetime

# Current date and time

current_date_time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")
print("The Current Date and time is :", current_date_time)

# b) Current year

current_year = datetime.today().strftime("%Y")

print("The Current year is :", current_year)

# c) Month of year

current_month = datetime.today().strftime("%B")

print("The current month is : ", current_month)


# d) Week number of the year

current_week = datetime.today().strftime("%W")

print("The current Week number of the year is : ", current_week)

# e) Weekday of the week

current_weekday = datetime.today().strftime("%w")

print("The current Weekday of the week is : ", current_weekday)

# f) Day of year

current_day_of_year = datetime.today().strftime("%j")

print("The current Day of year is : ", current_day_of_year)

# g) Day of the month

current_day_of_month = datetime.today().strftime("%d")

print("The current Day of the month is : ", current_day_of_month)

# h) Day of week

current_day_of_week = datetime.today().strftime("%A")

print("The current Day of week is : ", current_day_of_week)
