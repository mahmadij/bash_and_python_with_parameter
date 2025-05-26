#!/bin/bash

#========================================================== 
#Starts the venv and runs the runner.py with a passed in parameter. This is the script called from terminal with a parameter passed in.
#==========================================================

# Always operate from the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment from project-relative path
source "$SCRIPT_DIR/venv/bin/activate"

# Change into script directory
cd python-scripts

# Run the runner script with the task argument passed in 
python runner.py --task "$1"

# Deactivate venv
deactivate
