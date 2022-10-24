# Your code to create majestic plots goes in here!
import pandas as pd
import matplotlib.pyplot as plt
import sys


def make_boxplot(file_name, out_png):
    '''
    Saves a boxplot for input data file.
    Input:
        file_name: input data file
        out_png: output png file name
    Output:
        saves file 'out_png'
    '''
    try:
        iris = pd.read_csv(file_name,  header=None)
    except FileNotFoundError:
        raise FileNotFoundError(file_name + ' not found.')
        sys.exit(1)
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'iris_species']
    
    x_labels = iris.columns
    bp = plt.boxplot(iris[iris.columns[0:4]], labels=iris.columns[0:4])
    plt.ylabel('cm')
    plt.savefig(out_png)

def make_scatterplot(file_name, x_attribute, y_attribute):
    '''
    Saves a scatter plot for input data file.
    Input:
        file_name: input data file
        x_attribute: attribute to be plotted on x-axis
            of scatter plot
        y_attribute: attribute to be plotted on y-axis
            of scatter plot    
    Output:
        saves file 'x_attribute_v_y_attribute.png'
    '''
    try:
        iris = pd.read_csv(file_name,  header=None)
    except FileNotFoundError:
        raise FileNotFoundError(file_name + ' not found.')
        sys.exit(1)
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'iris_species']
    try:
        for species in set(iris['iris_species']):
            iris_species_data = iris[iris['iris_species'] == species]
            sp = plt.scatter(iris_species_data[x_attribute],
                            iris_species_data[y_attribute],
                            label=species)
        out_png = x_attribute + '_v_' + y_attribute + '.png'
        plt.legend()
        plt.xlabel(x_attribute + ' (cm)')
        plt.ylabel(y_attribute + ' (cm)')
        plt.savefig(out_png)
    except KeyError:
        raise KeyError('One of the input attributes does not exist')

def combine_plots(file_name, x_attribute, y_attribute):
    '''
    Saves a figure where left figure is boxplot
    and right figure is scatter plot.
    Input:
        file_name: input data file
        x_attribute: attribute to be plotted on x-axis
            of scatter plot
        y_attribute: attribute to be plotted on y-axis
            of scatter plot    
    Output:
        saves file 'multi_panel_figure.png'
    '''
    try:
        iris = pd.read_csv(file_name,  header=None)
    except FileNotFoundError:
        raise FileNotFoundError(file_name + ' not found.')
        sys.exit(1)
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'iris_species']
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(15, 5)
    
    axes[0].boxplot(iris[iris.columns[0:4]], labels=iris.columns[0:4])
    axes[0].set_ylabel('cm')
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)

    try:
        for species in set(iris['iris_species']):
            iris_species_data = iris[iris['iris_species'] == species]
            axes[1].scatter(iris_species_data[x_attribute],
                            iris_species_data[y_attribute],
                            label=species)

        axes[1].set_xlabel(x_attribute + ' (cm)')
        axes[1].set_ylabel(y_attribute + ' (cm)')
        axes[1].spines['top'].set_visible(False)
        axes[1].spines['right'].set_visible(False)
    except KeyError:
        raise KeyError('One of the input attributes does not exist')
    
    out_png = 'multi_panel_figure.png'
    plt.savefig(out_png)
    