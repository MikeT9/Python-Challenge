# Import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Make a list of months
    Months = []
    # Make a list of profits...Jesus, Muhammed, Soloman, The Simpsons, etc.
    Profit = []
    # Add a 0 to the list to provide starting variable for calc of diff as second to last
    Profit.append(0)
    # Make a list of the Difference in profits from month to month...Christian, Muslim, Byzantine, Fox Tv, etc.
    Diff_Profit = []
    
    # Loop through the data
    for row in csvreader:
        # Add Strings to Months list
        Months.append(str(row[0]))
        # Add Integers to Profit list
        Profit.append(int(row[1]))
        # Add the Calculated Difference to Diff_Profit List
        Diff_Profit.append(Profit[-1] - Profit[-2])

    # Remove the first element 0 previously added for calculation purposes
    Profit.pop(0)
    
    # Print my final analysis
    print(f'Financial Analysis')
    print(f'------------------')
    print(f'Total Months: {len(Months)}')
    print(f'Total Profit: {sum(Profit)}')
    print(f'Average Change: {(sum(Diff_Profit) / len(Months))}')
    print(f'Greatest Increase in Profit: {Months[Diff_Profit.index(max(Diff_Profit))]} {max(Diff_Profit)}')
    print(f'Greatest Decrease in Profit: {Months[Diff_Profit.index(min(Diff_Profit))]} {min(Diff_Profit)}')
    print(f'------------------')