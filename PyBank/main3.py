import os
import csv

# Create path
csvpath = os.path.join("Resources", "budget_data.csv")
file_to_output= os.path.join("Analysis", "budget_analysis.txt")

# Read and next past headers
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    # Read header row
    header = next(csv_reader)
    # remove 1st row of data
    # first_row = next(csv_reader)

# Lists to store data
    months=[]
    profit=[]

# loop through data and write to months lists and profit lists
    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1]))

    # Print number of months
    total_months = len(months)
    # print (f"Total Months: {total_months}")

    # Get the profit/loss for net. Lists as str so need to int profit
    net = 0
    i = 1

    # loop through and add profit/loss to net
    for i in range(total_months):
        net = net +int(profit[i])
    # print(f'Total: ${net}')

difference = []
x=0
y=0

for x in range(total_months):
    if x==0:
        difference.append(0)
    else:
        difference.append(int(profit[x]-int(profit[y])))
        y+=1
# print(difference)

average_month = ((sum(difference))/(len(difference)))
# print (f'Avg difference: ${round((average_month),2)}')

# Use min and max to find changes in difference list
max_change = max(difference)
# print (f"${max_change}")
min_change = min(difference)
# print (f"${min_change}")

# create my output prints

output = (
    f"Financial Analysis\n"
    f"______________________\n"
    f"Total Months in dataset: {total_months}\n"
    f"Net Total of profit/loss: ${net}\n"
    f"Average Changes in profit/loss: ${round((average_month),2)}\n"
    f"Greatest Increase in Profits: ${max_change}\n"
    f"Greatest Decrease in Profits: ${min_change}\n"
    )

# Print the output in code
print(output)
# Export the results to text file
with open(file_to_output, 'w') as textfile:

#     # Initialize csv.writer
   textfile.write(output)