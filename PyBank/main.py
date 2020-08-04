#import modules
import os
import csv

#output results to txt file
output_file = os.path.join ('Analysis', 'budget_results.txt')
    
#csv file path
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
    #profit_loss_total = 0
    pltotal = []
    for row in data:
        tot_prof = row[1]
        pltotal.append(tot_prof)
    pltotal2 = [float(integral) for integral in pltotal]
    final_pltotal = sum(pltotal2)
#print total months
print("Financial Analysis\n\nTotal Months: " + f'{sum_month}')
print("Total: " + f'{final_pltotal}'.rstrip('.0'))
#---------------------------------------------------------------------------
#set file pate using write mode
with open(output_file, 'w') as txtFile:
    #write total months life]
    #txtFile.write("Financial Analysis")
    txtFile.write("Financial Analysis\n---------------------------------\nTotal Months: "+ f'{sum_month}'"\nTotal: " + f'{final_pltotal}'.rstrip('.0'))
    #write total profit/loss
    #txtFile.write("Total: " + f'{final_pltotal}'.rstrip('.0'))