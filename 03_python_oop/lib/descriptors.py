class MyDescriptor:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if value >= 0:
            instance._value = value
        else:
            raise ValueError("Value must be non-negative.")

class MyClass:
    def __init__(self):
        self._value = 0
    value = MyDescriptor()

obj = MyClass()
obj.value = 42