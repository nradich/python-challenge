#Pypoll

import os
import csv

csvpath = os.path.join('electiondata.csv')

votes =[]
candidates = []

with open ('electiondata.csv', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

        
khancount = 0
corcount = 0
licount = 0
toolcount = 0      
        
for x in candidates:       
    if x == 'Khan':
        khancount = khancount + 1
    elif x == 'Correy':
        corcount = corcount +1
    elif x == 'Li':
        licount = licount + 1
    else:
        toolcount = toolcount +1 

votecount = 0
for x in votes:
    votecount = votecount +1
    

#print(khancount)
#print(corcount)    
#print(licount)    
#print(toolcount)

a = ((khancount)/(votecount)) * 100
c= ((corcount)/(votecount)) * 100
l =((licount)/(votecount))* 100
t = ((toolcount)/(votecount))* 100


#Answer to 1st Question

print('Election Results')
print('-----------------')
print(f'Total Votes:{len(votes)}')
print('------------------')
#calculate the percentages
print(f'Khan:{round(a,2)}%, {khancount}')
print(f'Correy: {round(c,2)}%, {corcount} ')
print(f'Li: {round(l,2)}%, {licount}')
print(f"O'Tooley: {round(t,2)}%, {toolcount}")
print('-------------------')
print('Winner: Khan')



#sending results to a file
with open ('pollresults.txt', 'w') as pollfile:
    pollfile.write('Election Results')
    pollfile.write('-----------------')
    pollfile.write(f'Total Votes:{len(votes)}')
    pollfile.write('------------------')
    pollfile.write(f'Khan:{round(a,2)}%, {khancount}')
    pollfile.write(f'Correy: {round(c,2)}%, {corcount} ')
    pollfile.write(f'Li: {round(l,2)}%, {licount}')
    pollfile.write(f"O'Tooley: {round(t,2)}%, {toolcount}")
    pollfile.write('-------------------')
    pollfile.write('Winner: Khan')







