
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

newdict = dict(dic1)
newdict.update(dic2)
newdict.update(dic3)

print(newdict)
