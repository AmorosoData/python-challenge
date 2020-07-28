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
    voter_list=[]
    county_list=[]
    candidate_list=[]

# loop through data for votes
    for row in csv_reader:
        voter_list.append(row[0])



        county_list.append(row[1])
        candidate_list.append(row[2])
    # print(voter_list)

    # Print number of months
    total_votes = len(voter_list)
    print (f"Total number of votes: {total_votes}"\n)
    


    for row in csv_reader:
        if row[2] not in candidate_list:
            candidate_list.apend(row[2])
    print (f"These are the name of all candidates: {candidate_list}")
