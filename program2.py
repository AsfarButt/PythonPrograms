users = ["u1","u2","u3"]
scores = [85, 42, 90]

highscores = []

for i, j in zip(users, scores):
    if j >= 80:
        highscores.append(i)
    
for i in highscores:
    print(i)