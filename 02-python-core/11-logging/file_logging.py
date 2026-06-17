import logging

logging.basicConfig(
    filename="logs/file.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Database connection failed")