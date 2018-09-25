import os 
import csv

csvpath= os.path.join('budgetdata.csv',)

month =[]

with open ('budgetdata.csv' , newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next (csvreader, None)

 #row 2 is month   
#row 1 is numbers
    counter = 0
    for row in csvreader:
        month.append(int(row[0])
        
    def add_month(x):
        return sum(x)
    x = month
