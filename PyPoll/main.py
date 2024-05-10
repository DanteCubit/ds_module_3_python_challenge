#Tutor was helpful in refactoring code
#import os and csv
import os
import csv

#variable list
csvpath = "PyPoll/Resources/election_data.csv"
output_file="PyPoll/Analysis/results.txt"
total_votes =  0
candidate_options = []
candidate_votes = { }
winning_count = 0
winner = ""

#Open csv and read header
with open(csvpath, encoding='UTF-8') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
#loop for candidates and votes   
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#determine total votes
with open(output_file, "w") as txt_file:
    election_results = ( 
        f"Election Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------------\n")
    print(election_results)

#determine candidate votes and percentages  
    txt_file.write(election_results)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        txt_file.write(voter_output)
    
#determine winner  
    winnning_candidate_summary = (
        f"-------------------\n"
        f"Winner: {winner}\n"
        f"------------------\n")

#print and save   
    print(winnning_candidate_summary)
    txt_file.write(winnning_candidate_summary)