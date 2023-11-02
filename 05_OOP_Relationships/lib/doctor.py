

class Doctor:
    all = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all.append(self)
    #! direct ownership
    def appointments(self):
        from .appointment import Appointment
        return [appt for appt in Appointment.all if appt.doctor is self]
    
    def patients(self):
        return list({appt.patient for appt in self.appointments()})

    #! indirect ownership