file = open("test.txt", "r")

count = 0

line = file.read().split("\n")

for i in line:
    if i:
        count += 1

print(count)
