user_set = set()


size = int(input("Enter the size of the Set :"))
print("Enter all elements of the set one by one :")
for i in range(size):
    user_set.add(input("Enter element to add : "))

print(" Your set is :", user_set)

to_remove = input("\n Enter the element you want to remove :")

if to_remove in user_set:
    user_set.remove(to_remove)
    print("The updated set :", user_set)

else:
    print("\n The element you have mentioned cannot be found. Please check\n")
    print(user_set)
