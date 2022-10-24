# Your code to create majestic plots goes in here!
import pandas as pd
import matplotlib.pyplot as plt


def make_boxplot(file_name, out_png):
    iris = pd.read_csv(file_name,  header=None)
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
    iris = pd.read_csv(file_name,  header=None)
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'iris_species']
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

def combine_plots(file_name, x_attribute, y_attribute):
    iris = pd.read_csv(file_name,  header=None)
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'iris_species']
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(15, 5)
    
    axes[0].boxplot(iris[iris.columns[0:4]], labels=iris.columns[0:4])
    axes[0].set_ylabel('cm')
    
    # for species in set(iris['iris_species']):
    #     iris_species_data = iris[iris['iris_species'] == species]
    #     axes[1].scatter(iris_species_data[x_attribute],
    #                     iris_species_data[y_attribute],
    #                     label=species)
    # axes[1].set_xlabel(x_attribute + ' (cm)')
    # axes[1].set_ylabel(y_attribute + ' (cm)')
    
    out_png = 'multi_panel_figure.png'
    plt.savefig(out_png)
    