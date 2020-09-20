import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

pd.set_option('display.max_columns',20)						# Show more information - count of the shown columns
pd.set_option('display.width', None)						# Show more information - None is using the maximum width of the IDE

# Import data
df = pd.read_csv("medical_excamination.csv",sep=",")

df ["overweight"]=[1 if (x / ((y/100)**2)) > 25 else 0 for x,y in zip(df["weight"], df["height"])]
df["gluc"]=[1 if x > 1 else 0 for x in df["gluc"]]
df["cholesterol"]=[1 if x > 1 else 0 for x in df["cholesterol"]]

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'cholesterol', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.loc[:,["cholesterol","gluc","smoke","alco","active","overweight","cardio"]]
    cols = list(df_cat.columns)
    cols.sort()

    #print(cols)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    grp = df_cat.groupby("cardio")
    df_grp1 = grp.get_group(0)
    df_grp2 = grp.get_group(1)
    data = []

    for i in cols:
        if i == "cardio": continue
        tmp1 = df_grp1[i].value_counts()
        tmp2 = df_grp2[i].value_counts()
        data.append ([0, i, 0, tmp1[0]])
        data.append ([0, i, 1, tmp1[1]])
        data.append ([1, i, 0, tmp2[0]])
        data.append ([1, i, 1, tmp2[1]])
    df_cat = pd.DataFrame(data,columns=["cardio","variable","value","total"])

    # Draw the catplot with 'sns.catplot()'
    fig=sns.catplot (x="variable", y="total", col="cardio", hue="value", kind="bar", data=df_cat)
    plt.show()

    # Do not modify the next two lines
    fig.savefig('catplot.png')

    return fig


# Draw Heat Map
def draw_heat_map():
    print(df.shape)
    # Clean the data
    df_heat = df[df["ap_lo"] <= df["ap_hi"]]
    print(df_heat.shape)
    df_heat = df[(df['height'] >= df['height'].quantile(0.025))]
    print(df_heat.shape)
    df_heat = df[(df['height'] < df['height'].quantile(0.975))]
    print(df_heat.shape)
    df_heat = df[(df['weight'] >= df['weight'].quantile(0.025))]
    print(df_heat.shape)
    df_heat = df[(df['weight'] < df['weight'].quantile(0.975))]
    print(df_heat.shape)





    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = f, ax = plt.subplots(figsize=(11, 9))

    cmap = sns.diverging_palette (230, 20, as_cmap=True)

    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

    # Do not modify the next two lines
    fig.figure.savefig('heatmap.png')
    return fig

fig = draw_cat_plot()
draw_heat_map()


