# Accept total seconds and convert them into hours, minutes, and seconds.            

total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"""Hours: {hours}
Minutes: {minutes}
Seconds: {seconds}
      """)
