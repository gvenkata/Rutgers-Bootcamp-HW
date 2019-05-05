#PyPoll
import csv
import os

candidates = []
candidates2d = []
counter = 0
vName = ""
vCount = 0
vPerc = 0



with open ("election_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    voter_list = list(reader)

print()
print("Election Results")
print("-----------------")

print ("Total Votes: " + str(len(voter_list)))
print("-----------------")

#Create 1d list of unique candidates from file
for row in voter_list:
    if row[2] not in candidates: 
        candidates.append(row[2])
    else: 
        pass

#Create 2d list with 0 for vote totals
for i in range (len(candidates)):
    candidates2d.append([candidates[i], 0])

#Tally rows in file to update 2d array with vote counts and do calcs
for row in voter_list: 
    for i in range(len(candidates2d)):     
        if row[2].strip() == candidates2d[i][0].strip():
            candidates2d[i][1]= candidates2d [i][1] + 1

with open("output.txt", "a") as o:
    print("Election Results", file=o)
    print("-----------------", file=o)
    print ("Total Votes: " + str(len(voter_list)), file=o)
    print("-----------------", file=o)

    for i in range (len(candidates2d)):
        vName = candidates2d [i][0]
        vCount = candidates2d [i][1]
        vPerc = round((vCount/len(voter_list)) * 100, 2)
        print (vName + ": " + str(vPerc) + "% (" + str(vCount) + ")")
        print (vName + ": " + str(vPerc) + "% (" + str(vCount) + ")", file=o)

f.close
o.close



