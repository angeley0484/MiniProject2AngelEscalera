### INF601 - Advanced Programming in Python
### Angel Escalera
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

laptops = pd.read_csv("laptop_prices.csv", index_col=0)

laptops["Prices_euros"] = laptops["Price_euros"]
print(laptops.head())

axs = laptops.plot.area(figsize=(12, 4), subplots=True)



