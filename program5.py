data = [3, -1, 0, 4, -2, 5]
sorted_data = []

for data in data:
    if data > 0 and data % 2 == 0:
        sorted_data.append(data)
        
for i in sorted_data:
    print(i)
