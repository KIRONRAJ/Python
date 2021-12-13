file = open("test.txt", "r")

my_list = [x.rstrip() for x in file]

print(my_list)
