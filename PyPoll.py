import csv
import os
# Path of file to read from
file_to_load = os.path.join("resources", "election_results.csv")
# Path of file to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_options:
    votes = candidate_votes[candidate_name]
    vote_percentage = (float(votes) / float(total_votes)) * 100

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------\n"
)

print(winning_candidate_summary)

    # 1. Total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The precentage of votes each candidate won
    # 4. Total number of votes each candidate won
    # 5. Winner of the election based on popular vote

# Writing to a file
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
