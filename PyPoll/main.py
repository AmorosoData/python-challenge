# Incorporated the csv module
import csv
import os
# Files to load and output (Remember to change these)
csvpath = os.path.join("Resources", "election_data.csv")
output = os.path.join("analysis", "election_analysis.txt")

# Read and next past headers
with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)
    #print (f"CSV Header: {csv_headers}"

    # List Variables
    list=[]
    vote_count=0

    for row in csv_reader:
        # print(row)
        if row[2] not in list:
            vote_count +=1
            list.append(row[2])
        else:
            vote_count+=1
            print(len(list)) =3


