data = {
    "A": [1, -2, 3, 0],
    "B": [-1, -2, -3],
    "C": [4, 0, -5, 6],
    "D": []
}

results = {x: sum(x**2 for x in y if x>0) for x, y in data.items() if sum(x**2 for x in y if x>0) != 0}

for i in results:
    print(i, results[i])
