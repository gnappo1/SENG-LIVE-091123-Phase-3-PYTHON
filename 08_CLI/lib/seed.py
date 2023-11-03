# Feel free to use fake to generate seed data for your project, or create your own seed data.
# In addition you may also fire up a get request to an API or scrape a webpage to get seed data for your project.

from classes.doctor import Doctor
from classes.patient import Patient
from classes.appointment import Appointment
from random import sample
from faker import Faker
fake = Faker()

SPECIALTIES = [
    'Allergy and immunology',
    'Anesthesiology',
    'Dermatology',
    'Diagnostic radiology',
    'Emergency medicine',
    'Family medicine',
    'Internal medicine',
    'Medical genetics',
    'Neurology',
    'Nuclear medicine',
    'Obstetrics and gynecology',
    'Ophthalmology',
    'Pathology',
    'Pediatrics',
    'Physical medicine and rehabilitation',
    'Preventive medicine',
    'Psychiatry',
    'Radiation oncology',
    'Surgery',
    'Urology'
]

def drop_tables():
    #! Drop tables first to avoid errors and clear out old data
    Appointment.drop_table()
    Doctor.drop_table()
    Patient.drop_table()

def create_tables():
    #! Create tables brand new
    Doctor.create_table()
    Patient.create_table()
    Appointment.create_table()

def seed_tables():
    #! Create seed data
    for _ in range(50):
        try:
            Doctor.create(fake.name(), fake.phone_number(), sample(SPECIALTIES, 1)[0])
            Patient.create(fake.name(), fake.email(), fake.phone_number())
            print("Created doctor and patient")
        except Exception as e:
            print("Failed to create doctor or patient because of error: ", e)
            
    for _ in range(10):
        try:
            doctors = Doctor.get_all()
            patients = Patient.get_all()
            Appointment.create(
                fake.date(),
                fake.time(),
                fake.sentence(),
                sample(doctors, 1)[0].id,
                sample(patients, 1)[0].id
            )
            print("Created appointment")
        except Exception as e:
            print("Failed to create appointment because of error: ", e)

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
    import ipdb; ipdb.set_trace()