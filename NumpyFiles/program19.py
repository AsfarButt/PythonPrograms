import numpy as np
import pandas as pd

dataset = pd.read_csv("practicedataset3.csv")

# print(dataset.head())

# new_dataset = pd.melt(
#     dataset,
#     id_vars=["OrderID", "City", "Customer", "Product"],
#     value_vars=["Jan", "Feb", "Mar"],
#     value_name="Revenue",
#     var_name="Month"
# )

# print(new_dataset)


dataset["RevenuePerOrder"] = dataset["Jan"]+dataset["Feb"]+dataset["Mar"]   # dont know how to do for 3 cols.. cause then i would have to make 3 revenues (and if it can be done using complex lambda functions will do that later.. not in the scope of current stage)
print(dataset["RevenuePerOrder"])
dataset["TotalRevenue"] = dataset.groupby("City")["RevenuePerOrder"].transform("sum")

print(dataset[["TotalRevenue","OrderID"]])
# print(dataset)

pivot_table = pd.pivot_table(
    dataset,
    index="City",
    columns="Product",
    values="RevenuePerOrder",
    fill_value=0,
    aggfunc="sum"
)

print(pivot_table)

print(pivot_table)

new_dataset = pd.melt(
    dataset,
    id_vars=["OrderID","City","Customer","Product"],
    value_vars=["Jan","Feb","Mar"],
    var_name="Month",
    value_name="Revenue"
)

print(new_dataset)