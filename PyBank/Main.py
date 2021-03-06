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
    # Add a boolean variable for calc of diff for second to last
    First = True
    # Make a list of the Difference in profits from month to month...Christian, Muslim, Byzantine, Fox Tv, etc.
    Diff_Profit = []
    
    # Loop through the data
    for row in csvreader:
        # Add Strings to Months list
        Months.append(str(row[0]))
        # Add Integers to Profit list
        Profit.append(int(row[1]))
        # Add the Calculated Difference to Diff_Profit List
        if not First == True:
            Diff_Profit.append(Profit[-1] - Profit[-2])
        else:
            First = False

    
    # Print my final analysis
    print(f'Financial Analysis')
    print(f'------------------')
    print(f'Total Months: ${len(Months)}')
    print(f'Total Profit: ${sum(Profit)}')
    print(f'Average Change: ${(sum(Diff_Profit) / len(Diff_Profit)):.2f}')
    print(f'Greatest Increase in Profit: {Months[Diff_Profit.index(max(Diff_Profit))]} ${max(Diff_Profit)}')
    print(f'Greatest Decrease in Profit: {Months[Diff_Profit.index(min(Diff_Profit))]} ${min(Diff_Profit)}')
    print(f'------------------')

# Set variable for output file
output_file = os.path.join("Analysis","Financial_Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=',')

    # Write the Analysis
    writer.writerow([f'Financial Analysis'])
    writer.writerow([f'------------------'])
    writer.writerow([f'Total Months: {len(Months)}'])
    writer.writerow([f'Total Profit: ${sum(Profit)}'])
    writer.writerow([f'Average Change: ${(sum(Diff_Profit) / len(Diff_Profit)):.2f}'])
    writer.writerow([f'Greatest Increase in Profit: {Months[Diff_Profit.index(max(Diff_Profit))]} ${max(Diff_Profit)}'])
    writer.writerow([f'Greatest Decrease in Profit: {Months[Diff_Profit.index(min(Diff_Profit))]} ${min(Diff_Profit)}'])
    writer.writerow([f'------------------'])