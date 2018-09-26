import os 
import csv

csvpath= os.path.join('budgetdata.csv',)

month =[]
total = []
difference = []

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


  

for x,y in zip(total,(total[1:])):
        difference.append(y-x)
print(difference)

def avgmonth ():
    return sum(difference)/len(difference)

print(avgmonth())
print(max(difference))
print(min(difference))

    #def avgmonth ():
       # """Calculating the average change per month"""
        #for i in total:
           # avg = sum(i,i+1)
           # print(avg)
    #avgmonth()
         #def add_month(x):#return sum(x
    #  #x=month
#print(number_of_months())
#"""86"""
#print(sum(total))
#"""Second column added up"""
#x= number_of_months()
    #y= sum(total)
    #print(y/x)