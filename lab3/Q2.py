txt = open("test.txt", "r")

lines = int( input("Enter the number of lines to be displayed : ") )

print(txt.readlines(lines))
