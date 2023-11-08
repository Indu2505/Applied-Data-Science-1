#importing the required libraries for visualization.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset into the environment.
unemployed_dataset = pd.read_csv("df_sex_unemployment_rates.csv")

# Convert date column to datetime using pandas library.
unemployed_dataset['date'] = pd.to_datetime(unemployed_dataset['date'])

# Plot: Line plot.
def line_plot_function(data, x_name='X axis', y_name='Y axis',title ='X vs Y'):
    '''
    This function is used to plot the line plot for the give arrays of data.

    Parameters
    ----------
    Data : data frame
        Data frame which has time series data
    x_name: String
        The x axis name must be provided
    y_name: String
        The y axis name must be provided.
    Title : String
        Title for the plot.

    '''
    plt.figure(figsize=(15,8))
    plt.plot(data['date'], data['overall_rate'], label='Overall Unemployment Rate',c='red')
    plt.plot(data['date'],data['men_rate'], label='Mens Unemployment Rate',c='blue')
    plt.plot(data['date'], data['women_rate'], label='Womens Unemployment Overall  Rate',c='orange')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

line_plot_function(unemployed_dataset,x_name='Years',y_name='Unemployment(%)', title=' US Unemployment rate over time')

def scatter_plot_function(data,x_name='X axis', y_name='Y axis',title ='X vs Y'):
    '''
    This function is used to plot the scatter plot for the given array of data.

    Parameters
    ----------
    Data : data frame
        Data frame which 2 continous values.
    x_name: String
        The x axis name must be provided
    y_name: String
        The y axis name must be provided.
    Title : String
        Title for the plot.

    '''
    plt.scatter(data['men_rate'],data['women_rate'],label='data points')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.title(title)
    plt.show()
scatter_plot_function(unemployed_dataset,x_name='Mens Unemployment rate', y_name='Women Unemployment rate',title='Scatter of Men and women unemployment rate.')

# create a data for date between 2012 to 2022 for past decade dataset.
unemployed_dataset['Year'] = unemployed_dataset['date'].dt.year
unemployed_dataset_decade = unemployed_dataset[(unemployed_dataset['Year'] <= 2022) & (unemployed_dataset['Year']>=2012)]

def box_plot_function(data,x_name='X axis', y_name='Y axis',title ='X vs Y'):
    '''
    

    Parameters
    ----------
    This function is used to plot the box plot for the given array of data.

    Parameters
    ----------
    Data : data frame
        Data frame which 2 continous values.
    x_name: String
        The x axis name must be provided
    y_name: String
        The y axis name must be provided.
    Title : String
        Title for the plot.

    '''
    plt.boxplot(data[['women_16_19_rate','women_20_24_rate','women_25_34_rate']])
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.xticks([1,2,3],['16-19 years','20-24 years','25-35 years'],rotation=45)
    plt.title(title)
    plt.show()

box_plot_function(unemployed_dataset_decade,x_name='Age group',y_name='Unemployment rate',title = 'Different age group Women unemployment rate in past decade')