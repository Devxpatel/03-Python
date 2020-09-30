import os

import csv

totalmonths = 0

net = 0

monthlychange = []

months = []

greatest_increase = 0

greatest_increase_month = 0

greatest_decrease = 0

greatest_decrease_month = 0


csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    row = next(csvreader)
    
    previousrow = int(row[1])

    totalmonths += 1
    
    net += int(row[1])
    
    greatest_increase = int(row[1])
    
    greatest_increase_month = row[0]


    for row in csvreader:
        
        totalmonths += 1

        net += int(row[1])

        change_revenue = int(row[1]) - previousrow
        
        monthlychange.append(change_revenue)
        
        previousrow = int(row[1])
        
        months.append(row[0])
        

        if int(row[1]) > greatest_increase:

            greatest_increase = int(row[1])
            
            greatest_increase_month = row[0]
            

        if int(row[1]) < greatest_decrease:

            greatest_decrease = int(row[1])

            greatest_decrease_month = row[0]  
        

    averagechange = sum(monthlychange)/ len(monthlychange)
    
    highest = max(monthlychange)
    
    lowest = min(monthlychange)


print(f"Financial Analysis")

print(f"---------------------------")

print(f"Total Months: {totalmonths}")

print(f"Total: ${net}")

print(f"Average Change: ${averagechange:.2f}")

print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")

print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


output_file = os.path.join('.', 'Resources', 'output.txt')


with open(output_file, 'w',) as newtextfile:

    newtextfile.write(f"Financial Analysis\n")
    
    newtextfile.write(f"---------------------------\n")
    
    newtextfile.write(f"Total Months: {totalmonths}\n")
    
    newtextfile.write(f"Total: ${net}\n")
    
    newtextfile.write(f"Average Change: ${averagechange}\n")
    
    newtextfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    
    newtextfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
