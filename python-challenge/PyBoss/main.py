#PyPoll
#Push to Git
import csv
import os
import time
from us_state_abbrev import us_state_abbrev

#import pandas
veID = ""
vFN = ""
vLN = ""
vsDOB = ""
vSSN = ""
vState = ""

#f = pandas.read_csv('employee_data.csv')
with open ("employee_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    ee_list = list(reader)

with open("ee_new_format.csv", "a") as o:
    print ("Emp ID,First Name,Last Name,DOB,SSN,State", file=o)
    for row in ee_list:
        veID = row[0] 
        vFN, vLN = row[1].split()
        vDOB = time.strptime(row[2], "%Y-%m-%d")
        vsDOB = time.strftime("%m/%d/%Y", vDOB)
        vSSN = "***-**-" + row[3][7:]
        vState = us_state_abbrev[row[4]]
        print (veID + "," + vFN + "," + vLN + "," + vsDOB + "," + vSSN + "," + vState, file=o)

f.close
o.close
        
        

#Print Header

#Loop through csv file
#Emp ID is the same
#Name --> First Name, Last Name
#DOB Reformat Date to MM/DD/YYYY
# SSN mask first 5 numbers
# Convert State to 2 letter abbreviation
# Create a line, print line to csv


#print(f)
