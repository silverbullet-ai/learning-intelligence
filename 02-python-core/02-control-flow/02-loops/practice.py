# Multiplication table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Factorial
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)


# Fibonacci
n = int(input("Enter number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b