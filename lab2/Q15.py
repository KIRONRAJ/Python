import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&()|<>:.,[]{}"

combined = lower + upper + numbers + symbol
length = 10
password = "".join(random.sample(combined, length))
print("Auto generated Password is:", password)
