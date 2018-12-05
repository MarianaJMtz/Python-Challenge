#Dependencies
import os
import csv

#set path the file
csvpath = os.path.join('budget_data.csv')

#open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #Find the total number of months included in the dataset
    months = 0
    net = 0
    values = [ ]
    dates = [ ]
    dif = [ ]
    next(csvreader)
    for row in csvreader:
        long = len(row[0])
        if long != 0:
            months = months + 1
            
    #Create a list for dates: will be used later            
        dates.append(row[0])
            
    #The total net amount of "Profit/Losses" over the entire period
        net = net + int(row[1])
        
    #The average change on "Profit/Losses" between months
        values.append(int(row[1]))
        
    for i in range(len(values)):
        if i>0:
            change = int(values[i])-int(values[i-1])
            dif.append(change)
    sumdif = sum(dif)
    avg= sumdif/len(dif)
    
    #The greatest increase in profits: amount 
    greatest = max(dif)
               
    #The greatest decrease in losses: amount
    loss = min(dif)
    
    #dates
    for i,j in enumerate(dif):
        if j == greatest:
            greatestdate= dates[i+1]
        if j == loss:
            lossdate = dates[i+1]     
            
#Output
print("Financial Analysis")
print("--------------------------------------")
print("Total Months: " + str(months))
print("Total: " + str(net))
print("Average Change: " + str(avg))
print("Greatest Increase in Profits: " + greatestdate +"($" +str(greatest) +")")
print("Greatest Increase in Profits: " + lossdate +"($" +str(loss) +")")

#Text file

file = open ("PyBank_Results.txt","w")

file.write("Financial Analysis")
file.write("--------------------------------------")
file.write("Total Months: " + str(months))
file.write("Total: " + str(net))
file.write("Average Change: " + str(avg))
file.write("Greatest Increase in Profits: " + greatestdate +"($" +str(greatest) +")")
file.write("Greatest Increase in Profits: " + lossdate +"($" +str(loss) +")")

file.close()