#!/usr/bin/env python3

# 📚 Review:
# Python Environment Setup
# Python Debugging Tools
# Python Data Types

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb


# TODO Initial Discussion
# 0. Style Guide (visit: https://peps.python.org/pep-0008/#code-lay-out)
# 1. Data Types
# 2. Variable Naming Conventions (visit https://peps.python.org/pep-0008/#naming-conventions)
# 3. String Interpolation
# 4. Printing to Console

#! 1. Data Types
# None: NoneType
# Boolean: bool (True, False)
# String: str
# Numeric: float, int, complex
# Sequence: list, tuple, range
# Set: set, frozenset
# Mapping: dictionary
# Binary: bytes, bytearray, memoryview


#! 2. Variable Naming Conventions
# casing: snake_case OR all caps for constants (ALL)
# leading underscore or letter is allowed
# case-sensitive
# no special keyword for declarations
# delete variables
# NameError exception

pet_mood = "Hungry!"
# print(pet_mood)
#! You can delete a variable!
# del pet_mood
# print(pet_mood)

pet_name = "Rose"

# TODO 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."

# if pet_mood == "Hungry!":
#     print("Rose needs to be fed.")
# elif pet_mood == "Rowdy!":
#     print("Rose needs a walk.")
# else:
#     print("Rose is all good.")
#     # Note => Feel free to set your own values for "pet_mood" to view various outputs.

#! if you have python V3.10+
# match(pet_mood):
#     case "Hungry!":
#         print("Rose needs to be fed.")
#     case "Rowdy!":
#         print("Rose needs a walk.")
#     case _:
#         print("Rose is all good.")


# TODO 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."
#! recommended
# print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose is all good.")
#! not recommended - hard to read defeats the purpose of a ternary
# print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose needs a walk.") if pet_mood == "Rowdy!" else  print("Rose is all good.")

# TODO 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"
def say_hello():
    # ipdb.set_trace()
    return "Hello, world!"
# print(say_hello(), end="\n")

# TODO 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
# Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
# pet_greeting("Rose") => "Rose says hello!"
# pet_greeting("Spot") => "Spot says hello!"
def pet_greeting(name, age=20):
    return f"{name} says hello! I am {age} yo."
# print(pet_greeting("Rose", 7))
# print(pet_greeting("Spot"))

# TODO 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."
def pet_status(pet_name, pet_mood):
    # global pet_mood
    if pet_mood == "Hungry!":
        return(f"{pet_name} needs to be fed.")
    elif pet_mood == "Rowdy!":
        return(f"{pet_name} needs a walk.")
    else:
        return(f"{pet_name} is all good.")
# print(pet_status("Rose", "Hungry!"))
# print(pet_status("Spot", "Rowdy!"))
# print(pet_status("Bud", "Relaxed"))
#     # Note => Feel free to set your own values for "pet_mood" to view various outputs.
# Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
# in Global Scope.

def test(first, second, *all, name, age, **kwargs):
    #! keyword arguments are always listed after the * operator 
    print(f"Required args are: {first}, {second}")
    print(f"Additional extra args are: {all}")
    print(f"Key-value args are: {name}, {age}")
    print(f"Additional extra keyword args are: {kwargs}")

# test("one", "two", True, 32, name="Matteo", age=32, job="teacher")

# TODO 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors.
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"
def pet_birthday(age):
    """
    This function takes in one argument of type int
    Checks of the type is correct and then returns ...
    """
    # if type(age) is int:
    try:
        return f"Happy Birthday! Your pet is now {age + 1}."
    except Exception as e:
        return "You must pass an integer!" #! or use the error e

# print(pet_birthday(10))
# print(pet_birthday("oops"))
# print(pet_birthday.__doc__)

# Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()

# TODO 7. ✅ Write a loop that will print out a countdown from 5 to 0
#! Loops (for...in, while)
x = 5
while x >= 0:
    print(x)
    x -= 1

#! or equivalent
for x in range(5, -1, -1):
    print(x)

#! When you do not care about the number in the range but rather
#! want to repeat the same action multiple times
for _ in range(5):
    print("Same thing printed 5 times")
    
# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()

#! The following conditional is used to differentiate between the two scenarios:
    #* We run the file from the terminal as a script
    #* We use the file as a module imported somewhere else in our app

if __name__ == '__main__':
    #! We run the file from the terminal as a script
    ipdb.set_trace()