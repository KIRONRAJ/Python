file = open("test.txt", "r")

words = file.read().split()

maxlen = len(max(words, key=len))

res = [word for word in words if len(word) == maxlen]

print(res)
