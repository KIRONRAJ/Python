txt = open("test.txt", "r")

n = int(input("Enter the number of lines to be displayed : "))

lines = txt.readlines()

last_lines = lines[-n:]

print(last_lines)
