#PyBank
import csv
import os

unique_months = []
grand_total = 0
top_month = 0
bottom_month = 0
diff = 0
diffs = []
diffs.append([])

total_diffs = 0
grt_inc = 0
grt_inc_month= ""
grt_dec = 0
grt_dec_month= ""
vDate = ""



with open ("budget_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    budget_list = list(reader)

for i in range(len (budget_list)):
    for j in range(len(budget_list[i])):
        if j == 0:
            if budget_list[i][j] not in unique_months:
                unique_months.append(budget_list[i][j])
        if j == 1:
            grand_total = grand_total + float(budget_list[i][j])

for i in range(len (budget_list)):
    for j in range(len(budget_list[i])):
        if i==0 and j==1:
            top_month = float(budget_list[i][j])
        elif i != 0 and j == 0:
            vDate = budget_list[i][j]
            #print ("i is " + str(i))
            #print ("j is " + str(j))
            diffs[i-1].append(vDate)
        elif i != 0 and j == 1:
            bottom_month = float(budget_list[i][j])
            diff = top_month - bottom_month
            top_month = bottom_month
            #print ("i2 is " + str(i))
            #print ("j2 is " + str(j))
            diffs[i-1].append(diff)
            diffs.append([])
            #print(diffs)
        else:
            pass
    
for i in range(len(diffs)):
       for j in range(len(diffs[i])):
           if j==1:
                total_diffs = total_diffs + float(diffs[i][j])
                if float(diffs[i][j]) > grt_inc: 
                    grt_inc = float(diffs[i][j])
                    grt_inc_month = (diffs[i][0])
                if float(diffs[i][j]) < grt_dec:
                     grt_dec = float(diffs[i][j])
                     grt_dec_month = (diffs[i][0])


print ("Financial Analysis")
print ("------------------")
print ("Total Months: " + str(len(unique_months)))
print ("Total: $" + str(grand_total))
print ("Average Change: $" + str(round(total_diffs/len(unique_months),2)))
print ("Greatest Increase: " + grt_inc_month + " (" + str(grt_inc) + ")")
print ("Greatest Decrease: " + grt_dec_month + " (" + str(grt_dec) + ")")

with open("output.txt", "a") as o:
    print ("Financial Analysis", file=o)
    print ("------------------", file=o)
    print ("Total Months: " + str(len(unique_months)),file=o)
    print ("Total: $" + str(grand_total),file=o)
    print ("Average Change: $" + str(round(total_diffs/len(unique_months),2)),file=o)
    print ("Greatest Increase: " + grt_inc_month + " (" + str(grt_inc) + ")",file=o)
    print ("Greatest Decrease: " + grt_dec_month + " (" + str(grt_dec) + ")",file=o)
f.close

