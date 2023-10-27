class FileWriter:
    def write(self, message):
        with open("log.txt", "a") as file:
            file.write(message + "\n")

class Logger:
    def __init__(self):
        self.writer = FileWriter()

    def log(self, message):
        self.writer.write(message)

# Usage
logger = Logger()
logger.log("This is a log message.")
