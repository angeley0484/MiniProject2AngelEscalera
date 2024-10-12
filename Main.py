### INF601 - Advanced Programming in Python
### Angel Escalera
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import os
for dirname, _, filenames in os.walk('laptop_prices.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


import plotly.express as px

laptops = pd.read_csv("laptop_prices.csv", index_col=0)

laptops["Prices_euros"] = laptops["Price_euros"]
print(laptops.head())

#axs = laptops.plot.area(figsize=(12, 4), subplots=True)


df = pd.read_csv('laptop_prices.csv')
df.head()
df.info
df.describe()
df.isnull().info()

fig = px.scatter(df,x='Company',y='Price_euros',color='Company')
fig.show()
