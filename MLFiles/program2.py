import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

dataset1 = pd.read_csv("W:\Work\Python-Files\MLFiles\practicedataset1.csv")
dataset2 = pd.read_csv("W:\Work\Python-Files\MLFiles\practicedataset2.csv")
dataset3 = pd.read_csv("W:\Work\Python-Files\MLFiles\practicedataset3.csv")

dataset = pd.concat([dataset1, dataset2, dataset3], axis=0)

X = dataset[["years_experience", "education_level", "age", "weekly_hours", "projects_completed"]]

Y = dataset[["annual_salary"]]

MLModel = LinearRegression()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

