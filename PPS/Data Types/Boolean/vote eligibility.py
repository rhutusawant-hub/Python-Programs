# Accept a person's age and create a Boolean value indicating whether the person is eligible to vote.

age = int(input("Enter age: "))

eligible = age >= 18

print(f"Eligible to vote: {eligible}")