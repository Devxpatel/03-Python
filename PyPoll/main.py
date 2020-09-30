import os

import csv

totalvotes = 0

khanvotes = 0

correyvotes = 0

livotes = 0

otooleyvotes = 0


csvpath = os.path.join('.', 'Resources', 'election_data.csv')


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)


    for row in csvreader:
        
        totalvotes += 1
        
        if (row[2] == "Khan"):
           
            khanvotes += 1
        
        elif (row[2] == "Correy"):
            
            correyvotes += 1
       
        elif (row[2] == "Li"):
            
            livotes += 1
        
        else:
            
            otooleyvotes += 1
            

    kahnpercentage = khanvotes / totalvotes
    
    correypercentage = correyvotes / totalvotes
    
    lipercentage = livotes / totalvotes
    
    otooleypercentage = otooleyvotes / totalvotes
    
    
    winner = max(khanvotes, correyvotes, livotes, otooleyvotes)

    if winner == khanvotes:
        
        winner_name = "Khan"
    
    elif winner == correyvotes:
        
        winner_name = "Correy"
    
    elif winner == livotes:
    
        winner_name = "Li"
    
    else:
    
        winner_name = "O'Tooley" 


print(f"Election Results")

print(f"---------------------------")

print(f"Total Votes: {totalvotes}")

print(f"---------------------------")

print(f"Kahn: {kahnpercentage:.3%}({khanvotes})")

print(f"Correy: {correypercentage:.3%}({correyvotes})")

print(f"Li: {lipercentage:.3%}({livotes})")

print(f"O'Tooley: {otooleypercentage:.3%}({otooleyvotes})")

print(f"---------------------------")

print(f"Winner: {winner_name}")

print(f"---------------------------")


output_file = os.path.join('.', 'Resources', 'output.txt')


with open(output_file, 'w',) as newtextfile:

    newtextfile.write(f"Election Results\n")
    newtextfile.write(f"---------------------------\n")
    newtextfile.write(f"Total Votes: {totalvotes}\n")
    newtextfile.write(f"---------------------------\n")
    newtextfile.write(f"Kahn: {kahnpercentage:.3%}({khanvotes})\n")
    newtextfile.write(f"Correy: {correypercentage:.3%}({correyvotes})\n")
    newtextfile.write(f"Li: {lipercentage:.3%}({livotes})\n")
    newtextfile.write(f"O'Tooley: {otooleypercentage:.3%}({otooleyvotes})\n")
    newtextfile.write(f"---------------------------\n")
    newtextfile.write(f"Winner: {winner_name}\n")
    newtextfile.write(f"---------------------------\n")