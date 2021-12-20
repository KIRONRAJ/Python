user_list = []
total = 0
size = int(input("Enter the size of the List :"))
print("Enter all elements of the set one by one :")
for i in range(size):
    user_list.append(int(input("Enter integer elements to add : ")))

print(" Your set is :", user_list)

for x in user_list:
    total = total + x

print(" The Sum of the elements in your list is :", total)
