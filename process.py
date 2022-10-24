import argparse
import data_processor as dp

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows')
    parser.add_argument('--cols')
    parser.add_argument('--in_file')
    parser.add_argument('--out_file')
    return parser.parse_args()

def main():
    args = get_args()
    
    # random matrix
    random_matrix = dp.get_random_matrix(int(args.rows), int(args.cols))
    print(len(random_matrix))
    
    # file dimensions
    file_dimensions = dp.get_file_dimensions(args.in_file)
    print(file_dimensions)
    
    
    
if __name__ == '__main__':
    main()