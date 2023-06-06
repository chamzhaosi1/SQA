# Installer Python 3.11.3
# Refer: https://www.python.org/downloads/release/python-3113/

# Check python version
python --version

# Installl virtualenv
pip install virtualenv

# Change directory to project folder
cd C:\Users\cham\OneDrive\Documents\Project\SQA

# Create virtual environment
virtualenv  --python C:\Users\cham\AppData\Local\Programs\Python\Python311\python.exe venv

# Run as administrator
# To allow execution of PowerShell scripts:
Set-ExecutionPolicy Unrestricted -Force

## Reload VS code

# Change directory to project folder
cd C:\Users\cham\OneDrive\Documents\Project\SQA

## Activate virtual environment
venv\Scripts\activate.ps1

# Change directory to unit test folder
cd C:\Users\cham\OneDrive\Documents\Project\SQA\unit_test

# Install required library
pip install pytest
pip install flask

## Remark
#Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and subdirectories. Pytest automatically identifies those files as test files. We can make pytest run other filenames by explicitly mentioning them.

#Pytest requires the test function names to start with test. Function names which are not of format test* are not considered as test functions by pytest. We cannot explicitly make pytest consider any function not starting with test as a test function.
