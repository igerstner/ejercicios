import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 1
df = pd.read_csv(R"/data2/certi/3_medical_data_visualizer/medical_examination.csv")

#Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
# 2
df['BMI'] =(df['weight']/ (df['height']/100)**2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3
def normalize(df, column):
    df[column].apply(lambda x:1 if x> 1 else 0)
    return df
df = normalize(df, 'cholesterol')
df = normalize(df, 'gluc')

# 4
def draw_cat_plot():
# 5
    columns = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=columns) #ver que columns que es una variable que arme aca va sin corchetes pero una columna va con.
    df_cat = df_cat.reset_index()\
                .groupby(['variable', 'cardio', 'value']) \
                .agg('count') \
                .rename(columns={'index': 'total'}) \
                .reset_index()

    # 6

    # 7

    # 8
    fig = sns.catplot( x = "variable", y = 'total', col = 'cardio', hue = 'value', data =df_cat, kind = 'bar').fig

    # 9
    fig.savefig(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\catplot.png')
    return fig

draw_cat_plot()

# 10
def draw_heat_map():
    # 11
    df_heat = ( (df['ap_lo'] <= df['ap_hi']) &
               (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(2.5/100)) &
               (df['weight'] <= df['weight'].quantile(0.975)) )

    # 12
    df_filtered = df[df_heat]
    corr = df_filtered.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(13, 10))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmin=-0.5, vmax=0.5)

    # Show the plot
    plt.show()

    # 16
    fig.savefig(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\heatmap.png')
    return fig
draw_heat_map()


# DESDE ACA YA SON RESPUESTAS
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    columns = [
      'active',
      'alco',
      'cholesterol',
      'gluc',
      'overweight',
      'smoke'
    ]
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=columns)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df_cat.reset_index() \
                .groupby(['variable', 'cardio', 'value']) \
                .agg('count') \
                .rename(columns={'index': 'total'}) \
                .reset_index()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        x="variable",
        y="total",
        col="cardio",
        hue="value",
        data=df_cat,
        kind="bar").fig

    # Do not modify the next two lines
    fig.savefig(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\catplot.png')
    return fig
draw_cat_plot()
