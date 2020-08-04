#import modules
import os
import csv

with open('output_file', 'w') as txtfile:
        #initialize writer
    #txt_writer = txt.writer(txtFile)
    
#csv file path
    file_path = os.path.join ('Resources', 'budget_data.csv')
with open(file_path, "r") as csvFile:
    #Create csv reader
    csv_reader = csv.reader(csvFile, delimiter=',')
    #remove header
    next(csv_reader)
    #create variables for total months
    total_months = 0
    total = 0
    for each in csv_reader:
        total_months += 1
    for row in csv_reader:
        total = sum(row[1])
print(total_months)
print(total)
