import os
import csv

#Path to collect data
budget_data = os.path.join('budget_data.csv')

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

   # Split the data on commas
   csvreader = csv.reader(csvfile, delimiter=',')

   header = next(csvreader)
for row in csvreader:

#Count the number of months
   num_months = list(csvreader)
   months = len(num_months)
print(f"Total Number of Months: {str(months)}")
#total profits and loss
total_profitsandloss = 0
total_profitsandloss = total_profitsandloss + int(abs(row["Profit/Losses"]))
print(total_profitsandloss)