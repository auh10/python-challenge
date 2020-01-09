#dependencies
import os, csv
#read data from file named "budget_data.csv" in folder named "Resources"
csv_path = os.path.join("../Resources/budget_data.csv")

#To Count months, previous revenue, and total revenue
total_months = 0
previous_revenue = 0
total_revenue = 0
#empty lists to be extracted from data file
months_of_change = []
revenue_change = []
#dictionaries to store increases and decreases to later find greatest increase and greatest decrease
increase = {}
decrease = {}
#greatest increase and greatest decrease
greatest_increase = {}
greatest_decrease = {}

#open and read in csv file, data separated by comma delimiter
with open(csv_path, newline='', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #loop through each row
    for row in csv_reader:
        #create a list of total months
        total_months.append(row[0])
        total_months = total_months + 1
        #create list for total revenue
        total_revenue = total_revenue.append(row[1])
        total_revenue = total_revenue + float(row[1])
        #revenue
        revenue = float(row[1])
        #previous_revenue
        previous_revenue = revenue - revenue_change
        #revenue change
        revenue_change = revenue - previous_revenue

        #add total months from row [0]
        #sum of revenue from first month to last month
        sum_revenue = sum(total_revenue('row[1]'))
        #average of monthly changes
        average_monthly_change = avg(float(revenue_change(row[1]))
        #locate month with greatest increase
        if row in revenue_changes is > 0:
            increase.append(row[1])
        else if row in revenue_changes is < 0:
            decrease.append(row[1])

        #put month of greatest increase into a variable
        greatest_increase_month = greatest_increase(float(row[1]))
        #locate month with greatest decrease and put into variable
        greatest_decrease_month = greatest_decrease(float(row[1]))
        #add for total revenue for whole year divided by the number of changes throughout the year period
        total_revenue = sum(total_revenue)/len(total_revenue)

output = (
    f"\nFinancial Analysis\n"
    f"-------------------------"
    f"Total Months: {total_months}\n"
    f"Total Revenue: {total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_deccrease[1]})\n"
)    

#print output to terminal

print(output)



#write cleaned data into CSV file

output_path = os.path.join("..", "output", "budget_analysis.csv")
with open(output_path, "w", newline='', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    