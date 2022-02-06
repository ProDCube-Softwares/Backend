import logging
from logging import getLogger

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


class ColoredFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt: str):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        logFmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(logFmt, datefmt="%H:%M %p")
        return formatter.format(record)


class CustomLogger:
    def __init__(self):
        stdoutHandler = logging.StreamHandler()
        stdoutHandler.setLevel(logging.INFO)
        stdoutHandler.setFormatter(
            ColoredFormatter("%(levelname)s | %(asctime)s | %(message)s"))
        self.customLogger = getLogger(__name__)
        self.customLogger.setLevel(logging.INFO)
        self.customLogger.addHandler(stdoutHandler)

    def info(self, message: str, functionName: str, fileName: str):
        self.customLogger.info("FileName: %s | FunctionName: %s | Message: %s", fileName, functionName, message)

    def warning(self, message: str, functionName: str, fileName: str):
        self.customLogger.warning("FileName: %s | FunctionName: %s | Message: %s", fileName, functionName, message)

    def error(self, message: str, functionName: str, fileName: str):
        self.customLogger.error("FileName: %s | FunctionName: %s | Message: %s", fileName, functionName, message)

    def critical(self, message: str, functionName: str, fileName: str):
        self.customLogger.critical("FileName: %s | FunctionName: %s | Message: %s", fileName, functionName, message)


logger = CustomLogger()
