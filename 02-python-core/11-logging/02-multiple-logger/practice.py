import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

student_logger = logging.getLogger(
    "student"
)

teacher_logger = logging.getLogger(
    "teacher"
)

student_logger.info(
    "Student logged in"
)

teacher_logger.info(
    "Teacher uploaded assignment"
)