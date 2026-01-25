# import numpy as np
# import pandas as pd

# Arr1 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

# print(Arr1['a'])

# data = {
#     "name":["ali","alex","sarah","elizabeth"],
#     "age":[12,18,32,22],
#     "ID":["SO_109","DO_229","SO_011","FOW_178"]
# }

# arr2 = pd.DataFrame(data)

# print(arr2)

# arr3 = pd.read_excel("employes.xlsx",sheet_name="Sheet1")

# print(arr3)

# arr4 = pd.read_csv("employes.csv")

# # print(arr4)
# import numpy as np
# import pandas as pd
# arr3 = pd.read_excel("employes.xlsx",sheet_name="Sheet1")

# # print(arr3.columns)
# # print(arr3.shape)
# # print(arr3.info())
# # print(arr3.describe())

# print(arr3[["TotalCharges","PaymentMethod"]][arr3["TotalCharges"] > 1500])


import numpy as np
import pandas as pd 

dataset = pd.read_csv("practicedataset1.csv")
print(dataset)

print(dataset.info())

missing_count = dataset.isna().sum().sort_values(ascending=False) #counting missing values

print(missing_count)  

dataset["Age"] = dataset["Age"].fillna(dataset["Age"].median())
dataset["TotalCharges"] = dataset["TotalCharges"].fillna(dataset["TotalCharges"].median())  # (int type)

missing_count = dataset.isna().sum().sort_values(ascending=False) #counting missing values

print(missing_count)  

dataset["Gender"] = dataset["Gender"].fillna(dataset["Gender"].mode()[0])  # (str type)

missing_count = dataset.isna().sum().sort_values(ascending=False) #counting missing values

print(missing_count)  
# dataset = dataset.fillna(dataset.median())

duplicate_values = dataset.duplicated().sum() # this checks row wise

print(duplicate_values)  # no of duplicates

print(dataset[dataset.duplicated(keep=False)]) #duplicate arrays

dataset = dataset.drop_duplicates()
# or
dataset = dataset.drop_duplicates(subset="CustomerID")

print(dataset[dataset.duplicated(keep=False)])

print(dataset.dtypes)