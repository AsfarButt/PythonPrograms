matrix = [
    [0, 2, -1],
    [3, 0],
    [-2, 4, 5]
]

results = {(x,y): matrix[x][y] for x in range(len(matrix)) for y in range(len(matrix[x])) if matrix[x][y] != 0}

for i in results:
    print(i, results[i])
 