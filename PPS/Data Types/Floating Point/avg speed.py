# Accept distance and time as decimal values and calculate the average speed.

distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

average_speed = distance / time

print(f"Average Speed: {average_speed:.2f}")