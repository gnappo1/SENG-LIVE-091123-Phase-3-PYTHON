# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

#! Lists
#TODO Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

#TODO Reading Information From Lists
#2. ✅ Return the first pet name
# pet_names[0]
# pet_names[1000] => IndexError: list index out of range
#3. ✅ Return all pet names beginning from the 3rd index (included)
# pet_names[3:]
#4. ✅ Return all pet names before the 3rd index (not included)
# pet_names[:3]
#5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index
# pet_names[3:7]
#6. ✅ Find the index of a given element
# pet_names.index("Lea") => 4
# pet_names.index("LeaX") => ValueError: 'LeaX' is not in list
#7. ✅ Read the original list in reverse order
# pet_names.reverse() => destructive returns None
# pet_names[::-1] => non destructive
#8. ✅ Return the frequency of a given element

#TODO Updating Lists
#9. ✅ Change the first pet_name to all uppercase letters
# pet_names[0] = pet_names[0].upper()
#10. ✅ Append a new name to the list
# pet_names.append("matteo")
#11. ✅ Add a new name at a specific index
# pet_names.insert(0, "test") => inserts before el currently in that index position
#12. ✅ Add two lists together
# pet_names + ["new el"]
#first, *rest = pet_names => unpacking is possible in Python!
#13. ✅ Remove the final element from the list
# pet_names.pop()
#14. ✅ Remove element by specific index
# pet_names.pop(index) => index has to be within range or IndexError: pop index out of range
#15. ✅ Remove a specific element
# pet_names.remove("Rose") => destructive but el has to be in collection else ValueError: list.remove(x): x not in list
#16. ✅ Remove all pet names from the list
# pet_names.clear() => destructive

#!Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable
    
    # Why Are Tuples Immutable?

        # What advantages does this provide for us? In what situations
        # would this serve us?
#TODO Accessing Elements
#17. ✅ Create an empty Tuple, one with one element and one with 10 pet ages
empty_tuple = ()
single_tuple = (True,)
ages_generator = tuple(range(10))

#18. ✅ Print the first pet age

#TODO Testing Mutability (you can add a tuple to a tuple though)
#19. ✅ Attempt to remove an element with ".pop" => AttributeError: 'tuple' object has no attribute 'pop'
#20. ✅ Attempt to change the first element => TypeError: 'tuple' object does not support item assignment

#TODO Tuple Methods
#21. ✅ Return the frequency of a given element
# ages_generator.count(44) => 0
# ages_generator.count('4') => 1
#22. ✅ Return the index of a given element
# ages_generator.index('44') => ValueError: tuple.index(x): x not in tuple
# ages_generator.index(4) => 4

#! Range
#23. ✅ create a Range 
# Note:  Ranges are primarily used in loops
r = range(10)
r.step
r.stop
r.start

#! Sets (value cannot be modified but you can add/remove elements)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}
# z = {1, 2, 3}
# y = {1, 4, 5}
#TODO Reading
#27. ✅ Print set elements with a loop
# for el in pet_fav_food:
#     print(el)
#27. ✅ Check if an element is in a set
# <el> in pet_fav_food
#27. ✅ Get first element
# i = iter(pet_fav_food)
# next(i)
#28. ✅ Get a copy of a set
# pet_fav_food.copy()
#28. ✅ isdisjoint, issubset, issuperset
# z.isdisjoint(y)

#TODO Updating 
#29. ✅ Add an element to a set
# pet_fav_food.add("biscuits")
#30. ✅ Union, intersection, difference
# z.union(y)
# z.intersection(y) or z & y
# z.difference(y)
#30. ✅ Update current set with elements from other set
# a.update(y)

#TODO Deleting
#31. ✅ Delete specific el using ".remove"  VS ".discard"
# Remove: 'Remove an element from a set; it must be a member.\n\nIf the element is not a member, raise a KeyError.'
# pet_fav_food.remove(2) => KeyError
# pet_fav_food.remove(4) => it will remove it destructively
# pet_fav_food.discard(2) => DOES NOTHING
# pet_fav_food.discard(4) => it will remove it destructively
#32. ✅ Delete random element using ".pop"
# pet_fav_food.pop() => watch out from where the el is removed
#33 ✅ Delete every key/value pair
# pet_fav_food.clear()

#! Dictionaries (from 3.7+, dictionaries are ordered)
#TODO Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

#TODO Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# pet_info_spot["name"]
#28. ✅ Print the pet attribute of "age" using ".get"
# pet_info_spot.get("names", "default value")

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error
#28b. ✅ Get dict keys
# pet_info_spot.keys() => dict_keys(['name', 'age', 'breed'])
#28c. ✅ Get dict values
# pet_info_spot.values() => dict_values(['Spot', 25, 'boxer'])
#28d. ✅ Get dict pairs
# pet_info_spot.items() => dict_items([('name', 'Spot'), ('age', 25), ('breed', 'boxer')])

#TODO Updating 
#29. ✅ Update Rose's age to 12
# pet_info_rose['age'] = 12
#30. ✅ Update Spot's age to 26
# pet_info_spot.update({"age": 26})
# pet_info_spot |= {"age": 26}

#TODO Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []
# del pet_info_spot["name"]
#32. ✅ Delete Spot's age using ".pop"
# pet_info_spot.pop("name") => returns the value for the key-value pair removed
#33. ✅ Delete the last item for Rose using "popitem()"
# pet_info_spot.popitem() => ('breed', 'boxer')
#33b ✅ Delete every key/value pair => clear()
# pet_info_spot.clear()

#! Loops 

#34. ✅ Loop through a range of 10 and print every number within the range
#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
#36. ✅ Loop through the "pet_info" list and print every dictionary
#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument
#38. ✅ Create a function that takes a list as a parameter
    # The function should define a variable ("counter") and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Once the loop has finished, return the final value of "counter"

#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'
    
#! Functional Programming corner
# map like VS map
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]
names_to_upper = [pet.get("name").upper() for pet in pet_info]
# print(names_to_upper)
names_to_upper_with_map = list(map(lambda pet: pet.get("name").upper(), pet_info))
# print(names_to_upper_with_map)

# find like VS find
#41. ✅ Use list comprehension to find all of the pets under 3 years old
pets_under_3_with_gen = (pet for pet in pet_info if pet.get("age") > 3)
next(pets_under_3_with_gen)

# filter like VS filter
#42. ✅ Use list comprehension to find all of the pets under 3 years old
pets_under_3 = {pet for pet in pet_info if pet.get("age") > 3}
# print(pets_under_3)
def check_condition(pet):
    return pet["age"] < 3

names_to_upper_with_filter = list(filter(check_condition, pet_info))
# print(names_to_upper_with_filter, "here")

# reduce like VS reduce
#42. ✅ Use list comprehension to find all of the pets under 3 years old

#! Writing Generators
#43. ✅ Create a generator expression matching the filter above
(pet for pet in pet_info if pet.get("age") > 3)

#! Compare Generators and Expressions
import sys
import timeit
starter_list = list(range(100000))

#! MEMORY
print("List Comprehension Memory Size", sys.getsizeof([el for el in starter_list if el%2==0]))
# 444376
print("Generator Expression Memory Size",sys.getsizeof((el for el in starter_list if el%2==0)))
#208

#! RUNTIME
print("Comprehension Run 1 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1))
#=> 0.005183833185583353
print("Comprehension Run 1000 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1000))
# => 2.4483373747207224
print("Generator Run 1 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1))
# => 9.041279554367065e-06
print("Generator Run 1000 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1000))
# => 0.00024854158982634544