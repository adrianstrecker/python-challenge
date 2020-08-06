#import modules
import os
import csv
from collections import Counter

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
    #create variables for percentage of each candidate
    k_percentage = (candidate_k_total)/(total_votes)
    c_percentage = (candidate_c_total)/(total_votes)
    l_percentage = (candidate_l_total)/(total_votes)
    o_percentage = (candidate_o_total)/(total_votes)
#---------------------------------------------------------------
#create candidate list to find winner
#----------------------------------------------------------------
    candidate_list = [candidate_k, candidate_c, candidate_l, candidate_o]
    candidate_list_total = [candidate_k_total, candidate_c_total, candidate_l_total, candidate_o_total]
    winner = max(candidate_list_total)
    winner_name = str(candidate_list.index[max(candidate_list_total)])
    print(winner_name)  

#print results
print("Election Results"+ "\n-------------------------------"+ "\nTotal Votes: " + f'{total_votes}')
print("-------------------------------")
#print Khan total
print("Khan: " + "{:.0%}".format(k_percentage) + " " + "(" + f'{candidate_k_total}' + ")")
#print Correy total
print("Correy: " + "{:.0%}".format(c_percentage) + " " + "(" + f'{candidate_c_total}' + ")")
#print Li total
print("Li: " + "{:.0%}".format(l_percentage) + " " + "(" + f'{candidate_l_total}' + ")")
#print O'Tooley total
print("O'Tooley: " + "{:.0%}".format(o_percentage) + " " + "(" + f'{candidate_o_total}' + ")")
print("-------------------------------")

#print output
with open(output_file, 'w') as txtFile:
    #output results to .txt file
    txtFile.write("Election Results"+ "\n-------------------------------"+ "\nTotal Votes: " + f'{total_votes}' + "\n-------------------------------" + "\nKhan: " + "{:.0%}".format(k_percentage) + " " + "(" + f'{candidate_k_total}' + ")" + "\nCorrey: " + "{:.0%}".format(c_percentage) + " " + "(" + f'{candidate_c_total}' + ")" + "\nLi: " + "{:.0%}".format(l_percentage) + " " + "(" + f'{candidate_l_total}' + ")" + "\nO'Tooley: " + "{:.0%}".format(o_percentage) + " " + "(" + f'{candidate_o_total}' + ")" + "\n-------------------------------")