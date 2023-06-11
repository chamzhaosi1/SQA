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
cd C:\Users\cham\OneDrive\Documents\Project\SQA\01_unit_test

# Change directory to api test folder
cd C:\Users\cham\OneDrive\Documents\Project\SQA\02_api_test

# Install required library
## Assignment 1
pip install pytest

## Remark
#Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and subdirectories. Pytest automatically identifies those files as test files. We can make pytest run other filenames by explicitly mentioning them.

#Pytest requires the test function names to start with test. Function names which are not of format test* are not considered as test functions by pytest. We cannot explicitly make pytest consider any function not starting with test as a test function.

## Assignment 2
pip install flask

# Refer: https://selenium-python.readthedocs.io/installation.html
## Assignment 3
pip install selenium

# Check the google chrome version
# Version 114.0.5735.110 (Official Build) (64-bit)

# Download the chrome driver (Please make sure the version is matched)
# https://sites.google.com/chromium.org/driver/
# chromedriver_win32.zip

# Extrieve the file to the porject folder

