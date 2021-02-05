# Import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Make a list of voters by Voter ID
    Voter = []

    # Loop through data...Weeeeeeeeeee
    for row in csvreader:

            #Add Voter to list
            Voter.append(row[0])

    print(f'Election Results')
    print(f'----------------')
    print(f'Total Votes: {len(Voter)}')
    print(f'----------------')
    print(f'{name}{percent}{votes}')
    print(f'----------------')
    print(f'Winner: {name}')
    print(f'----------------')