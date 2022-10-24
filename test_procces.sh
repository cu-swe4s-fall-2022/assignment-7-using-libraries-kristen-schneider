test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# testing successful runs for random matrix
run basic_matrix1 python process.py --rows 0 --cols 0 --in_file iris.data --out_file out.txt
assert_exit_code 0
assert_in_stdout 0
run basic_matrix2 python process.py --rows 3 --cols 4 --in_file iris.data --out_file out.txt
assert_exit_code 0
assert_in_stdout 3

# testing bad runs for random matrix
run zeros_matrix1 python process.py --rows 0 --cols 1 --in_file iris.data --out_file out.txt
assert_exit_code 1
run zeros_matrix2 python process.py --rows 1 --cols 0 --in_file iris.data --out_file out.txt
assert_exit_code 1
run negative_matrix1 python process.py --rows 0 --cols -1 --in_file iris.data --out_file out.txt
assert_exit_code 1
run negative_matrix1 python process.py --rows -1 --cols 0 --in_file iris.data --out_file out.txt
assert_exit_code 1

# testing successful runs for file dimensions
run basic_dimensions python process.py --rows 0 --cols 0 --in_file iris.data --out_file out.txt
assert_exit_code 0
assert_in_stdout '(150, 5)'
run bad_dimensions python process.py --rows 0 --cols 0 --in_file bad.data --out_file out.txt
assert_exit_code 1


