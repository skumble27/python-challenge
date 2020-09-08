import statistics
import csv


poll_file = ('E:/My Documents/Professional Development/Monash University Data Analytics Boot Camp/GitHubRepo/python-challenge/PyPoll/Resources/election_data.csv')
candidate_list = []

total_votes = 0

with open(poll_file) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes +=1
        candidate_list.append(row[2])
    
unique_candidates = set(candidate_list)
otooley_vote_count = float(candidate_list.count('O\'Tooley'))
correy_vote_count = float(candidate_list.count('Correy'))
khan_vote_count = float(candidate_list.count('Khan'))
li_vote_count = float(candidate_list.count('Li'))
unique_candidates = list(unique_candidates)

## Calculating the percentages of votes for each candidate
otooley_percentage_vote = round(float(otooley_vote_count)/float(total_votes) * float(100),3)

correy_percentage_vote = round(float(correy_vote_count)/float(total_votes) * float(100),3)

khan_percentage_vote = round(float(khan_vote_count)/float(total_votes) * float(100),3)

li_percentage_vote = round(float(li_vote_count)/float(total_votes) * float(100),3)

## Creating a Dictionary of Candidates
count_list = [otooley_vote_count, correy_vote_count, khan_vote_count, li_vote_count]

percentage_list = [otooley_percentage_vote, correy_percentage_vote, khan_percentage_vote, li_percentage_vote]


## Creating a nested dictionary
Summary_Candidates = dict({
1: {'Name': [unique_candidates[0]], 'Vote': [count_list[0]], 'Percentage': [percentage_list[0]]},

2:{'Name': [unique_candidates[1]], 'Vote': [count_list[1]], 'Percentage': [percentage_list[1]]},

3:{'Name': [unique_candidates[2]], 'Vote': [count_list[2]], 'Percentage': [percentage_list[2]]},

4:{'Name': [unique_candidates[3]], 'Vote': [count_list[3]], 'Percentage': [percentage_list[3]]}

})





