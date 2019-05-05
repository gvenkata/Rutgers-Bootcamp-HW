#PyPoll
import csv
import os
import pandas

f = pandas.read_csv('employee_data.csv', index_col = "Emp ID")
print(f)
