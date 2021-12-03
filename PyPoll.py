import csv
import os
# Path of file to read from
file_to_load = os.path.join("resources", "election_results.csv")
# Path of file to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Total votes for entire election
total_votes = 0

# Candidates and their votes cast
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
# Counties and their votes cast
county_options = []
county_votes = {}

# Winning candidate and their vote count/percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# Largest turnout county and their vote count
largest_turnout_county = ""
largest_turnout_count = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    for county_name in county_options:
        votes = county_votes[county_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100

        county_results = (
            f"{county_name}: {vote_percentage:.1f}% "
            f"({votes:,})\n"
        )
        print(county_results)
        txt_file.write(county_results)

        if (votes > largest_turnout_count):
            largest_turnout_count = votes
            largest_turnout_county = county_name

    largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n"
    )
    print(largest_turnout_summary)
    txt_file.write(largest_turnout_summary)

#------------------------------------------------------------------------------

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% "
            f"({votes:,})\n"
        )
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
