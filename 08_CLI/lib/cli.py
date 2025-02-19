from helpers import (
    welcome,
    menu,
    list_doctors,
    list_patients,
    list_appointments,
    find_doctor_by_name,
    find_patient_by_name,
    find_appointment_by_date_and_time,
    create_doctor,
    create_patient,
    create_appointment,
    update_doctor,
    update_patient,
    update_appointment,
    delete_doctor,
    delete_patient,
    delete_appointment,
    find_patients_by_doctor_name,
    exit_program,
)

def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_doctors()
        elif choice == "2":
            list_patients()
        elif choice == "3":
            list_appointments()
        elif choice == "4":
            find_doctor_by_name()
        elif choice == "5":
            find_patient_by_name()
        elif choice == "6":
            find_appointment_by_date_and_time()
        elif choice == "7":
            create_doctor()
        elif choice == "8":
            create_patient()
        elif choice == "9":
            create_appointment()
        elif choice == "10":
            update_doctor()
        elif choice == "11":
            update_patient()
        elif choice == "12":
            update_appointment()
        elif choice == "13":
            delete_doctor()
        elif choice == "14":
            delete_patient()
        elif choice == "15":
            delete_appointment()
        elif choice == "16":
            find_patients_by_doctor_name()
        elif choice == "17":
            exit_program()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()