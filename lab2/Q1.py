import random

# vowels

vowels = ["a", "e", "i", "o", "u"]

#using the charactors only once.

for x in vowels:
    random.shuffle(vowels)
    print("".join(vowels))
