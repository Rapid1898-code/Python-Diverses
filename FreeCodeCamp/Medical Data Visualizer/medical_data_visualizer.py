import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

pd.set_option('display.max_columns',20)						# Show more information - count of the shown columns
pd.set_option('display.width', None)						# Show more information - None is using the maximum width of the IDE

# Import data
df = pd.read_csv("medical_excamination.csv",sep=",")

# Add 'overweight' column
#ow_list = []
#for idx,cont in df["weight"].items():
#    bpi = df["weight"][idx] / ((df["height"][idx]/100)**2)
#   if bpi > 25: ow_list.append(1)
#    else: ow_list.append(0)
#df["overweight"] = ow_list

#(df["cholesterol"] > 1)

print(df)

df ["overweight"]=[1 if (x / ((y/100)**2)) > 25 else 0 for x,y in zip(df["weight"], df["height"])]df["gluc"]=[1 if x > 1 else 0 for x in df["gluc"]]
df["cholesterol"]=[1 if x > 1 else 0 for x in df["cholesterol"]]
print(df)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'cholesterol', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
