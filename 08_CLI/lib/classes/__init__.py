import sqlite3

CONN = sqlite3.connect('office.db')
CURSOR = CONN.cursor()