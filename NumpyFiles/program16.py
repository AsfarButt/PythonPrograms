import numpy as np
import pandas as pd

dataset = pd.read_csv("practicedataset1.csv")

print(dataset)
print(dataset.info())

missing_count = dataset.isna().sum().sort_values(ascending=False)
print(missing_count)

dataset["Age"] = dataset["Age"].fillna(dataset["Age"].median())
dataset["TotalCharges"] = dataset["TotalCharges"].fillna(dataset["TotalCharges"].median())

missing_count = dataset.isna().sum().sort_values(ascending=False)
print(missing_count)

dataset["Gender"] = dataset["Gender"].fillna(dataset["Gender"].mode()[0])

missing_count = dataset.isna().sum().sort_values(ascending=False)
print(missing_count)

duplicate_values = dataset.duplicated().sum()
print(duplicate_values)

print(dataset[dataset.duplicated(keep=False)])

dataset = dataset.drop_duplicates()
dataset = dataset.drop_duplicates(subset="CustomerID")

print(dataset[dataset.duplicated(keep=False)])

print(dataset.dtypes)

v_dataset = dataset["MonthlyCharges"].str.replace(".", "", 1)

print(v_dataset.str.isnumeric())
print(~v_dataset.str.isnumeric())

dataset["MonthlyCharges"] = pd.to_numeric(
    dataset["MonthlyCharges"],
    errors="coerce"
)

print(dataset["MonthlyCharges"].dtype)
print(dataset.dtypes)

print(dataset["MonthlyCharges"].isna().sum())

dataset["MonthlyCharges"] = dataset["MonthlyCharges"].fillna(
    dataset["MonthlyCharges"].median()
)

print(dataset["MonthlyCharges"].isna().sum())
print(dataset)
