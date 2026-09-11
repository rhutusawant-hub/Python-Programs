# Q4. Number Grid
# Print the following pattern:
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

i = 1

while i <= 4:
    j = 1

    while j <= 4:
        print(f"{j}", end=" ")
        j = j + 1

    print()
    i = i + 1