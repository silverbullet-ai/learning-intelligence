# Write to file
with open("sample_files/example.txt", "w") as file:

    file.write("Hello World\n")
    file.write("Python File Handling")


# Read file
with open("sample_files/example.txt", "r") as file:

    content = file.read()

print(content)