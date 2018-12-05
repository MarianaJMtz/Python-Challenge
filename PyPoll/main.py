#Dependencies
import os
import csv
from decimal import Decimal

#set path the file
csvpath = os.path.join('election_data.csv')
#open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    next(csvreader)
    
    #Used variables
    n = 0
    candidates = [ ]
    votes = [ ]
    votesnumber = [ ]
    percentage = [ ]
    
    #number of votes
    for row in csvreader:
        long = len(row[0])
        if long != 0:
            n = n + 1
        
        votes.append(row[2])
           
    #Find the list of candidate names
        if row[2] not in candidates:
            candidates.append(row[2])
    
    #Number of votes
    for name in candidates:
        votesnumber.append(votes.count(name))
        
    #Percentage of votes
    for number in votesnumber:
        percentage.append(Decimal(int(number)*100/int(n)))
        
    #Election Winner
    position=votesnumber.index(max(votesnumber))
    Winner = candidates[position]
    
#Print values
       
print('Election Results')
print('--------------------------------------------------')
print('Total Votes: ' + str(n))
print('--------------------------------------------------')
i=0
for i in range(len(candidates)):
        print(candidates[i] + ': ' + str(round(percentage[i],3)) + '% ' + 
              '('+ str(votesnumber[i]) + ')')
i=i + 1
print('--------------------------------------------------')
print('Winner: ' + Winner)
print('--------------------------------------------------')

#Text file

file = open ("PyPoll_Results.txt","w")

file.write('Election Results')
file.write('--------------------------------------------------')
file.write('Total Votes: ' + str(n))
file.write('--------------------------------------------------')
j=0
for i in range(len(candidates)):file.write(candidates[i] + ': ' 
                  + str(round(percentage[i],3)) + '% ' + 
              '('+ str(votesnumber[i]) + ')')
j=j + 1
file.write('--------------------------------------------------')
file.write('Winner: ' + Winner)
file.write('--------------------------------------------------')

file.close()

