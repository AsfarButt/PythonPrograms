sensor_ids = ["A1", "B2", "C3", "D4"]
readings   = [20.5, None, 19.8, None]

result_dict = {}

for (index, value) ,name in zip(enumerate(readings),sensor_ids):
    if not value == None:
        result_dict[name] = value
    
    elif value == None:
        a = index
        b = index
        while a >= 0 and readings[a] is None:
            a -= 1
        while b < len(readings) and readings[b] is None:
            b += 1
        if b >= len(readings):
            b = a
        elif a < 0:
            a = b          
        result_dict[name] = (readings[a]+readings[b])/2
        
for i in result_dict:
    print(i, result_dict[i])