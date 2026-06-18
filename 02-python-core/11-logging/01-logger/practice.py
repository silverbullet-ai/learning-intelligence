import logging

logging.basicConfig(
    filename="../logs/calculator.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def multiply(a, b):
    result = a * b
    logging.info(f"Multiplication: {a} * {b} = {result}")
    return result

print(multiply(5, 10))