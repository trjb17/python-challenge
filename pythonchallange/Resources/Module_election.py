# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file and store the data
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        # Count total votes
        total_votes += 1
        # Extract candidate name
        candidate = row[2]
        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

# Calculate the percentage of votes for each candidate
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")