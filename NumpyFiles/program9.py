data = [3, -2, 4, -1, 0, 5, -6]

dict1 = {x: y**2 for x, y in enumerate(data) if y>0}

for i in dict1:
    print(i, dict1[i])