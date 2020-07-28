import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

# Read and next past headers
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    # Read header row
    header = next(csv_reader)
    # remove 1st row of data
    # first_row = next(csv_reader)

# Lists to store data
    candidate_list=[]
    votes = 0

# loop through data for votes
    for votes in csv_reader:
        candidate_list.append(row[2])
        votes = votes+1
        candidates=[]
    # print(voter_list)

    if candidate_list not in canidates:
        canidates.append(candidate_list)
        votes[candidate_list]=votes[candidate_list]+1
    print(votes)