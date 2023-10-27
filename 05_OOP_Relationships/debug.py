#!/usr/bin/env python3

from lib.pet import Pet
from lib.owner import Owner

pat = Owner(
    "Pat",
    "Jones",
)
rose = Owner(
    "Rose",
    "Smith",
)

taco = Pet(
    "Taco",
    "Cat",
    pat
)
fido = Pet(
    "Fido",
    "Dog",
    rose
)
joe = Owner("Joe", "Jones")
princess = Pet("Princess", "Fish", joe)

theresa = Owner("Theresa", "Jones")


from lib.appointment import *
from lib.doctor import *
from lib.patient import *

jimmy = Patient("Jimmy")
patty = Patient("Patty")
may = Patient("May")

rosenbaum = Doctor("Dr. Rosenbaum", "Gynocology")
williams = Doctor("Dr. Williams", "Oncology")


Appointment(doctor=rosenbaum, patient=may, reason_for_visit="Stomach issues.", date="5/25/23")
Appointment(doctor=rosenbaum, patient=patty, reason_for_visit="Non-stop migrains", date="5/26/23")
Appointment(doctor=williams, patient=jimmy, reason_for_visit="Legs always sore in the mornings", date="5/23/23")
Appointment(doctor=williams, patient=patty, reason_for_visit="Feels light-headed when jogging", date="5/12/23")
Appointment(doctor=rosenbaum, patient=may, reason_for_visit="Can't keep food down", date="5/30/23")


import ipdb

ipdb.set_trace()
