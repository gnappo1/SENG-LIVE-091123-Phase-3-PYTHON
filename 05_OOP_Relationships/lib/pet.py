
class Pet:
    all = []

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner #! Dependency Injection
        # Pet.all.append(self) #! anti-pattern and major pet peeve
        # self.all.append(self) #! completely fine in Python
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

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, new_owner):
        from .owner import Owner
        if not isinstance(new_owner, Owner):
            raise TypeError("Owner must be of type Owner")
        elif hasattr(self, "owner"):
            raise Exception("You cannot reset the owner after birth")
        else:
            self._owner = new_owner

if __name__ == "__main__":
    try:
        fido = Pet(name="Fido", breed="Pug")
    except Exception as e:
        import ipdb; ipdb.set_trace()
    print(fido)
