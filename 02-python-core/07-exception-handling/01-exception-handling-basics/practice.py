try:

    number = int(input("Enter a number: "))

    result = 10 / number

    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero")

except ValueError:

    print("Invalid input")

finally:

    print("Execution completed")