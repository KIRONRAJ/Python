from datetime import date, timedelta

current_date = date.today()

print("The Current Date :", current_date)


new_date = current_date - timedelta(days=5)

print("Five days before today is : ", new_date)
