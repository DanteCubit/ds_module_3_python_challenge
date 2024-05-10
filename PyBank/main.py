#Tutor was helpful in refactoring code
import csv

#variable list
csvpath = 'PyBank/Resources/budget_data.csv'
output_file = "PyBank/Analysis/results.txt"
month_count = 0
total_profit = 0
last_month_profit = 0
changes = []

# Open the CSV file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Read rows
    for row in csvreader:
        month_count += 1
        total_profit += int(row[1])

        # Calculate change
        if month_count > 1:
            change = int(row[1]) - last_month_profit
            changes.append(change)

        last_month_profit = int(row[1])

# Calculate average change
avg_change = sum(changes) / len(changes)

# Find max and min changes
max_change = max(changes)
min_change = min(changes)
max_month = min_month = None

# Find the corresponding months for max and min changes
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header again
    for row in csvreader:
        if int(row[1]) - last_month_profit == max_change:
            max_month = row[0]
        elif int(row[1]) - last_month_profit == min_change:
            min_month = row[0]

# Generate output summary
output = (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${round(avg_change, 2)}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})\n")

# Print and save
with open(output_file, "w") as txt_file:
    print(output)
    txt_file.write(output)