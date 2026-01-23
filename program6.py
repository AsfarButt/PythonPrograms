words = ["apple","banana","cherry","data"]

dict1 = {}
for word in words:
    if not len(word) < 6:
        dict1[word] = len(word)
        
for i in dict1:
    print(i)