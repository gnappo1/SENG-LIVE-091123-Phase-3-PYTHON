# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Owner:
    
    pass