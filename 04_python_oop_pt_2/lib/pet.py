#!/usr/bin/env python3
# Class Attributes and Methods 

# import ipdb
from decorator_profiler import measure_performance
# ALLOWED_LIST = ['name', 'age', 'temperament', 'breed', 'owner']

class Pet:
# ✅ Define a class attribute (total_pets) and set it to 0

    # __slots__= ('_name', '_age', '_temperament', '_breed', '_owner')
    
    # What happens with our instances when we add a class attribute?
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v) #if k in ALLOWED_LIST else None
            # self._name, self.age, self.breed, self.temperament, self.owner = name, age, breed, temperament, owner

    # Using Property to control the behavior of attributes
    def get_name(self):
        print("Inside the name property getter")
        return self._name
    
    def set_name(self, new_name):
        print("Inside the name property setter")
        if not isinstance(new_name, str):
            raise TypeError("Value must be a string")
        elif len(new_name) <= 2:
            raise ValueError("Value must be a string with more than 2 chars")
        else:
            self._name = new_name
        
    name = property(get_name, set_name)
    
    def get_breed(self):
        print("Inside the breed property getter")
        return self._breed
    
    def set_breed(self, new_breed):
        print("Inside the breed property setter")
        if not isinstance(new_breed, str):
            raise TypeError("Value must be a string")
        elif len(new_breed) <=2:
            raise ValueError("Value must be an int greater than 0")
        else:
            self._breed = new_breed

    breed = property(get_breed, set_breed)
    
    def get_age(self):
        print("Inside the age property getter")
        return self._age
    
    def set_age(self, new_age):
        print("Inside the age property setter")
        if not isinstance(new_age, int):
            raise TypeError("Value must be an int")
        elif new_age < 0:
            raise ValueError("Value must be an int greater or equal to 0")
        else:
            self._age = new_age
        
    age = property(get_age, set_age)
    
    def get_owner(self):
        print("Inside the owner property getter")
        raise AttributeError('Privacy concern, you cannot see me!')
    
    def set_owner(self, new_owner):
        print("Inside the owner property setter")
        if not isinstance(new_owner, str):
            raise TypeError("Value must be an string")
        elif len(new_owner) <= 2:
            raise ValueError("Value must be an string greater than 2")
        else:
            self._owner = new_owner
        
    owner = property(get_owner, set_owner)
    
    def get_temperament(self):
        print("Inside the temperament property getter")
        raise AttributeError('Privacy concern, you cannot see me!')
    
    def set_temperament(self, new_temperament):
        print("Inside the temperament property setter")
        if not isinstance(new_temperament, str):
            raise TypeError("Value must be a string")
        elif len(new_temperament) < 2:
            raise ValueError("Value must be an string greater or equal to 2")
        else:
            self._temperament = new_temperament
        
    temperament = property(get_temperament, set_temperament)
    
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            owner:{self.owner}
        ''')

fido = Pet(name="Fido", xyz="xyz", age=2, breed="pug", temperament="docile", owner="Matteo")
milo = Pet(name="Milo", xyz="xyz", age=2, breed="pug", temperament="docile", owner="Matteo")
print('done')
