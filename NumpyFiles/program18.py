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


# CustomerDetails = dataset.groupby(["City","Customer"])["OrderAmount"].sum()
# idx = CustomerDetails.groupby(level=0).idxmax()
# TopCustomer = CustomerDetails.loc[idx]
# print(TopCustomer)

# CustomerDetails = dataset.groupby(["City","Customer"])["OrderAmount"].sum().reset_index()
# print(CustomerDetails)
# TopCustomer = CustomerDetails.groupby(["City"])["OrderAmount"].max()

# # print(TopCustomer)

# TopCity = dataset.groupby("City")["OrderID"].count().idxmax()
# AggregatedArray = dataset.groupby("City").agg(
#     AvgDeliveryTime = ("DeliveryDays","mean"),
#     MaxOrderAmnt = ("OrderAmount","max"),
#     NoOfOrders = ("OrderID","count")
# )
# AggregatedRow = AggregatedArray.loc[[TopCity]]
# print(AggregatedRow)

# NewDF = dataset.groupby("City")["OrderID"].count().reset_index()
# print(NewDF)

# NewDF = dataset.groupby("City")["OrderID"].transform("count").reset_index()
# print(NewDF)

# NewPivotTable = pd.pivot_table(
#     dataset,
#     index="City",
#     columns="Customer",
#     values="OrderID",
#     aggfunc="count",
#     fill_value = "NA"
# )

# print(NewPivotTable)

# NewPivotTable = pd.pivot_table(
#     dataset,
#     index="City",
#     columns="Customer", # i used customer because my dataset only have orderID and its unique for all,
#     values="OrderAmount",
#     aggfunc="sum",
#     fill_value=0
# )
# print(NewPivotTable)

# Sales = dataset.groupby(["City","OrderMonth"])["OrderAmount"].sum().reset_index()
# print(Sales)