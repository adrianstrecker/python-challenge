#import modules
import os
import csv

#output results to txt file
output_file = os.path.join ('Analysis', 'budget_results_redone.txt')
    
#set csv file path being read
file_path = os.path.join ('Resources', 'budget_data.csv')
with open(file_path, "r") as csvFile:
#Create csv reader
    csv_reader = csv.DictReader(csvFile, delimiter=',')
    #find total months
    #next(csv_reader)
    total_months = -1
    for row in open(file_path):
        total_months += 1
    #data = list(csv_reader)
    #total profit/loss
    profit_loss = []
    date = []
    monthly = []
    for row in csv_reader:
        profit_loss.append(int(row['Profit/Losses']))
        total_pl = sum(profit_loss)
        date.append(row['Date'])
    #Calculate average monthly change
    for row in range(1,len(profit_loss)):
            monthly.append(profit_loss[row] - profit_loss[row-1])
            avg_change = sum(monthly)/len(monthly)
    #calculate maximum increase and decrease
            max_increase = max(monthly)
            max_decrease = min(monthly)
    #match date to appropriate max increase and max decrease
            date_increase = str(date[monthly.index(max(monthly))+1])
            date_decrease = str(date[monthly.index(min(monthly))+1])

#print header & total months
print("Financial Analysis" + "\n---------------------------------" + "\nTotal Months: " + f'{total_months}')
print("---------------------------------")
#print total profit/loss
print("Total: " + f'${round(total_pl):,}')
#print average change
print("Average Change: " + f'${round(avg_change, 2)}')
#print greatest increase
print("Greatest Increase in Profits: " + f'{date_increase}',"(",(f'${max_increase:,}'),")")
#print greatest decrease
print("Greatest Decrease in Profits: " + f'{date_decrease}',"(",(f'${max_decrease:,}'),")")
#---------------------------------------------------------------------------
#set file pate using write mode
with open(output_file, 'w') as txtFile:
    #output results to .txt file
    txtFile.write("Financial Analysis\n---------------------------------\nTotal Months: "+ f'{total_months}'"\nTotal: " + f'${round(total_pl):,}' + "\nAverage Change: " + f'${round(avg_change, 2)}' + "\nGreatest Increase in Profits: "+ f'{date_increase}'+ " (" + (f'${round(max_increase)}') + ")" + "\nGreatest Decrease in Profits: "+ f'{date_decrease}'+ " (" + (f'${round(max_decrease)}') + ")")