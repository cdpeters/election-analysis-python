# **Automating an Election Audit with Python**

## **Overview of Project**
Elections, especially on a national level, naturally produce large data sets
that require the use of automated programs for auditing the results. The
purpose of this project is to produce an election audit for a 2018 U.S. House
of Representatives election in Colorado as a case study in how to automate an
analysis. The goal is to produce a flexible python script that could be adapted
to analyze new data sets of a similar structure in future elections. The audit
results will include the vote counts for each candidate as well as voter
turnout numbers for each county. Output also contains a declaration of the
winner of the election, along with the county that had the largest voter
turnout. The raw data is contained in
[election_results.csv](/resources/election_results.csv), which can be found in
the resources folder.

## **Analysis and Results**
The analysis is carried out in the python script ```PyPoll.py``` which is
roughly split into two parts:
1. Initialization and Reading Input Data
1. Writing Output Data

### **Initialization and Reading Input Data**
The initialization portion included creating variables to hold file paths along
with other variables necessary for holding candidate and county information.
Candidates, counties, and vote totals were appended and incremented as
necessary (via conditional statements) all within a ```with``` block to ensure
appropriate file handling. This section only contains hard coded information in
two locations outside of the specific file paths:
```python
candidate_name = row[2]
county_name = row[1]
```
In the future, these values can be abstracted away into variables to allow
more flexibility if the structure of the raw data file changes.

### **Writing Output Data**
Once the names and counts were gathered, another ```with``` block was used for
analysis, formatting, and writing to the output file. Two ```for``` loops then
cycle through each county and candidate to calculate the vote percentages with
the line:
```python
vote_percentage = (votes / float(total_votes)) * 100
```
Notice the type conversion of ```total_votes``` to a ```float```. This is to
ensure the division always results in a ```float``` in case other versions of
python are used.

To capture the largest county and winning candidate information, the following
conditional is evaluated at each iteration to see if the appropriate variables
need to be updated. The conditionals shown are found in separate ```for```
loops within the script, but are shown together for conciseness (the code that
is in between is implied by the ellipsis):
```python
if (votes > largest_turnout_count):
    largest_turnout_count = votes
    largest_turnout_county = county_name
...
if (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage
```

Results, shown in the following section, were then formatted and printed to the
terminal as well as to the output file
[election_analysis.txt](/analysis/election_analysis.txt) found in the analysis
folder.

### **Results**
The data presented is the terminal output that the script produces. Here are
the main results of the audit:
* The total number of votes cast in the election:
```
Election Results
-------------------------
Total Votes: 369,711
-------------------------
```

* The following contains a breakdown of the voting turnout by county (vote
count in parentheses):
```
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
```

* Thus, the largest voter turnout by county is Denver with 306,055 votes cast:
```
-------------------------
Largest County Turnout: Denver
-------------------------
```

* The breakdown of votes for each candidate is as shown (vote count in
parentheses):
```
Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)
```

* Thus, the winner of the election is Diana DeGette with 73.8% of the total
vote:
```
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
```

## **Summary**
The script provided can be used with any election data that follows the same
format as the raw CSV file, where county and candidate name are the second and
third values in each row respectively. One way in which the script can be
restructured to add flexibility is to recast the entire script as a function.
The inputs to the function can contain information about the structure of the
raw data file to be read. This would allow election commissions to analyze raw
data files that are different in structure with the same script as long as the
structure is specified in the arguments to the function. Something similar to:
```python
def election_audit(filepath, county_index, candidate_index)
```
Here ```county_index``` and ```candidate_index``` would contain the value of
the index where those respective names can be found within a row. These indices
would be used in place of the hard coded values mentioned in the
**Initialization and Reading Input Data** section. Additional parameters can be
included as needed.

Another modification that can be made is to add the ability to interact with
the folder structure of the operating system. Combine this with a loop over a
folder that holds many election data files and you can produce an output audit
file with results for each election in the folder. This would allow for all
elections under that commission to be analyzed with one script, provided the
raw data files have the same structure as implemented here. These are just two
modifications among many that show how powerful automating scripts can be.