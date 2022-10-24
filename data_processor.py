# remember to import your libraries!
import numpy as np
import os
import sys

def get_random_matrix(num_rows, num_columns):
    '''
    Returns NxM matrix of random floating
    point numbers sampled from uniform in 
    range (0,1].
    Input:
        num_rows: integer value, number of rows
        num_columns: integer value, number of colums
    Output:
        random_matrix: NxM matrix of random floating
            point numbers sampled from uniform in 
            range (0,1].
    '''
    random_matrix = None
    if num_rows == 0 and num_columns > 0:
        raise Exception('Cannot have number of rows = 0 and number of columns > 0')
        sys.exit(1)
    elif num_rows > 0 and num_columns == 0:
        raise Exception('Cannot have number of rows > 0 and number of columns = 0')
        sys.exit(1)
    elif num_rows < 0 or num_columns < 0:
        raise Exception('Cannot have number of rows or number of columns < 0')
        sys.exit(1)
    else:
        random_matrix = np.random.rand(num_rows, num_columns)
    return random_matrix

def get_file_dimensions(file_name):
    '''
    Returns a tuple of the dimensions of a file
    Input:
        file_name: name of file to open
    Output:
        file_dimensions: a tuple of the dimensions
            of the input file
    '''
    num_rows = 0
    num_cols = 0
    f = open(file_name, 'r')
    for line in f:
        L = line.strip().split(',')
        if len(L) > 1:
            if num_cols == 0:
                if L[-1] == '':
                    print('here')
                    num_cols = len(L) -1
                else:
                    num_cols = len(L)
            num_rows += 1   
            
            # check for consistency in number of columns
            num_cols_curr = len(L)
            if num_cols_curr != num_cols:
                raise Exception('Number of columns is inconsistent in the file.')
                sys.exit(1)
    f.close()
    file_dimensions = (num_rows, num_cols)
    return file_dimensions

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
