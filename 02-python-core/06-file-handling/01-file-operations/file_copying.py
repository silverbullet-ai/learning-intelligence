# Copy file content

with open("sample_files/source.txt", "r") as source_file:

    content = source_file.read()

with open("sample_files/destination.txt", "w") as destination_file:

    destination_file.write(content)

print("File copied successfully")