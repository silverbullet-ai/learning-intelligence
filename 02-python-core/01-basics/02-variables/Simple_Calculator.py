num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
	quotient = num1 / num2

print('Sum:', sum)
print('Difference:', difference)
print('Product:', product)
if num2 != 0:
	print('Quotient:', quotient)
else:
    print("Division by zero not allowed")
