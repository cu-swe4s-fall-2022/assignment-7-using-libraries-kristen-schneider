test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

## FUNCTIONAL TESTS FOR RANDOM MATRIX
# testing successful runs for random matrix
run basic_matrix1 python process.py --mode matrix --rows 0 --cols 0
assert_exit_code 0
assert_in_stdout 0
run basic_matrix2 python process.py --mode matrix --rows 3 --cols 4
assert_exit_code 0
assert_in_stdout 3
# testing bad runs for random matrix
run zeros_matrix1 python process.py --mode matrix --rows 0 --cols 1
assert_exit_code 1
run zeros_matrix2 python process.py --mode matrix --rows 1 --cols 0
assert_exit_code 1
run negative_matrix1 python process.py --mode matrix --rows 0 --cols -1
assert_exit_code 1
run negative_matrix1 python process.py --mode matrix --rows -1 --cols 0
assert_exit_code 1


## FUNCTIONAL TESTS FOR FILE DIMENSIONS
# testing successful runs for file dimensions
run iris_dimensions python process.py --mode dimensions --in_file iris.data
assert_exit_code 0
assert_in_stdout '(150, 5)'
# testing bad runs for file dimensions
run bad_dimensions python process.py --mode dimensions --in_file bad.data
assert_exit_code 1


## FUNCTIONAL TESTS FOR WRITING FILE
# testing successful runs for write matrix
run basic_write python process.py --mode out --rows 5 --cols 8 --out_file out.csv
assert_exit_code 0
rm 'out.csv'
# testing bad runs for write matrix
run bad_write python process.py --mode out --rows 0 --cols 0 --out_file out.csv
assert_exit_code 1
FILE='out.csv'
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi


