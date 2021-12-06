import random

num = random.randrange(1, 10)

guess = int(input("Guess and Enter a number between 1 and 10 :"))


if guess == num:
    print("Hurray!! The Guess is correct")
elif guess < num:
    print("The Guess is low", "Better luck next Time. The Number was", num)
elif guess > num:
    print("The Guess is high", "Better luck next Time. The Number was", num)
