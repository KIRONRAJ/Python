userstring = input("Enter the String :")

count = {}

for x in userstring:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

print("The string", userstring, "have the following characters : \n", str(count))
