import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

#tracking financial parameters
total_months = 0
total_net = 0
month_of_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999]
net_change_list = []

with open(budget_csv, 'r') as csvfile:
    reader =csv.reader(csvfile)
    header = next(reader)  # skip header
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    for row in reader:
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        month_of_changes += [row[0]]
        #calculate greatest increase/decrease
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    #calculate average net change
    average_net_change = sum(net_change_list) / len(net_change_list)
    
    results = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_net_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    )
    print(results)

    analysis_path = os.path.join("analysis", "budget_analysis.txt")
    with open(analysis_path, 'w') as text_file:
        text_file.write(results)