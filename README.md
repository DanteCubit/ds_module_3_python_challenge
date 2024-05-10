# ds_module_3_python_challenge
Homework for Week 3 of Data Science Boot Camp

During this challenge, I was tasked with assisting a small, rural town in modernizing its vote-counting process, as well as creating a Python script to analyze the financial records of our company.

For the voting data analysis, I utilized a dataset named election_data.csv, which consisted of three columns: "Voter ID", "County", and "Candidate". My objective was to develop a Python script to analyze the votes and calculate the following:

The total number of votes cast: This involved iterating through all rows in the dataset, excluding the header, to count the votes.
A comprehensive list of candidates who received votes: This was achieved by iterating through the same loop, creating a dictionary of all candidates who received votes while also tallying their total number of individual votes.
The percentage of votes each candidate won: This was accomplished through a straightforward percentage conversion.
Determining the winner of the election based on the popular vote: The script identified the candidate with the highest vote count.
The script was programmed to display the results and simultaneously save them to a .txt file.

For the company's financial records, I was tasked with creating a Python script to analyze a dataset named budget_data.csv, consisting of two columns: "Date" and "Profit/Losses".

The tasks included:

Providing the total number of months included in the dataset: This was achieved by iterating through the rows after the header while also calculating the net total amount of "Profit/Losses" over the entire period.
Generating the changes in "Profit/Losses" over the entire period and calculating the average of those changes.
Identifying the greatest increase and decrease in profits (including the date and amount) over the entire period.
Similar to the voting data analysis, the financial analysis results were displayed and saved to a .txt file.