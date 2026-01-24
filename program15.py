import numpy as np
import pandas as pd

# Arr1 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

# print(Arr1['a'])

# data = {
#     "name":["ali","alex","sarah","elizabeth"],
#     "age":[12,18,32,22],
#     "ID":["SO_109","DO_229","SO_011","FOW_178"]
# }

# arr2 = pd.DataFrame(data)

# print(arr2)

arr3 = pd.read_excel("employes.xlsx",sheet_name="Sheet1")

print(arr3.head())