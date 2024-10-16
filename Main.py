### INF601 - Advanced Programming in Python
### Angel Escalera
### Mini Project 2


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import warnings
warnings.filterwarnings("ignore")




for dirname, _, filenames in os.walk('laptop_prices.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('laptop_prices.csv')
df.columns
df.head()
df.shape
df.isna().sum().sum()
df.info()
df.duplicated().sum()

# Set the style and context of the plot
sns.set(style="whitegrid", context="talk")

# Define a custom color palette
custom_palette = [
    '#1f77b4',  # Blue
    '#ff7f0e',  # Orange
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#9467bd',  # Purple
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#7f7f7f',  # Grey
    '#bcbd22',  # Olive
    '#17becf',  # Cyan
    '#ffbb78',  # Light Orange
    '#ff9896',  # Light Red
    '#c5b0d5',  # Light Purple
    '#f7b6d2',  # Light Pink
]

# Define font and color variables
font_title = {'fontsize': 16, 'fontweight': 'bold', 'color': 'darkblue'}
font_labels = {'fontsize': 14, 'fontweight': 'semibold', 'color': 'black'}

# Count of products by Company
company_counts = df['Company'].value_counts()

# Plot the counts
plt.figure(figsize=(12, 6))
sns.barplot(x=company_counts.index, y=company_counts.values, hue=company_counts.index, palette=custom_palette)
plt.title('Number of Products by Company', **font_title)
plt.xlabel('Company', **font_labels)
plt.ylabel('Number of Products', **font_labels)
plt.xticks(rotation=45)
plt.grid()



# Count of products by OS
os_counts = df['OS'].value_counts()

# Plot the counts
plt.figure(figsize=(12, 6))
sns.barplot(x=os_counts.index, y=os_counts.values, hue=os_counts.index, palette=custom_palette)
plt.title('Number of Products by Operating System',**font_title)
plt.xlabel('Operating System',**font_labels)
plt.ylabel('Number of Products',**font_labels)
plt.xticks(rotation=45)
plt.grid()


# Count of products by TypeName
type_counts = df['TypeName'].value_counts()

# Plot the counts
plt.figure(figsize=(12, 6))
sns.barplot(x=type_counts.index, y=type_counts.values, hue=type_counts.index, palette=custom_palette)
plt.title('Number of Products by Type',**font_title)
plt.xlabel('Product Type',**font_labels)
plt.ylabel('Number of Products',**font_labels)
plt.xticks(rotation=45)
plt.grid()


# Value counts for Screen
screen_counts = df['Screen'].value_counts()

# Plot the counts
plt.figure(figsize=(12, 6))
sns.barplot(x=screen_counts.values, y=screen_counts.index, hue=screen_counts.values, palette=custom_palette)
plt.title('Number of Products by Screen',**font_title)
plt.xlabel('Number of Products',**font_labels)
plt.ylabel('Screen Type',**font_labels)
plt.grid()



# Value counts for Touchscreen
touchscreen_counts = df['Touchscreen'].value_counts()

# Plot the counts
plt.figure(figsize=(6, 4))
sns.barplot(x=touchscreen_counts.index, hue=touchscreen_counts.index, y=touchscreen_counts.values, palette=custom_palette)
plt.title('Number of Products with Touchscreen',**font_title)
plt.xlabel('Touchscreen',**font_labels)
plt.ylabel('Number of Products',**font_labels)
plt.grid()



# Value counts for IPSpanel
ips_counts = df['IPSpanel'].value_counts()

# Plot the counts
plt.figure(figsize=(6, 4))
sns.barplot(x=ips_counts.index, y=ips_counts.values, hue=ips_counts.index, palette=custom_palette)
plt.title('Number of Products with IPS Panel',**font_title)
plt.xlabel('IPS Panel',**font_labels)
plt.ylabel('Number of Products',**font_labels)
plt.grid()



# Value counts for CPU_company
cpu_company_counts = df['CPU_company'].value_counts()

# Plot the counts
plt.figure(figsize=(12, 6))
sns.barplot(x=cpu_company_counts.values, y=cpu_company_counts.index, hue=cpu_company_counts.index, palette=custom_palette)
plt.title('Number of Products by CPU Company', **font_title)
plt.xlabel('Number of Products',**font_labels)
plt.ylabel('CPU Company',**font_labels)
plt.grid()

#Graphs the data
plt.show()
plt.savefig(f"Charts/company_counts.png")


'''
#Used to explore Plotly.express
df.info()
df.describe()
df.duplicated().sum()
df.isnull().info()
list(df.columns)


#Graphs all the collected data
fig = px.scatter(df,x='Company',y='Price_euros',color='Company')
fig.show()

fig = px.histogram(df,x='Price_euros', title='Distribution of laptop prices')
fig.show()

fig = px.scatter(df,x='Weight', y='Price_euros')
fig.show()

fig = px.pie(df, names = 'TypeName', values = 'Price_euros',title='Types_Of_Laptop')
fig.show()'''

