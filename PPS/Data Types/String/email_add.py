# Accept an email address and display the username and domain separately.

email = input("Enter email address: ")

diff = email.index("@")
username = email[:diff]
domain = email[diff +1:]

print(f"""
Username: {username}
Domain: {domain}
""")