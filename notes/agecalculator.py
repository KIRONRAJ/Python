def ageCalculator(y, m, d):
    import datetime

    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    print(age)


year = int(input("Enter the year : "))
month = int(input("Enter the Month : "))
day = int(input("Enter the Day : "))
ageCalculator(year, month, day)
