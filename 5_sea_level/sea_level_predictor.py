import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

epa = pd.read_csv(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\epa-sea-level.csv')


def draw_plot():
    # Read data from file

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=epa['Year'], y=epa['CSIRO Adjusted Sea Level'], c="pink")

    plt.show()

    slope, intercept, r_value, p_value, std_err = linregress(epa['Year'], epa['CSIRO Adjusted Sea Level'])
    #(pendiente, intersección, valor r, valor p, error estándar)
    print("Slope (pendiente):", slope)
    print("Intercept (intersección):", intercept)
    print("R-value (coeficiente de correlación):", r_value)
    print("P-value (valor p):", p_value)
    print("Std err (error estándar):", std_err)

    # Create first line of best fit
    #x = epa['Year']
    #y = intercept + x* slope
    x_actual = np.arange(epa['Year'].min(), epa['Year'].max())
    ax.scatter(x=x_actual, y=intercept + x_actual*slope, c="blue")

    # Create second line of best fit
    x_nuevo = np.arange(2000, 2051)
    ax.scatter(x=x_nuevo, y = intercept + x_nuevo*slope, c="red")

    plt.show()

    # Add labels and title
    ax.legend()
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig(R'C:\Users\Usuario\PycharmProjects\PythonProject2\data2\certi\sea_level_plot.png')
    return plt.gca()

draw_plot()