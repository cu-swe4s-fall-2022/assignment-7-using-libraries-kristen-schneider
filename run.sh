#! bin/bash

# unit tests for data processor
echo "Unit tests for data processor"
python test_data_processor.py

# functional tests for data processor
echo "Functional tests for data processor"
bash test_process.sh

# unit tests for plotter
echo "Unit tests for plotting"
python test_plotter.py

# functional tests for plotter
echo "Functional tests for plotting"
bash test_plot.sh