import pandas as pd
import numpy as np

dataset = pd.read_csv("practicedataset2.csv")

print(dataset.head())
print(dataset.shape)
print(dataset.info())

# Finding missing values

missing_values = dataset.isna().sum().sort_values(ascending=False)
print(missing_values)

print(dataset["DeliveryDays"].dtype)  # first we fill ites missing values
print(dataset["OrderAmount"].dtype)  # this is string so we first make it float or numeric before filling missing values

dataset["DeliveryDays"] = dataset["DeliveryDays"].fillna(dataset["DeliveryDays"].median())
# dataset["OrderAmount"] = dataset["OrderAmount"].fillna(dataset["OrderAmount"].median())

missing_values = dataset.isna().sum().sort_values(ascending=False)   # numeric missing is all set
print(missing_values)

int_col = dataset["OrderAmount"].str.replace(".","",1)
print(int_col[~int_col.str.isnumeric()])

dataset["OrderAmount"] = pd.to_numeric(dataset["OrderAmount"],errors="coerce")

# int_col = dataset["OrderAmount"].str.replace(".","",1)
# print(int_col[~int_col.str.isnumeric()])

print(dataset["OrderAmount"].dtype)

duplicate_entries = dataset[dataset.duplicated(keep=False)]

print(duplicate_entries)

dataset = dataset.drop_duplicates(keep="first")

duplicate_entries_count = dataset.duplicated(keep=False).sum()

print(duplicate_entries_count) # no duplicates

print(dataset[["OrderID","City"]])  # city col not organized
print(dataset["City"].dtype)
# empty_space_checker = dataset["City"].str.startswith(" ").sum()
# print(empty_space_checker)
dataset["City"] = dataset["City"].str.strip().str.title()
print(dataset[["OrderID","City"]])

print(dataset["OrderDate"])
dataset["OrderDate"] = pd.to_datetime(dataset["OrderDate"])  # type changing  this is date and time but its type was str
print(dataset["OrderDate"].dtype)

dataset["OrderMonth"] = dataset["OrderDate"].dt.month
print(dataset["OrderMonth"].head())

filtered_data = dataset[(dataset["OrderAmount"]>100) & (dataset["Delivered"] == "Yes")]
print(filtered_data)

# groupby (new feature)
avg_orderamount = dataset.groupby("City")["OrderAmount"].mean()
avg_deliverydays = dataset.groupby("City")["DeliveryDays"].mean()

print(avg_orderamount)
print(avg_deliverydays)



