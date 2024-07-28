import logging
import logging.handlers
import os
from datetime import datetime


class Logger:
    """
    A utility class for handling logging across an application. This class
        encapsules Python's logging setup and configures a file handler to
        automatically rotate logs daily with a backup of the last X days.

    Attributes:
        name (str): The nameof the logger, typically the module's __name__.
        log_dir (str): The directory where the log files will be stored.
            Defaults to "logs".
        level (logging.Level): The logging level threshold. Defaults to
            logging.INFO.
        rotate_logs (int): The number of days' backup to be kept. Defaults to
            30.

    Methods:
        get_logger: Returns the logger instance.
    """

    def __init__(
        self, name, log_dir="logs", level=logging.INFO, rotate_logs=30
    ):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        date_today = datetime.now().strftime("%Y_%m_%d")
        log_file_path = os.path.join(log_dir, f"{name}_{date_today}.log")

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s - "
            + "%(funcName)s - %(lineno)d"
        )

        file_handler = logging.handlers.TimedRotatingFileHandler(
            log_file_path,
            when="D",
            interval=1,
            backupCount=rotate_logs,
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """
        Returns the configured logger instance.

        Returns:
            logging.Logger: The configured logger instance with file hander.
        """
        return self.logger
