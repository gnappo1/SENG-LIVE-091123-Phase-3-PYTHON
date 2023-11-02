# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3
from helper import Helper
from contextlib import contextmanager

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

# Define a context manager for the database connection
# In this scenario, when the manager is used in every method, a connection is opened and closed for every method invocation
@contextmanager
def db_connection():
    conn = sqlite3.connect('resources.db')  # Replace 'your_database.db' with your actual database file
    try:
        yield conn
    finally:
        conn.close()

class Pet(Helper):

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, id=None):
        self.name, self.species, self.breed, self.temperament, self.id = name, species, breed, temperament, id
        
    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CONN.execute(f"""
                    CREATE TABLE IF NOT EXISTS {cls.pascal_to_camel_plural()} (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        species TEXT,
                        breed TEXT,
                        temperament TEXT
                    );
                """)
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"

        
    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CONN.execute("""
                    DROP TABLE pets;
                """)
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        try:
            with CONN:
                cursor = CONN.execute("""
                    INSERT INTO pets (name, species, breed, temperament) 
                    VALUES (?, ?, ?, ?);
                """, (self.name, self.species, self.breed, self.temperament))
                self.id = cursor.lastrowid
                return self
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"


    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament):
        return cls(name, species, breed, temperament).save()
        # pet = cls(name, species, breed, temperament)
        # pet.save()
        # return pet
    
    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_for_db(cls):
        try:
            with CONN:
                cursor = CONN.execute("""
                    SELECT * FROM pets
                    ORDER BY id DESC
                    LIMIT 1
                """)
                tup = cursor.fetchone() 
                return cls(tup[1], tup[2], tup[3], tup[4], tup[0])
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        try:
            with CONN:
                cursor = CONN.execute("""
                    SELECT * FROM pets;
                """)
                return [cls(tup[1], tup[2], tup[3], tup[4], tup[0]) for tup in cursor.fetchall()]
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"
    
    #! CODE ADDED AFTER THE END OF THE LECTURE
    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                cursor = CONN.execute("""
                    SELECT * FROM pets
                    WHERE name is ?;
                """, (name, ))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[0]) if row else None
        # If No "pet" Found, return "None"
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"
 
    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB
    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                cursor = CONN.execute("""
                    SELECT * FROM pets
                    WHERE id is ?;
                """, (id, ))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[0]) if row else None
        # If No "pet" Found, return "None"
        except sqlite3.Error as e:
            return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"
 
    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by(cls, name, species, breed, temperament):
        return cls.find_by_name(name) or cls.create(name, species, breed, temperament)
        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Instance Method to Update All Attributes
    #! Discussion: instance or class method? How do we intend to use it?
    def update(self):
        try:
            with CONN:
                CONN.execute("""
                    UPDATE pets
                    SET name=?, species=?, breed=?, temperament=?
                    WHERE id = ?
                """, (self.name, self.species, self.breed, self.temperament, self.id))
                CONN.commit()
                #! is there any different between the local self and the corresponding row of data in the db?
                return type(self).find_by_id(self.id)
        except sqlite3.Error as e:
                return (e and e.args and e.args[0]) or "An issue was raised by sqlite3!"