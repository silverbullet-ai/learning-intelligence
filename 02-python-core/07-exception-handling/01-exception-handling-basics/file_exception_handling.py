try:

    file = open("sample.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:

    print("File does not exist")

finally:

    if 'file' in locals() and not file.closed:

        file.close()

        print("File closed")