# Write a Python program to analyze the runs scored by a batsman in different matches.  
# Tasks to Perform:

# Accept runs scored in different matches using eval().
runs = eval(input("Enter the runs scored in different matches (as a list): "))

# Display all scores.
print(f"All scores: {runs}")

# Display the first and last match scores.
print(f"First match score: {runs[0]}")
print(f"Last match score: {runs[-1]}")

# Display scores of the first five matches.
print(f"Scores of the first five matches: {runs[:5]}")

# Display scores of the last four matches.
print(f"Scores of the last four matches: {runs[-4:]}")

# Display scores of alternate matches.
print(f"Scores of alternate matches: {runs[::2]}")

# Check whether the batsman has scored a century (100 runs).
print(f"Has the batsman scored a century? {100 in runs}")

# Add the score of the latest match.
runs.append(int(input("Enter the score of the latest match: ")))
print(f"Updated scores after adding the score of the latest match: {runs}")

# Insert a missed match score at a specified position.
position = int(input("Enter the position to insert the missed match score: "))
missed_score = int(input("Enter the missed match score: "))
runs.insert(position, missed_score)
print(f"Updated scores after inserting the missed match score: {runs}")

# Remove the lowest score.
runs.remove(min(runs))
print(f"Updated scores after removing the lowest score: {runs}")

# Sort the scores.
runs.sort()
print(f"Updated scores after sorting: {runs}")

# Reverse the scores.
runs.reverse()
print(f"Updated scores after reversing: {runs}")

# Display the highest score, lowest score, total runs, and average runs.
print(f"Highest score: {max(runs)}")
print(f"Lowest score: {min(runs)}")
print(f"Total runs: {sum(runs)}")
print(f"Average runs: {sum(runs)/len(runs)}")

# Count the number of half-centuries (50 runs) entered by the user.
half_centuries = runs.count(50)
print(f"Number of half-centuries (50 runs): {half_centuries}")

# Display the updated score list.
print(f"Final updated scores: {runs}")