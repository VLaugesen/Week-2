# %%
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.join("..", "Data", "DKHousingPricesSample100k.csv"))
print(df.head(10))

def plot_average_by_group(df, group, column):
    """
    Takes a pandas dataframe and prints/plots the avearge for a given column,
    sorted by a given group.
    """
    fig, ax = plt.subplots(figsize=(6, 3))

    goupby_region = df.groupby(group)
    groupby_region_mean = goupby_region[column].mean()
    print(groupby_region_mean)
    groupby_region_mean.plot(title="Average purchase price", ax=ax, kind="bar")

# %%
plot_average_by_group(df, "region", "purchase_price")
plot_average_by_group(df, "house_type", "purchase_price")


