from classes.__init__ import CURSOR, CONN
import re
from datetime import datetime


class Appointment:
    all = {}

    def __init__(self, date, time, description, doctor_id, patient_id, id=None):
        self.date = date
        self.time = time
        self.description = description
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.id = id

    def __repr__(self):
        return (
            f"<Appointment {self.id}: {self.date} @{self.time}, "
            + f"{self.description}, "
            + f"Doctor ID: {self.doctor_id}, "
            + f"Patient ID: {self.patient_id}>"
        )

    #! Attributes and Properties

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, doctor_id):
        if not isinstance(doctor_id, int):
            raise TypeError("Doctor_id must be an integer")
        elif doctor_id < 1 or not Doctor.find_by_id(doctor_id):
            raise ValueError(
                "Doctor ID must be a positive integer and pointing to an existing doctor"
            )
        else:
            self._doctor_id = doctor_id

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        if not isinstance(patient_id, int):
            raise TypeError("Patient_id must be must be an integer")
        elif patient_id < 1 or not Patient.find_by_id(patient_id):
            raise ValueError(
                "Patient_id must be a positive integer and pointing to an existing patient"
            )
        else:
            self._patient_id = patient_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        elif not re.match(
            r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", date
        ):
            raise ValueError("Date must be in format MM/DD/YYYY")
        else:
            self._date = date

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        if not isinstance(time, str):
            raise TypeError("Time must be a string")
        elif not re.match(r"([0][0-9]|[1][0-2]):[0-5][0-9](AM|PM)", time):
            raise ValueError("Time must be in format HH:MMAM or HH:MMPM")
        else:
            self._time = time

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        elif len(description) < 3:
            raise ValueError("Description must be a string longer than 2 characters")
        else:
            self._description = description

    #! Association Methods

    def doctor(self):
        return Doctor.find_by_id(self.doctor_id) if self.doctor_id else None

    def patient(self):
        return Patient.find_by_id(self.patient_id) if self.patient_id else None

    #! Helper Methods
    def in_the_future(self, date):
        try:
            today = datetime.now()
            if int(date[-4:]) > today.year:
                return True
            if int(date[-4:]) != today.year:
                return False
            if int(date[:2]) > today.month:
                return True
            else:
                return int(date[:2]) == today.month and int(date[2:4]) > today.day
        except Exception as e:
            return f"Date is not in mm/dd/yyyy format or is in the past! {e}"

    #! Utility ORM Class Methods
    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                date TEXT,
                time TEXT,
                description TEXT,
                doctor_id INTEGER,
                patient_id INTEGER,
                FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE,
                FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
            );
        """
        )
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS appointments;
        """
        )
        CONN.commit()

    @classmethod
    def create(cls, date, time, description, doctor_id, patient_id):
        # Initialize a new obj with the info provided
        new_appt = cls(date, time, description, doctor_id, patient_id)
        # save the obj to make sure it's in the db
        new_appt.save()
        return new_appt

    @classmethod
    def new_from_db(cls):
        CURSOR.execute(
            """
            SELECT * FROM appointments
            ORDER BY id DESC
            LIMIT 1;
        """
        )
        row = CURSOR.fetchone()
        appt = cls(row[1], row[2], row[3], row[4], row[5], row[0])
        cls.all[appt.id] = appt
        return appt

    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
            SELECT * FROM appointments; 
        """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]

    @classmethod
    def find_by_date_and_time(cls, date, time):
        CURSOR.execute(
            """
            SELECT * FROM appointments
            WHERE date is ? AND time is ?;
        """,
            (date, time),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
            SELECT * FROM appointments
            WHERE id is ?;
        """,
            (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None

    @classmethod
    def find_or_create_by(cls, date, time, description, doctor_id, patient_id):
        return cls.find_by_date_and_time(date, time) or cls.create(
            date, time, description, doctor_id, patient_id
        )

    #! Utility ORM Instance Methods
    def update(self):
        CURSOR.execute(
            """
            UPDATE appointments
            SET date = ?, time = ?, description = ?, doctor_id = ?, patient_id = ?
            WHERE id = ?
        """,
            (
                self.date,
                self.time,
                self.description,
                self.doctor_id,
                self.patient_id,
                self.id,
            ),
        )
        CONN.commit()
        type(self).all[self.id] = self
        return self

    def save(self):
        # self is only instantiated so it has no id
        CURSOR.execute(
            """
            INSERT INTO appointments (date, time, description, doctor_id, patient_id)
            VALUES (?, ?, ?, ?, ?);
        """,
            (self.date, self.time, self.description, self.doctor_id, self.patient_id),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        return self

    def delete(self):
        CURSOR.execute(
            """
            DELETE FROM appointments
            WHERE id = ?;
        """,
            (self.id,),
        )
        CONN.commit()
        #! Remove memoized object
        del type(self).all[self.id]
        #! Nullify id
        self.id = None
        return self


from classes.doctor import Doctor
from classes.patient import Patient
