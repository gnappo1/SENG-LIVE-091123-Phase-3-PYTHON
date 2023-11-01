#!/usr/bin/env python3

from owner import Owner, CONN as owner_conn, CURSOR as owner_cursor
from pet import Pet, CONN as pet_conn, CURSOR as pet_cursor

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

# Pet.drop_table()
# Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")
# spot.save()
# spot.name = "test"
# spot.update()
# Pet.new_for_db()
import ipdb; ipdb.set_trace()