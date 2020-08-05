#import modules
import os
import csv

#output results to txt file
output_file = os.path.join ('Analysis', 'election_results.txt')
    
#set csv file path being read
file_path = os.path.join ('Resources', 'election_data.csv')
with open(file_path, "r") as csvFile:
#Create csv reader
    csv_reader = csv.DictReader(csvFile, delimiter=',')
    #Get total votes
    total_votes = -1
    for row in open(file_path):
        total_votes += 1
    #Get vote count for each candidate
    #Candidate Khan
    candidate_k = []
    #Candidate Correy
    candidate_c = []
    #Candidate Li
    candidate_l = []
    #Candidate O'Tooley
    candidate_o = []
    for row in csv_reader:
        if row['Candidate'] == 'Khan':
         candidate_k.append(row)
         candidate_k_total = len(candidate_k)
        elif row['Candidate'] == 'Correy':
         candidate_c.append(row)
         candidate_c_total = len(candidate_c)
        elif row['Candidate'] == 'Li':
         candidate_l.append(row)
         candidate_l_total = len(candidate_l)
        else:
         candidate_o.append(row)
         candidate_o_total = len(candidate_o)
        
print("Election Results"+ "\n-------------------------------"+ "\nTotal Votes: " + f'{total_votes}')
print("-------------------------------")
#print Khan total
print("Khan: " + f'{candidate_k_total}')
#print Correy total
print("Correy: " + f'{candidate_c_total}')
#print Li total
print("Li: " + f'{candidate_l_total}')
#print O'Tooley total
print("O'Tooley: " + f'{candidate_o_total}')
# candidateList = {candidate: votes}
#for each row
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