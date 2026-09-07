# Accept an integer representing the number of seconds and convert it into minutes and remaining seconds.

total_seconds = int(input("Enter total seconds: "))

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"Minutes: {minutes}")
print(f"Remaining Seconds: {remaining_seconds}")