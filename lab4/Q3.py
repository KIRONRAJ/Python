from datetime import datetime

unix_timesamp = int(input("Enter the Unix timestamp: "))  # example: 1639679400

current_date_time = datetime.fromtimestamp(unix_timesamp).strftime(
    "%m/%d/%Y, %I:%M:%S %p"
)
print("The Current Date and time is :", current_date_time)
