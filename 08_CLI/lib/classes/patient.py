from classes.__init__ import CURSOR, CONN
import re


class Patient:
    all = {}

    def __init__(self, full_name, email, phone, id=None):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.id = id

    def __repr__(self):
        return f"<Patient {self.id}: {self.full_name}, {self.email}, {self.phone}>"

    #! Attributes and Properties

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        if not isinstance(full_name, str):
            raise TypeError("Full name must be a string")
        elif not re.match(r"^[a-zA-Z]+ [a-zA-Z]+$", full_name):
            raise ValueError(
                "Full name cannot be empty and must contain two words separated by a space"
            )
        else:
            self._full_name = full_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        elif not re.match(r"^\w+@\w+\.\w+$", email):
            raise ValueError("Email must be in format: yourcompany@domain.com")
        else:
            self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone must be a string")
        elif not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            raise ValueError("Phone must be in format: 123-456-7890")
        else:
            self._phone = phone

    #! Association Methods

    def appointments(self):
        CURSOR.execute(
            """
            SELECT * FROM appointments
            WHERE patient_id = ?
        """,
            (self.id,),
        )
        rows = CONN.fetchall()
        return [
            Appointment(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows
        ]

    def doctors(self):
        return list({appt.doctor for appt in self.appointments()})

    #! Helper Methods

    #! Utility ORM Class Methods

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                full_name TEXT,
                email TEXT,
                phone_number TEXT
            );
        """
        )
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS patients;
        """
        )
        CONN.commit()

    @classmethod
    def create(cls, full_name, email, phone):
        # Initialize a new obj with the info provided
        new_doctor = cls(full_name, email, phone)
        # save the obj to make sure it's in the db
        new_doctor.save()
        return new_doctor

    @classmethod
    def new_from_db(cls):
        CURSOR.execute(
            """
            SELECT * FROM patients
            ORDER BY id DESC
            LIMIT 1;
        """
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0])

    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
                SELECT * FROM patients; 
            """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute(
            """
            SELECT * FROM patients
            WHERE full_name is ?;
        """,
            (name,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
            SELECT * FROM patients
            WHERE id is ?;
        """,
            (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def find_or_create_by(cls, full_name, email, phone):
        return cls.find_by_name(full_name) or cls.create(full_name, email, phone)

    #! Utility ORM Instance Methods

    def save(self):
        # self is only instantiated so it has no id
        CURSOR.execute(
            """
            INSERT INTO patients (full_name, email, phone_number)
            VALUES (?, ?, ?);
        """,
            (self.full_name, self.email, self.phone),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        return self

    def update(self):
        CURSOR.execute(
            """
            UPDATE patients
            SET full_name = ?, email = ?, phone_number = ?
            WHERE id = ?
        """,
            (self.full_name, self.email, self.phone, self.id),
        )
        CONN.commit()
        type(self).all[self] = self
        return self

    def delete(self):
        CURSOR.execute(
            """
            DELETE FROM patients
            WHERE id = ?
        """,
            (self.id,),
        )
        CONN.commit()
        #! Remove memoized object
        del type(self).all[self.id]
        #! Nullify id
        self.id = None
        return self


from classes.appointment import Appointment
