with open("file1.txt", "r") as fileone, open("file2.txt", "r") as filetwo:
    for x, y in zip(fileone, filetwo):
        x = x.strip()
        y = y.strip()
        print(x + y)
