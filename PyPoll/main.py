import os
import csv
import statistics
from collections import Counter

pypollfile = os.path.join("Resources","election_data.csv")
outputfile = os.path.join("Analysis", "Analysis_PyPoll.txt")

total_votes = 0
candidate_tally_raw = []
candidate_list_count = []

with open(pypollfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_tally_raw.append(row[2])
## You could use a dictionary to analyse

## Dictionary helps to loop through the keys
candidate_list_count = dict(Counter(candidate_tally_raw)) 

##Will give the value back for the key
top_rank = candidate_list_count[list(candidate_list_count.keys())[0]]
second_rank = candidate_list_count[list(candidate_list_count.keys())[1]]
third_rank = candidate_list_count[list(candidate_list_count.keys())[2]]
fourth_rank = candidate_list_count[list(candidate_list_count.keys())[3]]

## Providing the specific name back
top_rank_name = list(candidate_list_count.keys())[0] 
second_rank_name = list(candidate_list_count.keys())[1]
third_rank_name = list(candidate_list_count.keys())[2]
fourth_rank_name = list(candidate_list_count.keys())[3]

## Writing the file into  a text
with open(outputfile, 'w') as datafile:
    datafile.write(f'Election Results\n')
    datafile.write(f'---------------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write(f'{top_rank_name}: {round(100*(top_rank/total_votes),3)}% ({top_rank})\n')
    datafile.write(f'{second_rank_name}: {round(100*(second_rank/total_votes),3)}% ({second_rank})\n')
    datafile.write(f'{third_rank_name}: {round(100*(third_rank/total_votes),3)}% ({third_rank})\n')
    datafile.write(f'{fourth_rank_name}: {round(100*(fourth_rank/total_votes),3)}% ({fourth_rank})\n')
    datafile.write(f'---------------------------------\n')
    datafile.write(f'Winner: {top_rank_name}\n')
    datafile.write(f'---------------------------------\n')
    datafile.close()

 
## Displaying Data on the Terminal
    print(f'Election Results')
    print(f'---------------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'{top_rank_name}: {round(100*(top_rank/total_votes),3)}% ({top_rank})')
    print(f'{second_rank_name}: {round(100*(second_rank/total_votes),3)}% ({second_rank})')
    print(f'{third_rank_name}: {round(100*(third_rank/total_votes),3)}% ({third_rank})')
    print(f'{fourth_rank_name}: {round(100*(fourth_rank/total_votes),3)}% ({fourth_rank})')
    print(f'---------------------------------')
    print(f'Winner {top_rank_name}')
    print(f'---------------------------------')

    