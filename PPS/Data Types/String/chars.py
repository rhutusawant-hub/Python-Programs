# Accept a string and display its first character, last character, and middle character.

text = input("Enter a string: ")

first = text[0]
last = text[-1]
middle = text[len(text) // 2]

print(f"""
First Character: {first}
Last Character: {last}
Middle Character: {middle}
""")