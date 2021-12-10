random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
sum = 0
while x < len(random_list):
    sum = sum + random_list[x]
    x += 1


print("The Elements are : ", random_list, "\n", "The sum of elements:", sum)
