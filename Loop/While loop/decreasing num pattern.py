# Q6. Decreasing Number Pattern
# Print the following pattern:
# 12345
# 1234
# 123
# 12
# 1

i = 5

while i >= 1:
    j = 1

    while j <= i:
        print(f"{j}", end="")
        j = j + 1

    print()
    i = i - 1