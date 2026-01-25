import pandas as pd
import numpy as np

dataset = pd.read_csv("practicedataset2.csv")

dataset["OnTime"] = (dataset["Delivered"] == "Yes") & (dataset["DeliveryDays"] <= 4)
ontime_per_city =  dataset.groupby("City")["OnTime"].sum()
print(ontime_per_city)
