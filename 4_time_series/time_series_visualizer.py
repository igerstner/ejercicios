import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import matplotlib
matplotlib.use('TkAgg')
import calendar

#register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df0= pd.read_csv(R'/data2/certi/4_time_series/fcc-forum-pageviews.csv')
df = df0.copy()

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace = True)

# Clean data
lower_percentile = df['value'].quantile(0.025)
upper_percentile = df['value'].quantile(0.975)
df = df[(df['value']>= lower_percentile) & (df['value']<= upper_percentile)]

def draw_line_plot():
    # Draw line plot
     fig, ax = plt.subplots(figsize=(8, 6))
     ax.plot(df.index, df['value'], label='Page Views', color='blue')

     ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
     ax.set_xlabel('Date')
     ax.set_ylabel('Page Views')

     plt.xticks(rotation=45)
     plt.tight_layout()

    # Save image and return fig (don't change this part)
     fig.savefig(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\line_plot.png')
     return fig

draw_line_plot()
plt.show()

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year  # Use the already formatted index
    df['month'] = df.index.month  # Use the already formatted index

    #agruop by year, month and calculate the average
    df_bar= df.groupby(['year', 'month'])['value'].mean().unstack()
    #crear la figura y el eje
    fig, ax = plt.subplots(figsize=(12, 8))

    df_bar.plot(kind='bar', ax = ax, width=0.8)
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])

    ax.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Monthly Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\bar_plot.png')
    return fig

# Draw bar plot
draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2)= plt.subplots(1,2,figsize=(18, 8))

    sns.boxplot(data =df_box, x="year", y= "value", ax = ax1,  palette="Set1")
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Average Page Views')
    ax1.set_title('Yearly Average Page Views')

    sns.boxplot(data=df_box, x="month", y="value", ax=ax2, palette="Set2")
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Average Page Views')
    ax2.set_title('Monthly Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()