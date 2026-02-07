import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

dataset1 = pd.read_csv("practicedataset1.csv")
dataset2 = pd.read_csv("practicedataset2.csv")
dataset3 = pd.read_csv("practicedataset3.csv")

dataset = pd.concat([dataset1, dataset2, dataset3], axis=0)

print(dataset)