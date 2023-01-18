import os

import csv

totalmonths = 0
total = 0 
change = []
profitloss = []
month = []

csvpath = os.path.join ('resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for csvrow in csvreader:


        totalmonths+=1

    
        total+=int(csvrow[1])


        profitloss.append(int(csvrow[1]))

        month.append(csvrow[0])
    
        change.append(profitloss[totalmonths-1]-profitloss[totalmonths-2])     

  
    totalchange = sum(change)

    averagechange = round(totalchange/(len(change)-1),2)

    inc_profit = max(change)
    grt_increase = change.index(inc_profit)

    dec_profit = min(change)
    grt_decrease = change.index(dec_profit)


outputh_path = "Budget_Analysis.txt"

file = open(outputh_path, 'w')


file.write("Financial Analysis\n")
file.write("--------------------------\n")
file.write(f"Total Months: {totalmonths}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${averagechange}\n")
file.write(f"Greatest Increase in Profits : {month[grt_increase]} (${inc_profit})\n")
file.write(f"Greatest Decrease in Profits : {month[grt_decrease]} (${dec_profit})\n")



file.close()









