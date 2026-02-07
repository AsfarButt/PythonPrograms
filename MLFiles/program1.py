from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# CHANGE this path if your CSV is elsewhere
dataset = pd.read_csv("practicedataset1.csv")

# Verify dataset loaded correctly
print(type(dataset))
print(dataset.head())
print(dataset.columns)

# Features and target
X = dataset[["years_experience", "education_level", "age", "weekly_hours", "projects_completed"]]
y = dataset["annual_salary"]

# Train model
MLModel = LinearRegression()
MLModel.fit(X, y)

# Predict for a new employee
newX = np.array([[3, 16, 33, 40, 8]])
newY = MLModel.predict(newX)

print(newY)


