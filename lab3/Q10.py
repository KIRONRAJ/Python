from typing import Counter

file = open("test.txt", "r")
count = Counter(file.read().split())

print("The Words counter", count)
