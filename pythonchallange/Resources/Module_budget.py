#Modules
import os
import csv

#set path for file
csvpath = os.path.join('budget_data.csv')

#open the csv
with open(csvpath, 'r') as file:
    reader = csv.reader(file)


       # Initialize variables
total_months = 0
total_sum = 0
total_change = 0
previous_value = None
greatest_increase = 0
greatest_increase_month = None
greatest_decrease = 0
greatest_decrease_month = None

# Open the csv
with open(csvpath, 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Loop through each row in the CSV
    for row in reader:
        # Increment total months
        total_months += 1

        # Extract the value from column 2 and convert it to an integer
        value_in_column_2 = int(row[1])

        # Add the value to the total sum
        total_sum += value_in_column_2

        # Check if it's not the first row
        if previous_value is not None:
            # Calculate the change from the previous value
            change = value_in_column_2 - previous_value

            # Add the change to the total change
            total_change += change

            # Check for greatest increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            # Check for greatest decrease
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        # Update the previous value for the next iteration
        previous_value = value_in_column_2

# Calculate the average change
average_change = total_change / (total_months - 1)  # Subtract 1 to exclude the first month from the calculation

# Print the results
print("Financial Analysis")
print("-------------------------")
print("Total Months:", total_months)
print("Total: ${}".format(total_sum))
print("Average Change: ${:.2f}".format(average_change))
print("Greatest Increase in Profits:", greatest_increase_month, "(Increase: ${})".format(greatest_increase))
print("Greatest Decrease in Profits:", greatest_decrease_month, "(Decrease: ${})".format(greatest_decrease))