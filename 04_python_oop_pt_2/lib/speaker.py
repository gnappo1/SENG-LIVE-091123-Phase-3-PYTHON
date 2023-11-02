class Speaker:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.add_property(k)
            setattr(self, k, v)

    def add_property(self, name):
        # Dynamically create a property
        def getter(self):
            try:
                return getattr(self, f"_{name}")
            except Exception:
                return None

        def setter(self, value):
            validation_functions = {
                "age": self.validate_age,
                "name": self.validate_name,
                "city": self.validate_city,
            }

            if name in validation_functions and validation_functions.get(name):
                setattr(self, f"_{name}", value)

        setattr(type(self), name, property(getter, setter))

    def validate_age(self, age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        elif age < 0:
            raise ValueError("Age must be a positive integer")
        else:
            return True
    
    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
    
    def validate_city(self, city):
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        elif len(city) < 2:
            raise ValueError("City must be at least 2 characters")

# Create an instance of Speaker
my_instance = Speaker(age=32, name="Matteo", city="SD")

import ipdb; ipdb.set_trace()

