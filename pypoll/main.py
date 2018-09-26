#Pypoll

import os
import csv

csvpath = os.path.join('electiondata.csv')

votes =[]

with open ('electiondata.csv', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
        votes.append(row[0])



# Answer to 1st Question
print(len(votes))



