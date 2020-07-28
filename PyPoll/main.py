import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
file_to_output= os.path.join("Analysis", "Election_Results.txt")
with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader)
    #print (f"CSV Header: {csv_headers}"
    # Variables
    candidates = []
    votes = 0
    
    # Loop through csv_reader
    for row in csv_reader:
        # if value in Candidate column is not in candidate_list,
        # append to candidate_list
        if row[2] not in candidates:
            votes+=1
            candidates.append(row[2])
        else:
            votes+=1
   
    # count votes per candidate
    i = 0 
    num_candidates = len(candidates)
    candidate_votes = [0]*num_candidates

    for i in range(num_candidates):
        if row[2] == candidates[i]:
            candidate_votes[i] += 1
        # print (len(candidate_list)) = 4
    most_vote = max(candidate_votes)
    vote_index = candidate_votes.index(most_vote)
    winner = candidates[vote_index]

    #print (winner)

    # percent per candidate
    j = 0
    percent_of_votes = []
    for j in range(num_candidates):
        percent = round(candidate_votes[j]/votes * 100,2)
        percent_of_votes.append(percent)

output = (
    f"Election Resultes\n"
    f"______________________\n"
    f"Total Votes: {votes}\n"
    f"Name: {candidates} {percent_of_votes}, {candidate_votes}\n"
    f"Winner: {winner}\n"
    )

# Print the output in code
print(output)
# Export the results to text file
with open(file_to_output, 'w') as textfile:

#     # Initialize csv.writer
   textfile.write(output)