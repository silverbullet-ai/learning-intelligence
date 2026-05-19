# Write binary data
with open("sample_files/example.bin", "wb") as file:

    file.write(b"Hello Binary World")


# Read binary data
with open("sample_files/example.bin", "rb") as file:

    content = file.read()

print(content)