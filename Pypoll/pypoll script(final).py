import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
total_votes = 0
candidates_unique = []
candidate_votes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidate_votes.append(1)

percentage = []
max_votes = candidate_votes[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_percentage = round(candidate_votes[x]/total_votes*100, 2)
    percentage.append(vote_percentage)
    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_index = x
election_winner = candidates_unique[max_index] 

(f'Election Results'+'\n')
(f'----------------------------'+'\n')
print(f'Total Votes: {total_votes}')
print("-"*28)
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})')
print("-"*28)
print(f'Winner: {election_winner}')
print("-"*28)

with open('Election_results_Analysis1.txt', 'w') as f:
    f.write(f'Election Results'+'\n')
    f.write(f'----------------------------'+'\n')
    f.write(f'Total Votes: {total_votes}')
    f.write(f'\n')
    f.write("-"*28)
    f.write(f'\n')
    for x in range(len(candidates_unique)):
        f.write(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})'+'\n')
    f.write("-"*28)
    f.write(f'\n')
    f.write(f'Winner: {election_winner}')
    f.write(f'\n')
    f.write("-"*28)
