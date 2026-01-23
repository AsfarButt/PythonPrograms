records = {
    "A": [10, -5, 3],
    "B": [-2, -1],
    "C": [4, 5, -6],
    "D": []
}

results = {x: sum(p for p in y if p>0) for x, y in records.items() if y and sum(x for x in y if x>0) > 0}

for i in results:
    print(i, results[i])