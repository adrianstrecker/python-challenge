#import modules
import os
import csv

#output results to txt file
output_file = os.path.join ('Analysis', 'election_results.txt')
    
#set csv file path being read
file_path = os.path.join ('Resources', 'election_data.csv')
with open(file_path, "r") as csvFile:
#Create csv reader
    csv_reader = csv.reader(csvFile, delimiter=',')
    #remove header
    next(csv_reader)
    #create variables for sum of month
    #https://stackoverflow.com/questions/27504056/row-count-in-a-csv-file
    #data = list(csv_reader)
    votes = []
    #date = []
    for row in csv_reader:
        votes.append(row[1])
        #date.append(row[0])
    total_votes = len(votes)
    print("Election Results"+ "\n-------------------------------"+ "\nTotal Votes: " + f'{total_votes}')
# candidateList = {candidate: votes}
#open CSV for read
#csv_file_object.next()
#for each row
#total votes = totalVotes +1
#if candidateList.index(current row candidate) <1 
	#then append dict to list and set votes = 0
#increase vote for candidate + 1
#exit for loop
#create temp variables
#for candidate in list
	#find one with most votes ( accumulator? )
	#calc and print percentage
#print outPut
with open(output_file, 'w') as txtFile:
    #output results to .txt file
    txtFile.write("Election Results"+ "\n-------------------------------"+ "\nTotal Votes: " + f'{total_votes}')	