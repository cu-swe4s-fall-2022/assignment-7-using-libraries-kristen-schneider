import data_processor as dp
import os
import random
import unittest

class TestDataProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.class_test_file_name = 'good.data'
        rows = 5
        cols = 10
        f = open(cls.class_test_file_name, 'w')
        
        for r in range(rows):
            for c in range(cols):
                rand_int = random.randint(1, 100)
                f.write(str(rand_int) + ',')
            f.write('\n')
        f.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.class_test_file_name)
    
    def test_get_random_matrix(self):
        # set values
        set_rows = 4
        set_cols = 8
        set_random_matrix = dp.get_random_matrix(set_rows, set_cols)
        self.assertEqual(len(set_random_matrix), set_rows)
        self.assertEqual(len(set_random_matrix[0]), set_cols)
        
        # random values
        rand_rows = random.randint(1,100)
        rand_cols = random.randint(1,100)
        rand_random_matrix = dp.get_random_matrix(rand_rows, rand_cols)
        self.assertEqual(len(rand_random_matrix), rand_rows)
        self.assertEqual(len(rand_random_matrix[0]), rand_cols)
        
        # negative assertions
        self.assertNotEqual(len(set_random_matrix), 0)
        self.assertNotEqual(len(set_random_matrix[0]), 0)
        self.assertNotEqual(len(rand_random_matrix), 0)
        self.assertNotEqual(len(rand_random_matrix[0]), 0)
 
        # raise errors
        self.assertRaises(Exception, dp.get_random_matrix, 0, 1)
        self.assertRaises(Exception, dp.get_random_matrix, 1, 0)
        self.assertRaises(Exception, dp.get_random_matrix, -1, 1)
        self.assertRaises(Exception, dp.get_random_matrix, 1, -1)
    
    def test_get_file_dimensionss(self):
        # 3 input files
        # good data
        iris_data = 'iris.data'
        # good data setup/teardown
        good_data = self.class_test_file_name
        # bad data
        bad_data = 'bad.data'
        
        
        iris_dimensions = dp.get_file_dimensions(iris_data)  
        # positive assertions on iris data
        self.assertEqual(iris_dimensions[0], 150)
        self.assertEqual(iris_dimensions[1], 5)
        # negative assertions on iris data
        self.assertNotEqual(iris_dimensions[0], 0)
        self.assertNotEqual(iris_dimensions[1], 0)
        
        good_dimensions = dp.get_file_dimensions(good_data)  
        # positive assertions on setup data
        self.assertEqual(good_dimensions[0], 5)
        self.assertEqual(good_dimensions[1], 10)
        # negative assertions on setup data
        self.assertNotEqual(good_dimensions[0], 0)
        self.assertNotEqual(good_dimensions[1], 0)
        
        # raise errors for bad data
        self.assertRaises(Exception, dp.get_file_dimensions, bad_data)
        
    def test_write_matrix_to_file(self):
        # raise errors for bad input
        self.assertRaises(Exception, dp.write_matrix_to_file, 0, 0, 'out.txt')
   
     


if __name__ == '__main__':
    unittest.main()