#import modules
import os
import csv

#set file path
file_path = os.path.join ('Resources', 'budget_data.csv')

with open(file_path, "r") as csvFile:
    #Create csv reader
    csv_reader = csv.reader(csvFile, delimiter=',')
    #create variables for sum of month
    data = list(csv_reader)
    sum_month = len(data)-1
#print total months
print("Total Months: " + f'{sum_month}')