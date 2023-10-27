from datetime import datetime
class Patient:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
