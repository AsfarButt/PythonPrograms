data = [(1, 2), (3, -1), (-2, 4), (0, 5)]
list1 = []

for data in data:
    list1.append(data[0]+data[1]) if data[0] > 0 and data[1] > 0 else 0
    
for i in list1:
    print(i)