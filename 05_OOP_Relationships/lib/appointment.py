from datetime import datetime
from .patient import Patient
from .doctor import Doctor

class Appointment:
    all = []

    def __init__(self, reason_for_visit, date, doctor, patient):
        self.reason_for_visit = reason_for_visit
        self.date = date
        self.doctor = doctor
        self.patient = patient
        type(self).all.append(self)

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, new_doc):
        if not isinstance(new_doc, Doctor):
            raise TypeError("Doctor must be of type Doctor")
        else:
            self._doctor = new_doc
    @property
    def patient(self):
        return self._patient
    @patient.setter
    def patient(self, new_patient):
        if not isinstance(new_patient, Patient):
            raise TypeError("Patient must be of type patient")
        else:
            self._patient = new_patient
            
    @classmethod
    def sorted_appointments(cls):
        return sorted(cls.all, key=lambda appt: datetime.strptime(appt.date, "%m/%d/%y"))
