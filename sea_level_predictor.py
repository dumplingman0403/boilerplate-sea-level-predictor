import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y, c = '#1f77b4', s=5)

    # Create first line of best fit
    res1 = linregress(x, y)
    x_pred = pd.Series(i for i in range(1880, 2051))
    y_pred = res1.slope * x_pred + res1.intercept
    plt.plot(x_pred, y_pred, 'r')
    # Create second line of best fit
    df_new = df[df['Year'] >= 2000]
    x_new = df_new['Year']
    y_new = df_new['CSIRO Adjusted Sea Level']
    res2 = linregress(x_new, y_new)
    x_pred_new = pd.Series(i for i in range(2000, 2051))
    y_pred_new = res2.slope * x_pred_new + res2.intercept
    plt.plot(x_pred_new, y_pred_new, 'y')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()