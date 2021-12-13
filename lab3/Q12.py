my_list = ["this", "is", "a", "list"]

file = open("test2.txt", "w")

for x in my_list:
    file.write("%s\n" % x)

file.close()

newfile = open("test2.txt", "r")
print(newfile)
