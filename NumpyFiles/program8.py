nums = [1,2,2,3,4,4,5]

dict1 = {x: ("even" if x % 2 == 0 else "odd") for x in set(nums)}

    
for i in dict1:
    print(i,dict1[i])
    
        