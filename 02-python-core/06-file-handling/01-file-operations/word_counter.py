with open("sample_files/example.txt", "r") as file:

    content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)