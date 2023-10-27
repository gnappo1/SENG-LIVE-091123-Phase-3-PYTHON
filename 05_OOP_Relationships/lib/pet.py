class Pet:
    all = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type string")
        elif not new_name:
            raise ValueError("Names must be at least one char long")
        else:
            self._name = new_name
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise TypeError("Breed must be of type string")
        elif not new_breed:
            raise ValueError("Breeds must be at least one char long")
        else:
            self._breed = new_breed