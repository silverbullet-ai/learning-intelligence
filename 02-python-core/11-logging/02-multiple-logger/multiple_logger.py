import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

logger1.debug(
    "This is a debug message for module1"
)

logger2.warning(
    "This is a warning message for module2"
)

logger2.error(
    "This is an error message for module2"
)