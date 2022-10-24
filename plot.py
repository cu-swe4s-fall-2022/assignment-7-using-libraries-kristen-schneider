import argparse
import plotter

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True)
    parser.add_argument('--data_file', required=True)
    parser.add_argument('--out_png')
    parser.add_argument('--attribute1')
    parser.add_argument('--attribute2')
    parser.add_argument('--species')
    return parser.parse_args()

def main():
    args = get_args()
    
    # box plot
    if args.mode == 'box':
        plotter.make_boxplot(args.data_file, args.out_png)
    # scatter plot
    elif args.mode == 'scatter':
        plotter.make_scatterplot(args.data_file, args.attribute1, args.attribute2)
    # both figures 
    elif args.mode == 'both':
        plotter.combine_plots(args.data_file, args.attribute1, args.attribute2)
    
    
if __name__ == '__main__':
    main()