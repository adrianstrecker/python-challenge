#import modules
import os
import csv
import statistics

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
    data = list(csv_reader)
    sum_month = len(data)
    #create variable for total profit/loss
    pltotal = []
    for row in data:
        pltotal.append(float(row[1]))
    final_pltotal = sum(pltotal)
    #create variables for monthly change
    monthly_change = []
    previous_month = 0.00
    current_month = 0.00
    date = []
    for i in range(1,len(pltotal)):
        monthly_change.append(pltotal[i] - pltotal[i-1])
        avg_change = sum(monthly_change)/len(monthly_change)
        #create greatest increase
        greatest_increase = max(monthly_change)
        #greatest_date = str(date[monthly_change.index(max(monthly_change))])
        #create greatest decrease
        greatest_decrease = min(monthly_change)
#print total months
print("Financial Analysis\n\nTotal Months: " + f'{sum_month}')
#print total profit/loss
print("Total: " + f'${final_pltotal}'.rstrip('.0'))
print("Average Change: " + f'${round(avg_change, 2)}')
print("Greatest Increase in Profits: " + f'${greatest_increase}'.rstrip('.0'))
print("Greatest Decrease in Profits: " + f'${greatest_decrease}'.rstrip('.0'))
#---------------------------------------------------------------------------
#set file pate using write mode
with open(output_file, 'w') as txtFile:
    #output results to .txt file
    txtFile.write("Financial Analysis\n---------------------------------\nTotal Months: "+ f'{sum_month}'"\nTotal: " + f'${final_pltotal}'.rstrip('.0') + "\nAverage Change: " + f'${round(avg_change, 2)}' + "\nGreatest Increase in Profits: " + f'${greatest_increase}'.rstrip('.0') + "\nGreatest Decrease in Profits: " + f'${greatest_decrease}'.rstrip('.0'))
