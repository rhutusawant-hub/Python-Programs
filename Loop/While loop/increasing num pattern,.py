# Q5. Increasing Number Pattern
# Print the following pattern:
# 1
# 12
# 123
# 1234
# 12345

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(f"{j}", end="")
        j = j + 1

    print()
    i = i + 1