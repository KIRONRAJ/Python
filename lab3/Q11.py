import os

info = os.stat("test.txt")
size = info.st_size
print("The size of the file is :", size, "bytes")
