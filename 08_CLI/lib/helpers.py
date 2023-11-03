import re


def welcome():
    print("Welcome to the Python CLI Project Template!")


def menu():
    print("Please select a group of options:")
    print()
    print("1. List all doctors")
    print("2. List all patients")
    print("3. List all appointments")
    print("4. Find a doctor by name")
    print("5. Find a patient by name")
    print("6. Find an appointment by date and time")
    print("7. Create a new doctor")
    print("8. Create a new patient")
    print("9. Create a new appointment")
    print("10. Update a doctor")
    print("11. Update a patient")
    print("12. Update an appointment")
    print("13. Delete a doctor")
    print("14. Delete a patient")
    print("15. Delete an appointment")
    print("16. Find patients by doctor name")
    print("17. Exit")


def list_doctors():
    doctors = Doctor.get_all()
    if doctors:
        for doctor in doctors:
            print(doctor)
    else:
        print(
            "I am sorry we underwent severe budget cuts and we no longer have doctors on payroll"
        )


def list_patients():
    patients = Patient.get_all()
    if patients:
        for patient in patients:
            print(patient)
    else:
        print("I am sorry, it looks like we have no patients in our system")


def list_appointments():
    appointments = Appointment.get_all()
    if appointments:
        for appointment in appointments:
            print(appointment)
    else:
        print("I am sorry, it looks like we have no appointments in our system")


def find_doctor_by_name():
    name = input("Enter the doctor's name: ")
    if len(name.strip()) and re.match(r"^[a-zA-Z ]+$", name) and name.title():
        doctor = Doctor.find_by_name(name.title())
        print(doctor) if doctor else print("No doctor found")
    else:
        print("Invalid name")


def find_patient_by_name():
    name = input("Enter the patient's name: ")
    if (
        isinstance(name, str)
        and name.strip()
        and re.match(r"^[a-zA-Z ]+$", name)
        and name.title()
    ):
        patient = Patient.find_by_name(name.title())
        print(patient) if patient else print("No patient found")
    else:
        print("Invalid name")


def find_appointment_by_date_and_time():
    date = input("Enter the appointment date (MM/DD/YYYY): ")
    time = input("Enter the appointment time (HH:MMAM or HH:MMPM): ")
    if isinstance(date, str) and isinstance(time, str) and len(date) and len(time):
        appointment = Appointment.find_by_date_and_time(date, time)
        print(appointment) if appointment else print("No appointment found")
    else:
        print("Invalid date or time")


def create_doctor():
    name = input("Enter the doctor's name: (i.e. Dr Bob)")
    phone = input("Enter the doctor's phone number: (i.e. 123-456-7890)")
    specialty = input("Enter the doctor's specialty: ")
    if (
        isinstance(name, str)
        and isinstance(phone, str)
        and isinstance(specialty, str)
        and len(name)
        and len(phone)
        and len(specialty)
    ):
        try:
            doctor = Doctor.create(name.title(), phone, specialty.title())
            print(doctor)
        except Exception as e:
            print("Error creating doctor: ", e)
    else:
        print("Invalid name, phone, or specialty")


def create_patient():
    name = input("Enter the patient's name: ")
    email = input("Enter the patient's email: ")
    phone = input("Enter the patient's phone number: ")
    if (
        isinstance(name, str)
        and isinstance(email, str)
        and isinstance(phone, str)
        and len(name)
        and len(email)
        and len(phone)
    ):
        try:
            patient = Patient.create(name.title(), email, phone)
            print(patient)
        except Exception as e:
            print("Error creating patient: ", e)
    else:
        print("Invalid name, email, or phone")


def create_appointment():
    date = input("Enter the appointment date (MM/DD/YYYY): ")
    time = input("Enter the appointment time (HH:MMAM or HH:MMPM): ")
    description = input("Enter the appointment description: ")
    doctor_id = input("Enter the doctor's id: ")
    patient_id = input("Enter the patient's id: ")
    if (
        Doctor.find_by_id(doctor_id)
        and Patient.find_by_id(patient_id)
        and len(date)
        and len(time)
        and len(description)
        and re.match(r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", date)
        and re.match(r"([0][0-9]|[1][0-2]):[0-5][0-9](AM|PM)", time)
    ):
        try:
            appointment = Appointment.create(
                date, time, description, int(doctor_id), int(patient_id)
            )
            print(appointment)
        except Exception as e:
            print("Error creating appointment: ", e)
    else:
        print("Invalid date, time, description, doctor name, or patient name")


def exit_program():
    print("Goodbye!")
    exit()


def update_doctor_by_id(id, name, phone, specialty):
    doctor = Doctor.find_by_id(id)
    doctor.full_name = name.title()
    doctor.phone = phone
    doctor.specialty = specialty.title()
    doctor = doctor.update()
    print(doctor)


def update_doctor():
    idx = input("Enter the doctor's id: ")
    name = input("Enter the doctor's name: ")
    phone = input("Enter the doctor's phone number: ")
    specialty = input("Enter the doctor's specialty: ")
    if (
        isinstance(idx, str)
        and isinstance(name, str)
        and isinstance(phone, str)
        and isinstance(specialty, str)
        and re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(name)
        and len(phone)
        and len(specialty)
    ):
        try:
            update_doctor_by_id(idx, name, phone, specialty)
        except Exception as e:
            print("Error updating doctor: ", e)
    else:
        print("Invalid id, name, phone, or specialty")


def update_patient_by_id(id, name, email, phone):
    patient = Patient.find_by_id(id)
    patient.full_name = name.title()
    patient.email = email
    patient.phone = phone
    patient = patient.update()
    print(patient)


def update_patient():
    idx = input("Enter the patient's id: ")
    name = input("Enter the patient's name: ")
    email = input("Enter the patient's email: ")
    phone = input("Enter the patient's phone number: ")
    if (
        isinstance(idx, str)
        and isinstance(name, str)
        and isinstance(email, str)
        and isinstance(phone, str)
        and re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(name)
        and len(email)
        and len(phone)
    ):
        try:
            update_patient_by_id(idx, name, email, phone)
        except Exception as e:
            print("Error updating patient: ", e)
    else:
        print("Invalid id, name, email, or phone")


def update_appointment_by_id(id, date, time, description, doctor_name, patient_name):
    try:
        appointment = Appointment.find_by_id(id)
        appointment.date = date
        appointment.time = time
        appointment.description = description
        doctor = Doctor.find_by_name(doctor_name.title())
        patient = Patient.find_by_name(patient_name.title())
        appointment.doctor_id = doctor.id
        appointment.patient_id = patient.id
        appointment = appointment.update()
        print(appointment)
    except Exception as e:
            print("Error updating appointment: ", e)


def update_appointment():
    idx = input("Enter the appointment's id: ")
    date = input("Enter the appointment date (MM/DD/YYYY): ")
    time = input("Enter the appointment time (HH:MMAM or HH:MMPM): ")
    description = input("Enter the appointment description: ")
    doctor_name = input("Enter the doctor's name: ")
    patient_name = input("Enter the patient's name: ")
    if (
        isinstance(idx, str)
        and isinstance(date, str)
        and isinstance(time, str)
        and isinstance(description, str)
        and isinstance(doctor_name, str)
        and isinstance(patient_name, str)
        and re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(date)
        and len(time)
        and len(description)
        and len(doctor_name)
        and len(patient_name)
    ):
        try:
            update_appointment_by_id(
                idx, date, time, description, doctor_name, patient_name
            )
        except Exception as e:
            print("Error updating appointment: ", e)
    else:
        print("Invalid id, date, time, description, doctor name, or patient name")


def delete_doctor_by_id(id):
    if doctor:= Doctor.find_by_id(int(id)):
        import ipdb; ipdb.set_trace()
        doctor.delete()
        print("Doctor successfully deleted")
    else:
        print("Invalid id")


def delete_doctor():
    idx = input("Enter the doctor's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_doctor_by_id(idx)
        except Exception as e:
            print("Error deleting doctor: ", e)
    else:
        print("Invalid id")


def delete_patient_by_id(id):
    patient = Patient.find_by_id(id)
    patient = patient.delete()
    print(patient)


def delete_patient():
    idx = input("Enter the patient's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_patient_by_id(idx)
        except Exception as e:
            print("Error deleting patient: ", e)
    else:
        print("Invalid id")


def delete_appointment_by_id(id):
    appointment = Appointment.find_by_id(id)
    appointment = appointment.delete()
    print(appointment)


def delete_appointment():
    idx = input("Enter the appointment's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_appointment_by_id(idx)
        except Exception as e:
            print("Error deleting appointment: ", e)
    else:
        print("Invalid id")


def find_patients_by_doctor_name():
    name = input("Enter the doctor's name: ")
    if len(name) > 0 and re.match(r"^[a-zA-Z ]+$", name) and name.title():
        doctor = Doctor.find_by_name(name.title())
        if doctor:
            patients = doctor.patients()
            for patient in patients:
                print(patient())
    else:
        print("Invalid name")


from classes.doctor import Doctor
from classes.patient import Patient
from classes.appointment import Appointment
