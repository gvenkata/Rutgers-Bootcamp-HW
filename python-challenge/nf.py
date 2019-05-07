# Netflix lookup

#Finding the info to some of Netflix's most popular videos

## Instructions

#* Prompt the user for what video they are looking for.

#* Search through the `netflix_ratings.csv` to find the user's video.

#* If the CSV contains the user's video then print out the title, what it is rated and the current user ratings.

  ##* For example "Pup Star is rated G with a rating of 82"

#* If the CSV does not contain the user's video then print out a message telling them that their video could not be found.
import csv
import os

file = "netflix_ratings.csv"

with open ("netflix_ratings.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    nf_list = list(reader)

movie = input("What video are you looking for? ")

for row in nf_list:
    if movie == row[0]: 
        print ("got it")
        print (row[0])
        print (row[1])
        print (row[2])
        print (row[3])
        print (row[4])
        print (row[5])
        print (row[6])
        break
    else: 
        print ("Go to redbox")