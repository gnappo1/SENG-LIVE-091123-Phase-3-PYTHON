# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes
ALLOWED_LIST = ["name", "age", "breed", "owner", "temperament"]
# 1. ✅ Create a Pet class
class Pet:
    name_of_class = "Something"
    """A class that represents the idea of an animal"""
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            #! we are not using the setter but assigning a value to the private attribute directly
            # setattr(self, f"_{k}", v) if k in ALLOWED_LIST else None 
            #! we are using the setter method to set initial values rather than doing it directly
            setattr(self, k, v) if k in ALLOWED_LIST else None 
    
    def __str__(self):
        return f"Name: {self._name} and age: {self._age}"
    
    def get_name(self):
        print("I am inside the getter")
        return self._name

    def set_name(self, name):
        print("I am inside the setter")
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise TypeError("Name must be a non-empty string")

    name = property(fget=get_name, fset=set_name)
    def get_age(self):
        return self._age

    def set_age(self, age):
        print("I am inside the setter")
        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            raise TypeError("Age must be a positive integer")

    age = property(fget=get_age, fset=set_age)

fido = Pet(name="Fido", age=2, breed="pug", owner="Matteo", temperament="docile")
import ipdb; ipdb.set_trace()

# __name__ => dunder methods
# __name => mangling used for specificity naming rather than hiding. Scopes attr name under the class it belongs to 
# _name => suggests that the attribute should be treated as private
# name_ => use reserved keywords or globals wo fear of overriding them
