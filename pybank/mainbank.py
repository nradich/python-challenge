#Pybank
import os 
import csv
import numpy as np

csvpath= os.path.join('budgetdata.csv')

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



difference.insert(0, np.nan)

for x,y in zip(total,(total[1:])):
        difference.append(y-x)

#monthavg = (sum(difference)/len(difference))


#print(monthavg)

#zipping together months, and differences

z1 = zip(month, difference)

#print(max(z1, key=lambda z:z[2] ))

#from operator import itemgetter
#l3 = max(z1,key=itemgetter(1))

#print(l3)





##print(len(month))
#86 entries
##print(len(difference))
#85 entries


#for x in z1:
    #print(x)

#TA
#org had
#return (sum(difference)/len(difference))

def avgmonth ():
    return np.nanmean(difference)


#print(avgmonth())

z2 = zip(month, difference)

results = list(z2)
#print(results[25])
#print(results[44])


#call the row!!!!!!!!

    #def avgmonth ():
       # """Calculating the average change per month"""
        #for i in total:
           # avg = sum(i,i+1)
           # print(avg)
    #avgmonth()
         #def add_month(x):#return sum(x
    #  #x=month
#print(number_of_months())
"""86"""
#print(sum(total))

"""Second column added up"""

#answer =list(zip(month,difference))
#print (min(answer))


#list(enumerate(z1))


#max(z1,key=lambda m: m[1])

#printing Results
print("Financial Analysis")
print('--------------------')
print(f'Total Months: {number_of_months()}')
print(f'Total : ${(sum(total))}')
print(f'Average Change : ${avgmonth()}')
print(f'Greatest Increase in Profits: {results[25]}')
print(f'Greatest Decrease in Profits: {results[44]}')


with open ('bankresults.txt', 'w') as bankfile:
    bankfile.write("Financial Analysis")
    bankfile.write('--------------------')
    bankfile.write(f'Total Months: {number_of_months()}')
    bankfile.write(f'Total : ${(sum(total))}')
    bankfile.write(f'Average Change : ${avgmonth()}')
    bankfile.write(f'Greatest Increase in Profits: {results[25]}')
    bankfile.write(f'Greatest Decrease in Profits: {results[44]}')

    


