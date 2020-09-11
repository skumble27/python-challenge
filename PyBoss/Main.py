## Importing the relevant modules
import os
import csv
import us_state_abbrev as usabr

## Changing the terminal directory to the location to the location of the main python script
os.chdir(os.path.dirname(__file__))

## Creating the file paths
py_boss_file = os.path.join("Resources", "employee_data.csv")

py_boss_output_file = os.path.join("Cleaned_file","cleaned_employee_data.csv")

## Creating empty lists in which to store relevant information
emp_ID_list = []
emp_name_list = []
DOB_list = []
SSN_list = []
state_list = []
