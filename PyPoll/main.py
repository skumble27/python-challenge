## PyPoll Project
## Importing the relevant modules for analyses
import os
import csv
import statistics
from collections import Counter

## Changing the terminal directory to the main script
os.chdir(os.path.dirname(__file__))

## File path to access the CSV Data to run the python script
py_poll_file = os.path.join("Resources", "election_data.csv")

## File path to export the data as a text file
output_py_poll_file = os.path.join("Analysis", "Analysis_PyPoll.txt")

## Declaring the variables for analysis of CSV Data

total_votes = 0
candidate_raw_tally = []
candidate_list_count = []

## Opening and Reading the CSV File
with open(py_poll_file) as csvfile:
    
    ## Reading the CSV File
    csvreader = csv.reader(csvfile, delimiter =',')

    ## Read the first line of the CSV File
    csvheader = next(csvreader)

    ## Looping through the rows in the CSV File
    for row in csvreader:

        ## Adding up the total number of votes
        total_votes += 1

        ## Adding the third column into a seperate list in is raw format
        candidate_raw_tally.append(row[2])

## Obtain Unique candidates and how many votes they received using the counter function
## Converting the list to a dictionary
candidate_list_count = dict(Counter(candidate_raw_tally))




## The Dictionary has been organised and ranked from highest to lowest using the counter function
top_ranked_name = list(candidate_list_count.keys())[0]
second_ranked_name = list(candidate_list_count.keys())[1]
third_ranked_name = list(candidate_list_count.keys())[2]
fourth_ranked_name = list(candidate_list_count.keys())[3]

## The total number of votes will be added to a new variable and indexed to the name
top_rank = candidate_list_count[list(candidate_list_count.keys())[0]]
second_rank = candidate_list_count[list(candidate_list_count.keys())[1]]
third_rank = candidate_list_count[list(candidate_list_count.keys())[2]]
fourth_rank = candidate_list_count[list(candidate_list_count.keys())[3]]

## Writing the output file into a textfile
with open(output_py_poll_file, 'w') as datafile:
    datafile.write(f'Election Results\n')
    datafile.write(f'---------------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write(f'{top_ranked_name}: {format(100*(top_rank/total_votes),".3f")}% ({top_rank})\n')
    datafile.write(f'{second_ranked_name}: {format(100*(second_rank/total_votes),".3f")}% ({second_rank})\n')
    datafile.write(f'{third_ranked_name}: {format(100*(third_rank/total_votes),".3f")}% ({third_rank})\n')
    datafile.write(f'{fourth_ranked_name}: {format(100*(fourth_rank/total_votes),".3f")}% ({fourth_rank})\n')
    datafile.write(f'---------------------------------\n')
    datafile.write(f'Winner: {top_ranked_name}\n')
    datafile.write(f'---------------------------------\n')
    datafile.close()

## Displaying the output data onto the terminal
    print(f'Election Results')
    print(f'---------------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'{top_ranked_name}: {format(100*(top_rank/total_votes),".3f")}% ({top_rank})')
    print(f'{second_ranked_name}: {format(100*(second_rank/total_votes),".3f")}% ({second_rank})')
    print(f'{third_ranked_name}: {format(100*(third_rank/total_votes),".3f")}% ({third_rank})')
    print(f'{fourth_ranked_name}: {format(100*(fourth_rank/total_votes),".3f")}% ({fourth_rank})')
    print(f'---------------------------------')
    print(f'Winner: {top_ranked_name}')
    print(f'---------------------------------')


    
