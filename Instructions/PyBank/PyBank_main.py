#import dependencies
import csv
import os

# Files to load and output 
file = os.path.join("Resources/budget_data.csv")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file, newline = '') as financial_data:
    reader = csv.reader(financial_data)

    # Assign header data to a list
    header = next(reader)

    # Set variables to avoid calculating header row
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_delta = int(first_row[1])


    #total months method to calculate total months and net gain
    for row in reader:
      total_months += 1
      total_net += int(row[1])

    #calculate total profit in between months
      delta = int(row[1]) - previous_delta
      previous_delta = int(row[1])
      #net_change_list = net_change_list + [delta]
      net_change_list += [delta]
      month_of_change += [row[0]]
    print (net_change_list)
    print (month_of_change)

    max_val = max(net_change_list)
    min_val = min(net_change_list)
    max_position = net_change_list.index(max_val)
    min_position = net_change_list.index(min_val)
    total_net_avg = sum(net_change_list)/len(net_change_list)

    print (max_val)
    print (min_val)
    print (max_position)
    print (min_position)
    print (month_of_change[24])
    print (month_of_change[43])
    print (total_net_avg)

#print into terminal with f-strings    
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: {total_net}\n"
    f"Average Revenue Change: ${total_net_avg}\n"
    f"Greatest Increase in Revenue: {month_of_change[24]} (${max_val})\n"
    f"Greatest Decrease in Revenue: {month_of_change[43]} (${min_val})\n"
)    

#print output to terminal
print(output)

#write cleaned data into CSV file
output_path = os.path.join("output/budget_final.csv")
with open(output_path, "w", newline='', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    