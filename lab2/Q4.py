userstring = input(" Enter the string :")

spacelessstring = userstring.replace(" ", "")

count = {}

for x in spacelessstring:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1


duplicates = {key: value for (key, value) in count.items() if value >= 2}


print(duplicates)
