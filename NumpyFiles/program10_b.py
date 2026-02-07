records = {
    "X": [1, -1, 2],
    "Y": [0, 0, 0],
    "Z": [-5, 3, 7],
    "W": []
}

results = {x:sum(x**2 for x in y if x>0) for x, y in records.items() if y and sum(x**2 for x in y if x>0) > 0}

for i in results:
    print(i, results[i])