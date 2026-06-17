from logger_config import logger


def add(a, b):
    logger.debug(
        f"Adding {a} and {b}"
    )
    return a + b


result = add(10, 20)

logger.info(
    f"Result = {result}"
)