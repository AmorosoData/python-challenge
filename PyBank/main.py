import os
import csv

bank_csv_path = os.path.join("", "Resources", "budget_data.csv")

with open(bank_csv_path) as csvfile:
    data_reader = csv.reader(csvfile, delimiter=",")

     # Read the header row first
    # csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in data_reader:
        print(row)

        # Store all of the text inside a variable called "months"
        months = csvfile.readlines()

        # Print the contents of the text file
        # print(months)

        print(len(months))
