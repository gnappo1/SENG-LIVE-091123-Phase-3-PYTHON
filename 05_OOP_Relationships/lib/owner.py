from .pet import Pet
class Owner:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.pets = [] #! SUPER WRONG PLEASE DO NOT USE IT
        type(self).all.append(self)

    def pets(self):
        #! return a list of all pets whose owner is myself
        return [pet for pet in Pet.all if pet.owner is self]
