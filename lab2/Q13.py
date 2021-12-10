user_list = list()
result_list = list()

size = int(input("Enter the size of the list :"))
print("Enter all elements of the list one by one :")
for i in range(size):
    user_list.append(int(input("Enter element to add : ")))

# <-- Sublist -->
for i in range(len(user_list) + 1):
    for j in range(i + 1, len(user_list) + 1):
        result_list.append(user_list[i:j])

# <-- Sublist -->

print(
    " The list you have entered : \n",
    user_list,
    "\nThe Sublist for the given list : ",
    result_list,
)
