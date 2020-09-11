## Importing the relevant modules
import os
import csv
import datetime


## Changing the terminal directory to the location to the location of the main python script
os.chdir(os.path.dirname(__file__))

## Creating the file paths
py_boss_file = os.path.join("Resources", "employee_data.csv")

py_boss_output_file = os.path.join("Cleaned_file","cleaned_employee_data.csv")

## Creating empty lists in which to store relevant information
emp_ID_list = []
first_name_list = []
last_name_list = []
corrected_DOB_list = []
SSN_list = []
state_list = []
DOB_list = []
formatted_SSN_list = []

## US States Abbreviation Dictionary
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

## Opening the CSV File as DictReader to clean the data set 
with open(py_boss_file) as csvfile:
    
    # CSV File being open as a DictReader
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        emp_ID_list = emp_ID_list + [row["Emp ID"]]

        ## Need to create a seperate list that contains the names that
        # are seperated as first and second name

        # Name are being split with the space as a parameter
        name_split = row["Name"].split(" ")

        # Appending the first and last name into different lists
        first_name_list = first_name_list + [name_split[0]]
        last_name_list = last_name_list + [name_split[1]]

        # Reformatting the date time by replacing "-" with "/"
        # Reading the "DOB" as dates
        corrected_DOB_list = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        corrected_DOB_list = corrected_DOB_list.strftime("%m/%d/%Y")

        ## Creating a new list with formatted DOB
        DOB_list = DOB_list + [corrected_DOB_list]

        ## Obtaining the SSN list and reformatting the parameters
        SSN_list = list(row["SSN"])
        SSN_list[0:3] = ("*","*","*")
        SSN_list[4:6] = ("*","*")
        combined_SSN_list = "".join(SSN_list)
        formatted_SSN_list = formatted_SSN_list + [combined_SSN_list]

        ##Abbreviating states
        State_abbreviated = us_state_abbrev[row["State"]]
        state_list = state_list + [State_abbreviated]

## The formatted lists will now be collated and exported into a new CSV file
cleaned_employee_data = zip(emp_ID_list,first_name_list,last_name_list,DOB_list, formatted_SSN_list, state_list)

with open(py_boss_output_file, 'w') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN","State"])
    csvwriter.writerows(cleaned_employee_data)
    

