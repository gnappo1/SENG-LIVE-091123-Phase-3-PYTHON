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
)
fido = Pet(
    "Fido",
    "Dog",
)
princess = Pet("Princess", "Fish")

joe = Owner("Joe", "Jones")
theresa = Owner("Theresa", "Jones")


from lib.appointment import *
from lib.doctor import *
from lib.patient import *

# jimmy = Patient("Jimmy")
# patty = Patient("Patty")
# may = Patient("May")

# rosenbaum = Doctor("Dr. Rosenbaum", "Gynocology")
# williams = Doctor("Dr. Williams", "Oncology")


# Appointment(rosenbaum, may, "Stomach issues.", "5/25/23")
# Appointment(rosenbaum, patty, "Non-stop migrains", "5/26/23")
# Appointment(williams, jimmy, "Legs always sore in the mornings", "5/23/23")
# Appointment(williams, patty, "Feels light-headed when jogging", "5/12/23")
# Appointment(rosenbaum, may, "Can't keep food down", "5/30/23")


import ipdb

ipdb.set_trace()
