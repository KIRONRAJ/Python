dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

userinput = int(input("Choose a number 1 - 6 to find the value stored against it : "))

if userinput in dict_num:
    print(dict_num[userinput])
else:
    print(" You have entered an invalid input , Please enter a number between 1-6")
