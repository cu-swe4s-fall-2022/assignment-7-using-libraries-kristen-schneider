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
        good_data_file = 'iris.data'
        good_attribute1 = 'petal_width'
        good_attribute2 = 'petal_length'

        bad_data_file = 'bad_iris.data'
        bad_attribute = 'bad_attribute'
        out_png = 'petal_width_v_petal_length.png'
        
        # raises exceptions
        self.assertRaises(Exception, plotter.make_scatterplot,
                          bad_data_file,
                          good_attribute1,
                          good_attribute2)
        self.assertRaises(Exception, plotter.make_scatterplot,
                          good_data_file,
                          bad_attribute,
                          good_attribute1)
        self.assertRaises(Exception, plotter.make_scatterplot,
                          good_data_file,
                          good_attribute1,
                          bad_attribute)
    
    def test_combine_plots(self):
        good_data_file = 'iris.data'
        good_attribute1 = 'petal_width'
        good_attribute2 = 'petal_length'

        bad_data_file = 'bad_iris.data'
        bad_attribute = 'bad_attribute'
        out_png = 'petal_width_v_petal_length.png'
        
        # raises exceptions
        self.assertRaises(Exception, plotter.combine_plots,
                          bad_data_file,
                          good_attribute1,
                          good_attribute2)
        self.assertRaises(Exception, plotter.combine_plots,
                          good_data_file,
                          bad_attribute,
                          good_attribute1)
        self.assertRaises(Exception, plotter.combine_plots,
                          good_data_file,
                          good_attribute1,
                          bad_attribute)
        
if __name__ == '__main__':
    unittest.main()
    