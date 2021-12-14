import random

file = open("test.txt", "r")

line = file.readlines()

print(random.choice(line))
