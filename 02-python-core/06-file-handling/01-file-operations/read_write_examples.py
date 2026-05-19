# Append example
with open("sample_files/example.txt", "a") as file:

    file.write("\nAppending new line")


# Read line by line
with open("sample_files/example.txt", "r") as file:

    for line in file:
        print(line.strip())