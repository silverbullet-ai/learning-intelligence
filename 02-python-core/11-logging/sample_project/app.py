from logger_config import logger

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and {b}, the sum is {result}")
    return result

def substract(a,b):
    result = a - b
    logger.debug(f"Substracting {a} from {b}, the difference is {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} by {b}, the product is {result}")

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b}, the quotient is {result}")
    except ZeroDivisionError:
        logger.error('Division by Zero(0) error.')
        return None

add(10,15)
substract(15,10)
multiply(10,5)
divide(15,3)
divide(10,0)