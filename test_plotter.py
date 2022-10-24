import plotter
import os
import random
import unittest

class TestPlotter(unittest.TestCase):
    
    def test_boxplot(self):
        bad_data_file = 'bad_iris.data'
        out_png = 'iris_boxplot.png'
        # raises exception
        self.assertRaises(Exception, plotter.make_boxplot, bad_data_file, out_png)
    
    def test_scatterplot(self):
        bad_data_file = 'bad_iris.data'
        out_png = 'iris_boxplot.png'
        # raises exception
        self.assertRaises(Exception, plotter.make_boxplot, bad_data_file, out_png)
    
    def test_combine_plots(self):
        bad_data_file = 'bad_iris.data'
        out_png = 'iris_boxplot.png'
        # raises exception
        self.assertRaises(Exception, plotter.make_boxplot, bad_data_file, out_png)
        
if __name__ == '__main__':
    unittest.main()
    