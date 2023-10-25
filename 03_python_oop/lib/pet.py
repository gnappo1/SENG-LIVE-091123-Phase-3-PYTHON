# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes
ALLOWED_LIST = ["name", "age", "breed", "owner", "temperament"]
# 1. ✅ Create a Pet class
class Pet:
    """A class that represents the idea of an animal"""
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, f"_{k}", v) if k in ALLOWED_LIST else None
    
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
# In the `__init__` method of the `Pet` class, `_name = name` is
# assigning the value of the `name` argument to the `_name` attribute
# of the instance. This is a common practice to initialize instance
# attributes with the values passed as arguments during object
# creation.

    

    # Note: Add 'pass' to the Pet class
fido = Pet(name="Fido", age=2, breed="pug", owner="Matteo", temperament="docile")
import ipdb; ipdb.set_trace()

# __name__ => dunder methods
# __name => mangling used for specificity naming rather than hiding. Scopes attr name under the class it belongs to 
# _name => suggests thatb the attribute should be treated as private
# name_ => use reserved keywords or globals wo fear of overriding them

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__ 

    # Add arguments to instances  

    # Attributes:
        # name
        # age
        # breed
        # temperament
        # owner
    
    # Use dot notation to access each Pet instance's attributes 

    # Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # Review the "self" keyword 
    
    # Invoke "print_pet_details" on an instance 
    
    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet

# 5. ✅ Create an Owner class with two instance methods:

    # get_name => Retrieve Owner's name
    
    # set_name => Set Owner's name

        # Ensure that Owner's name is a String

        # If not, issue warning of "Name must be a string"

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name

    # Object Properties => Attributes that are controlled by methods