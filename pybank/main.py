import os 
import csv

csvpath= os.path.join('budgetdata.csv',)

month =[]
total = []

with open ('budgetdata.csv' , newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next (csvreader, None)

 #row 2 is month   
#row 1 is numbers
    #counting the number of months
    for row in csvreader:
        month.append(row[0])
        total.append(int(row[1]))
    def number_of_months():
        """Generates the number of rows in the CSV file"""
        return(len(month))
      
         #def add_month(x):#return sum(x
    #  #x=month
print(number_of_months())
"""86"""
print(sum(total))
"""Second column added up"