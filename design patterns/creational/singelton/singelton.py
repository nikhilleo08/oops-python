from abc import ABC, abstractmethod
import json

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Console] {message}")


class JSONLogger(Logger):
    def log(self, message):
        json_message = json.dumps({"log": message})
        print(f"[JSON] {json_message}")


class FileLogger(Logger):
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, message):
        with open(self.file_name, "a") as file:
            file.write(f"{message}\n")

class LoggerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.logger = None
        return cls._instance

    def set_logger(self, logger: Logger):
        self.logger = logger

    def log(self, message):
        if not self.logger:
            raise ValueError("Logger is not set!")
        self.logger.log(message)

class CompositeLogger(Logger):
    def __init__(self, *loggers):
        self.loggers = loggers

    def log(self, message):
        for logger in self.loggers:
            logger.log(message)

# Client Code
manager = LoggerManager()

# Use Console Logger
console_logger = ConsoleLogger()
manager.set_logger(console_logger)
manager.log("This is a console log message.")

# Switch to JSON Logger
json_logger = JSONLogger()
manager.set_logger(json_logger)
manager.log("This is a JSON log message.")

# Switch to File Logger
file_logger = FileLogger("logs.txt")
manager.set_logger(file_logger)
manager.log("This log message is saved to a file.")

# Switch to Composite Logger
composite_logger = CompositeLogger(ConsoleLogger(), FileLogger("logs.txt"))
manager.set_logger(composite_logger)
manager.log("This message is logged to both console and file.")


# The implementation of LoggerManager follows the Singleton pattern by ensuring that there is only one instance of the manager throughout the application. However, the individual logger implementations (e.g., ConsoleLogger, JSONLogger, and FileLogger) are not Singletons. This is intentional because:

# LoggerManager as a Singleton:

# Ensures a single global point of control for logging.
# Maintains consistency by managing the active logging behavior (e.g., which logger is being used).
# Loggers Not as Singletons:

# Each logger is designed to encapsulate specific behavior (e.g., logging to a file, JSON formatting).
# Keeping them as regular classes allows flexibility, such as having multiple file loggers for different files or multiple composite loggers.

# Why This is a Good Design

# 1. Combining Singleton and SOLID:
#   - LoggerManager is a Singleton to ensure centralized control.
#   - Loggers are not Singletons because they adhere to the Single Responsibility Principle and Open/Closed Principle.

# 2. Flexibility:
#   - You can add or switch between different loggers dynamically without modifying LoggerManager or the logger implementations.

# 3. No Tight Coupling:
#   - The LoggerManager depends on the Logger interface, not specific implementations, ensuring adherence to the Dependency Inversion Principle.
