import pandas as pd
import numpy as np

dataset = pd.read_csv("practicedataset2.csv")

# dataset["OnTime"] = (dataset["Delivered"] == "Yes") & (dataset["DeliveryDays"] <= 4)
# on_time_per_city = dataset.groupby("City")["OnTime"].mean().mul(100)
# print(on_time_per_city.round(1))

# dataset["OrderDate"] = pd.to_datetime(dataset["OrderDate"])
# print(dataset["OrderDate"].dtype)
# dataset["OrderMonth"] = dataset["OrderDate"].dt.month
# # print(dataset[["OrderID","OrderMonth"]])
# # OrderDetails = pd.DataFrame()
# # OrderDetails["TotalAmount"] = dataset.groupby("OrderMonth")["OrderAmount"].sum()
# # print(OrderDetails)
# # OrderDetails["NoOfOrders"] = dataset.groupby("OrderMonth")["OrderID"].count()
# # print(OrderDetails)
# # OrderDetails["AvgOrderAmount"] = dataset.groupby("OrderMonth")["OrderAmount"].median()
# # print(OrderDetails)

# OrderDetails = (
#     dataset.groupby("OrderMonth").agg(
#         TotalAmount = ("OrderAmount","sum"),
#         NoOfOrders = ("OrderID","count"),
#         AvgOrderAmount = ("OrderAmount","median")
#     )
# )

# print(OrderDetails)
# print(OrderDetails.dtypes)


CustomerDetails = dataset.groupby(["City","Customer"])["OrderAmount"].sum()
print(CustomerDetails)


