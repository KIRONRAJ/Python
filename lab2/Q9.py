usertuple = tuple(input("Enter the items to be stored inside a tuple : "))

to_find_index = input(" Enter the item to find its index number : ")


if to_find_index in usertuple:

    print(" The index of", to_find_index, "is", usertuple.index(to_find_index))
else:

    print(" The item", to_find_index, " is not found")

