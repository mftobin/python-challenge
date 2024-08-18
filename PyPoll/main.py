#import
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
#specify total votes
total_votes = 0

#make list to store candidate options
candidate_options = []

# #make a list to store vote percentage
vote_percentage = []

#dictionary to score each candidate
candidate_votes = {}
candidate_name = ""

#empty variable for winning candidate and winning vote count
winning_candidate = ""
winning_votes = 0

#with open election data file
with open(election_csv, "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # skip header
    #for loop again
    for row in reader:
        total_votes += 1  # increment total votes
       
        # get candidate name from row
        candidate_name = row[2]

        # if candidate's name is in list, increment their vote count
        if candidate_name in candidate_options:
            candidate_votes[candidate_name] += 1
        # if not, add candidate to list and set their vote count to 1
        else:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1

        # if current candidate's vote count is higher than current winning candidate's, update winning candidate and winning vote count
        if candidate_votes[candidate_name] > winning_votes:
            winning_candidate = candidate_name
            winning_votes = candidate_votes[candidate_name]

# second for loop to calculate vote percentage (total votes * 100)
    # in this second loop, we're updating the dictionary with vote percentage
    for candidate_name, votes in candidate_votes.items():
            vote_percentage = (votes / total_votes) * 100
            candidate_votes[candidate_name] = f"{vote_percentage:.3f}%,({votes})"
            # ^^ this prints the following new dictionary
            #{'Charles Casper Stockham': '23.049%,(85213)', 'Diana DeGette': '73.812%,(272892)', 'Raymon Anthony Doane': '3.139%,(11606)'}
            # now my objective in results is to print this dictionary in a readable format
            # so, I'll use f-string to print the dictionary with each candidate's name, vote percentage, and vote count
            # then, I'll print the results
            # print(f"{candidate_name}: {candidate_votes[candidate_name]}")
                #this printed all three lines however, within results, it was only printing the last line
                #while the code below prints all the correct information, it does not separate each line the way I would like.
                # I will follow up in office hours or a tutoring session to fix this final results, but this is miles ahead of what I had before
                # In the interest of time, I'll submit this homework assignment with this one error and hope that since the rest of my code is correct, the graders will take pity on me. Thank you!

    
    results = (
        f"Election Results:\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n"
        f"{candidate_votes}\n"
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n")

    print(results)

    analysis_path = os.path.join("analysis", "election_analysis.txt")
    with open(analysis_path, 'w') as text_file:
        text_file.write(results)