usertuple = tuple(input("enter the items to be stored inside a tuple : "))

if len(usertuple) > 4:

    print(
        "The elements in your tuple :",
        usertuple,
        "\n",
        "The forth element in your tuple is : ",
        usertuple[4],
        "\n",
        "The forth element from the last is :",
        usertuple[-4],
    )

else:
    print("Please enter at least 4 elements")
