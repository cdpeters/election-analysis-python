import csv
import os
# Path of file to read from
file_to_load = os.path.join("resources", "election_results.csv")
# Path of file to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

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
