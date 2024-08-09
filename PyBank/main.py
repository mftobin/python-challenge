import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

def print_

total_profit_losses = 0
# The total number of months included in the dataset
    total_rows = csvfile.readlines()
    total_months = len(total_rows)
    print("Total Months:", total_months)

# The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        try:
            value = int(row[1])
            total_profit_losses += value
        except ValueError:
            print(f"Skipping non-integer value in row: {row}")
    print(f"Total: $ {total_profit_losses}")

# The changes in "Profit/Losses" over the entire period, and then the average
#  of those changes 

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period