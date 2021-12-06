num = int(input("enter any number to find the divisors"))
div = []
i = 1
while i <= num:
    if (num % i) == 0:
        div.append(i)

    i = i + 1

print(div)
