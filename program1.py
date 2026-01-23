
def Func1(names):
    j = 0
    dict = {}
    for i in names:
        if j%2 == 0:
            dict[j] = names[j]
        j+=1
        
    for i in dict:
        print(i,": ",dict[i])

names = ["Ali","Sara","Ahmed","Zara"]
Func1(names)

