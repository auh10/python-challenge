#dependencies
import os
import csv

#file path from csv
file = os.path.join("Resources/election_data.csv")

# #empty lists to collect data 
# * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
total_votes = 0
candidates = []
total_votes_winner = 0
correy_votes = 0
khan_votes = 0
otooley_votes = 0
li_votes = 0

#use with open
with open(file, newline="", encoding='utf-8') as votes:
    reader = csv.reader(votes)

    # Assign header data to a list
    header = next(reader)

    # Set variables to avoid calculating header row
    first_row = next(reader)
    total_votes += 1
   
    #total months method to calculate total months and net gain
    for row in reader:
        #Calculate Total Votes
        total_votes += 1
        candidate = row[2]
        #Populate candidates list with unique candidates only
        if candidate not in candidates:
            candidates.append(row[2])
        #Calculate total votes per unique candidate    
        if candidate == "Correy":
            correy_votes += 1
        if candidate == "Khan":
            khan_votes += 1
        if candidate == "O'Tooley":
            otooley_votes += 1
        if candidate == "Li":
            li_votes += 1
        #find which candidate is greatest
        # if(round(int(correy_votes))) > (round(int(khan_votes))):

    #Determine the % of the votes
    khan_percent = round(int(khan_votes)/ int(total_votes), 2) * 100
    correy_percent = round(int(correy_votes)/ int(total_votes), 2) * 100
    li_percent = round(int(li_votes)/ int(total_votes), 2) * 100
    otooley_percent = round(int(otooley_votes)/ int(total_votes), 2) * 100

    #   candidates_with_votes += row[2]
    print ("Election Results")
    print (f"-" * 12)
    print (f"Total Votes: {total_votes}")
    print (f"-" * 12)
    print (f"{candidates[0]}: {khan_percent:.3f}% ({khan_votes})")
    print (f"{candidates[1]}: {correy_percent:.3f}% ({correy_votes})")
    print (f"{candidates[2]}: {li_percent:.3f}% ({li_votes})")
    print (f"{candidates[3]}: {otooley_percent:.3f}% ({otooley_votes})")
    print ("-" * 12)

    print ("-" * 12)

