# 12. Accept minutes and convert them into hours and remaining minutes.

minutes = int(input("Enter total minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes will be {hours}hours and {remaining_minutes} minutes")
