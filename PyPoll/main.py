import os

import csv

Candidate_votes = {}

Ballot = []

Charles_Casper_Stockham = 0
Raymon_Anthony_Doane = 0
Diana_DeGette = 0

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for csvrow in csvreader:
        Ballot.append(csvrow[1])
        votes= len(Ballot)

        if csvrow [2] == "Charles Casper Stockham":
            Charles_Casper_Stockham += 1
        
        elif csvrow[2] == "Diana DeGette":
            Diana_DeGette += 1
        
        elif csvrow[2] == "Raymond_Anthony_Doane":
            Raymon_Anthony_Doane += 1
        

    Candidate1 = round((Charles_Casper_Stockham/votes) *100,3)
    Candidate2 = round((Diana_DeGette/votes) *100,3)
    Candidate3 = round((Raymon_Anthony_Doane/votes) *100,3)

    Candidate_votes = {"Charles Casper Stockham": Charles_Casper_Stockham,"Diana DeGette": Diana_DeGette, "Raymon Anthony Doane": Raymon_Anthony_Doane }

    Election_winner = max (Candidate_votes, key=Candidate_votes.get)

    outputh_path = ("Election_result.txt")

    file = open(outputh_path, 'w')

    file.write ("Election Results\n")
    file.write ("-----------------------\n")
    file.write (f"Total Votes: {votes}\n")
    file.write ("---------------------------\n")
    file.write (f"Charles Casper Stockham: {Candidate1}% ({Charles_Casper_Stockham})\n")
    file.write (f"Diana DeGette: {Candidate2}% ({Diana_DeGette})\n")
    file.write (f"Raymon Anthony Doane: {Candidate3}% ({Raymon_Anthony_Doane})\n")
    file.write ("--------------------\n")
    file.write(f"Winner: {Election_winner}\n")

    file.close()
    

