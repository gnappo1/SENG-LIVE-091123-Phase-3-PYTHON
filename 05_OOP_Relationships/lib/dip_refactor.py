from abc import ABC, abstractmethod

class LogWriter(ABC):
    @abstractmethod
    def write(self, message):
        pass

class FileWriter(LogWriter):
    def write(self, message):
        with open("log.txt", "a") as file:
            file.write(message + "\n")

class Logger:
    def __init__(self, writer):
        self.writer = writer

    def log(self, message):
        self.writer.write(message)

# Usage
file_writer = FileWriter()
logger = Logger(file_writer)
logger.log("This is a log message.")
