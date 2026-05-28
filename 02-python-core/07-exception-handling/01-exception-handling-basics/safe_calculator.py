try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", num1 + num2)
    print("Division:", num1 / num2)

except ZeroDivisionError:

    print("Denominator cannot be zero")

except ValueError:

    print("Please enter valid numbers")