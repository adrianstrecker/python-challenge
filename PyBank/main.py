#import modules
import os
import csv

#output results to txt file
output_file = os.path.join ('Analysis', 'budget_results.txt')
    
#set csv file path being read
file_path = os.path.join ('Resources', 'budget_data.csv')
with open(file_path, "r") as csvFile:
#Create csv reader
    csv_reader = csv.reader(csvFile, delimiter=',')
    #remove header
    next(csv_reader)
    #create variables for sum of month
    #https://stackoverflow.com/questions/27504056/row-count-in-a-csv-file
    data = list(csv_reader)
    sum_month = len(data)
    #create variable for total profit/loss
    final_pltotal = 0
    for row in data:
        final_pltotal += int(row[1])
    #create variables for monthly change and matching date
    #https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
    monthly = []
    date = []
    monthly_change = []
    for row in data:
        monthly.append(float(row[1]))
        date.append(row[0])

    for row in range(1,len(data)):
        monthly_change.append(monthly[row] - monthly[row-1])
        avg_change = sum(monthly_change)/len(monthly_change)
        #reference date that matches greatest increase - modified from site referenced on line 28
        greatest_date = str(date[monthly_change.index(max(monthly_change))+1])
        #reference date that matches greatest decrease - modified from site referenced on line 28
        greatest_decrease_date = str(date[monthly_change.index(min(monthly_change))+1])
        #create greatest increase
        greatest_increase = max(monthly_change)
        #create greatest decrease
        greatest_decrease = min(monthly_change)
#print header & total months
print("Financial Analysis\n\nTotal Months: " + f'{sum_month}')
print("---------------------------------")
#print total profit/loss
print("Total: " + f'${round(final_pltotal)}')
#print average change
print("Average Change: " + f'${round(avg_change, 2)}')
#print greatest increase
print("Greatest Increase in Profits: " + f'{greatest_date}',"(",(f'${round(greatest_increase)}'),")")
#print greatest decrease
print("Greatest Decrease in Profits: " + f'{greatest_decrease_date}',"(",(f'${round(greatest_decrease)}'),")")
#---------------------------------------------------------------------------
#set file pate using write mode
with open(output_file, 'w') as txtFile:
    #output results to .txt file
    txtFile.write("Financial Analysis\n---------------------------------\nTotal Months: "+ f'{sum_month}'"\nTotal: " + f'${round(final_pltotal)}' + "\nAverage Change: " + f'${round(avg_change, 2)}' + "\nGreatest Increase in Profits: "+ f'{greatest_date}'+ " (" + (f'${round(greatest_increase)}') + ")" + "\nGreatest Decrease in Profits: "+ f'{greatest_decrease_date}'+ " (" + (f'${round(greatest_decrease)}') + ")")