import numpy as np
import pandas as pd

import pandas as pd

df_jan = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "City": ["NY", "LA", "NY", "Chicago", "LA"],
    "Quantity": [1, 2, 1, 1, 3],
    "Sales": [1200, 50, 80, 300, 150]
})

df_feb = pd.DataFrame({
    "OrderID": [201, 202, 203, 204, 205, 206],
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Laptop", "Headphones"],
    "City": ["NY", "NY", "LA", "Chicago", "LA", "NY"],
    "Quantity": [1, 1, 2, 1, 1, 2],
    "Sales": [1150, 25, 600, 90, 1180, 100]
})

df_sales = pd.concat(
    [df_jan, df_feb],
    axis=0
)

print(df_sales)

# combine_col = pd.concat(
#     [user_info, user_scores],
#     axis=1
# )

# new_df = pd.merge(
#     orders_df,
#     customers_df,
#     lef_ont="CustomerID",
#     right_index=True
#     how="left"
# )

# new_df = pd.merge(
#     visits_df,
#     ads_df,
#     left_index=True,
#     right_index=True,
#     how="inner"
# )

# new_df = pd.merge(
#     sales_df,
#     catalog_df,
#     left_on="ProductID",
#     right_index=True,
#     how="left"
# )