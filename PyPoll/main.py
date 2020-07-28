import os
import csv
from collections import defaultdict


csvpath = os.path.join("Resources","election_data.csv")
file_to_output = os.path.join("Analysis", "Election_Results.txt")

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader)
    #print (f"CSV Header: {csv_headers}"

    # Variables
    votes = {}
    total_votes = 0
    candidates = []

    for row in csv_reader: 
        # if value in Candidate column is not in candidate_list,
        # append to candidate_list
        total_votes +=1
        candidates_name = row[2]
        if candidates_name not in candidates:
            candidates.append(candidates_name)
            votes[candidates_name] = 1
        else:
            votes[candidates_name] += 1
    # print(candidates)
    # print(votes)
    # print(total_votes)
    winner_count = 0
    with open(file_to_output,"w") as txtfile:
        output_part_one = (
        f'Election Results\n'
        f'---------------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'---------------------------------\n')
        txtfile.write(output_part_one)
        print(output_part_one)

        for i in votes:
            # print(i,votes.get(i))
            value = votes.get(i)
            percentage = round((value/total_votes)*100,2)
            output_part_two = (
                f'{i}: {percentage} ({value})\n')
            txtfile.write(output_part_two)
            print(output_part_two)

            if value > winner_count:
                winner_count = value
                winner = i
        output_part_three = (
        f'---------------------------------\n'
        f'Winner is {winner}')
        txtfile.write(output_part_three)
        print(output_part_three)
