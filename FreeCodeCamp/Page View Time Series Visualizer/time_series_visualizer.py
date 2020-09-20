import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                sep=",",
                parse_dates=True,
                index_col=0)

# Clean data
df= df[(df['value'] >= df['value'].quantile (0.025))]
df= df[(df['value'] < df['value'].quantile (0.975))]
#print(df)

def draw_line_plot():
    # Draw line plot

    fig = plt.figure ()
    plt.plot (df.index, df.value)
    plt.title ('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel ('Date')
    plt.ylabel ('Page Views')
    plt.show ()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig




def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #df_bar = df.groupby(df.index.strftime('%Y %B'))['value'].sum()
    df_bar = df.groupby ([(df.index.strftime("%Y")), (df.index.strftime("%B"))]).sum ()
    print(df_bar)

    # Draw bar plot
    fig = plt.figure ()
    plt.bar(df.index, df.value)
    plt.title ('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel ('Years')
    plt.ylabel ('Average Page Views')
    plt.show ()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()
