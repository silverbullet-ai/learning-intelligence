import logging

logging.basicConfig(
    filename="logs/project.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

def add(a, b):
    logging.debug("Performing addition")
    return a + b

result = add(10, 20)

logging.info(f"Result: {result}")