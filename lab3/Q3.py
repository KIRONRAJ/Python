txt = open("test.txt", "a")
new_txt = input(" Enter the new content to be written to the existing text file : ")
txt.write(new_txt)
txt.close()

txt = open("test.txt", "r")
print(txt.read())
