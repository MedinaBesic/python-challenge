import os
import csv

# Path to collect data from the Resources folder
budget_data_csv=os.path.join('/Users', 'adnanbesic', 'desktop', 'classfolder', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

#variables added 
headers = []
rows = []
total_months = []
net_total = 0 

# The total number of months included in the dataset
# total_months 
# Read in the CSV file 
# def analysis(budget_data_csv):
with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas 
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip over title 
    header = next(csvreader)
    # Split first column into month and day
    # Save month into a list 
    # Count the # of months in list 
    # append total months if the month is not there
    # Take the sum of the profit/losses column by summing 
    for row in csvreader:
        month = row[0].split("-")[0]
        
        #check if jan is already in the list before appending
        if month not in total_months:
            total_months.append(month)
        # count how many months in the total months list 
        # possibly find the len(total_months)
#net total profit/losses 
        net_total += row[1]

        #sort list, then look at daily changes, then daily averages 


# print(total_months) 
# print(net_total)
   
# The net total amount of "Profit/Losses" over the entire period
# net_total 

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# # The greatest increase in profits (date and amount) over the entire period

# # The greatest decrease in profits (date and amount) over the entire period