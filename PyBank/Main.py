# Import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Define the function and have it accept the 'budget_data' as its sole parameter
def Print_Analysis(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    Month = str(budget_data[0])
    Profit = int(budget_data[1])

    #Total months can be found by finding the length of the month column
    Total_Months = len(Month)
    
    #Total profit can be found by summing the profit column
    Total_Profit = sum(Profit)

    #Average change can be found by averaging the listed difference
    Average_Profit = Total_Profit / Total_Months

    #Find greatest increase by finding max.
    Greatest_Increase = max(Profit)
    
    #Find greatest increase by finding max.
    Greatest_Decrease = min(Profit)

    #Print analysis
    print(f'Financial Analysis')
    print(f'------------------')
    print(f'Total Months: {Total_Months}')
    print(f'Total Profit: {Total_Profit}')
    print(f'Average Change: {Average_Profit}')
    print(f'Greatest Increase in Profit: {Greatest_Increase}')
    print(f'Greatest Decrease in Profit: {Greatest_Decrease}')
    print(f'------------------')

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    Print_Analysis

