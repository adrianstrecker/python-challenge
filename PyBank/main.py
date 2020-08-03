#import modules
import os
import csv

#output results to txt file
output_file = os.path.join ('Resources', 'budget_results.txt')
    
#csv file path
file_path = os.path.join ('Resources', 'budget_data.csv')
with open(file_path, "r") as csvFile:
#Create csv reader
    csv_reader = csv.reader(csvFile, delimiter=',')
    #create variables for sum of month
    data = list(csv_reader)
    sum_month = len(data)-1
#print total months
print("Total Months: " + f'{sum_month}')

#set file pate using write mode
with open(output_file, 'w') as txtFile:
    #write total months life
    txtFile.write("Total Months: " + f'{sum_month}')