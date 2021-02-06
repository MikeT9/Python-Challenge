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

    # Create a List to hold the politician's names.
    Pol_List = []

    # Create a list for total votes of respective politicians
    T_Vote = []

    # Create a lists to hold votes for each politician
    Khan_Vote = []
    Correy_Vote = []
    Li_Vote = []
    OTooley_Vote = []

    # Loop through data...Weeeeeeeeeee
    for row in csvreader:

        # Add Voter to list
        Voter.append(row[0])

        # Add Politician to list
        if row[2] not in Pol_List:
            Pol_List.append(str(row[2]))
            
        # Add votes for Politicians to lists
        if row[2] == Pol_List[0]:
            Khan_Vote.append(row[2])
        elif row[2] == Pol_List[1]:
            Correy_Vote.append(row[2])
        elif row[2] == Pol_List[2]:
            Li_Vote.append(row[2])
        elif row[2] == Pol_List[3]:
            OTooley_Vote.append(row[2])

    # Add Values to T_Vote list
    T_Vote.append(len(Khan_Vote))
    T_Vote.append(len(Correy_Vote))
    T_Vote.append(len(Li_Vote))
    T_Vote.append(len(OTooley_Vote))

    # Print Analysis
    print(f'Election Results')
    print(f'----------------')
    print(f'Total Votes: {len(Voter)}')
    print(f'----------------')
    print(f'{Pol_List[0]}: {((T_Vote[0] / len(Voter)) * 100):.3f}% ({T_Vote[0]})')
    print(f'{Pol_List[1]}: {((T_Vote[1] / len(Voter)) * 100):.3f}% ({T_Vote[1]})')
    print(f'{Pol_List[2]}: {((T_Vote[2] / len(Voter)) * 100):.3f}% ({T_Vote[2]})')
    print(f'{Pol_List[3]}: {((T_Vote[3] / len(Voter)) * 100):.3f}% ({T_Vote[3]})')
    print(f'----------------')
    print(f'Winner: {Pol_List[T_Vote.index(max(T_Vote))]}')
    print(f'----------------')