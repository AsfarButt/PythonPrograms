words = {
    "fruits": ["apple", "kiwi", ""],
    "veggies": ["", "carrot", "pea"],
    "grains": []
}

results = {x: sum(len(x) for x in y if x) for x, y in words.items() if sum(len(x) for x in y if x)}

for i in results:
    print(i, results[i])