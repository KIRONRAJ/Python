file_one = open("fileone.txt", "r")

file_two = open("filetwo.txt", "a")

for x in file_one:
    file_two.write(x)
    print(" File copied successfully")
