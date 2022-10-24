test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

## FUNCTIONAL TESTS FOR BOXPLOT
# testing successful runs for boxplot
run basic_boxplot python plot.py --mode box --data_file iris.data --out_png iris_boxplot.png
FILE='iris_boxplot.png'
assert_exit_code 0
rm $FILE
run bad_boxplot python plot.py --mode box --data_file bad_iris.data --out_png iris_boxplot.png
assert_exit_code 1
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi

## FUNCTIONAL TESTS FOR SCATTER PLOT
run basic_scatterplot python plot.py --mode scatter --data_file iris.data --attribute1 petal_width --attribute2 petal_length
FILE='petal_width_v_petal_length.png'
assert_exit_code 0
rm $FILE
run bad_scatterplot python plot.py --mode scatter --data_file bad_iris.data --attribute1 petal_width --attribute2 petal_length
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi
assert_exit_code 1

## FUNCTIONAL TESTS FOR MULTI PLOT
run basic_multiplot python plot.py --mode multi --data_file iris.data --attribute1 petal_width --attribute2 petal_length
FILE='multi_panel_figure.png'
assert_exit_code 0
run bad_multiplot python plot.py --mode multi --data_file bad_iris.data --attribute1 petal_width --attribute2 petal_length
rm $FILE
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi
assert_exit_code 1



