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
        
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    