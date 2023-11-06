# SENG-LIVE-WEST-061223 Phase 3 - Python

## Phase Level Objectives

- Understand the principles of Python as a language including principles of object oriented programming
- Understand the characteristics of a relational database
- Perform CRUD actions on a database using SQLAlchemy & Alembic
- Design an API to handle CRUD actions
- Communicate with an API using different HTTP verbs
- Create and present a project with a React frontend and a database-backed API backend


| Lecture                                                                     |   Notes    | Videos     | Starter      | Solution      |
| --------------------------------------------------------------------------- | :--------: | ---------- | ------------ | ------------- |
| 1. (10/23/23) Python Fundamentals                                           | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/qBDAzHzlFFk) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/01_matteo_example_starter_python_fundamentals/01_python_fundamentals) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/01_matteo_example_solution_python_fundamentals/01_python_fundamentals) |
| 2. (10/24/23) Python Data Structures                                        | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/ctqRfLTjkcQ) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/02_matteo_starter_data_structures/02_python_data_structures) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/02_matteo_solution_data_structures/02_python_data_structures) |
| 3. (10/25/23) Object Oriented Programming in Python                         | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/TYS30LKTD8Y) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/03_matteo_starter_oop_part_1/03_python_oop) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/03_matteo_solution_oop_part_1/03_python_oop) |
| 4. (10/26/23) OOP 2: Class Methods, Class Variables | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/3M_aUQ3cjPI) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/04_matteo_starter_oop_part_2/04_python_oop_pt_2) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/04_matteo_solution_oop_part_2/04_python_oop_pt_2) |
| 5. (10/27/23) Object Relationships     | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/VdFiXva12XE) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/05_matteo_starter_relationships/05_OOP_Relationships) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/05_matteo_solution_relationships/05_OOP_Relationships) |
| 6. (10/30/23) SQL Fundamentals & Table Relations                            | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/SLfIcdtdF5A) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/06_matteo_starter_SQL/06_SQL) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/06_matteo_solution_SQL/06_SQL) |
| 7. (11/1/23) Object-Relational Mapping                                     | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/-cmqHbxzMq0) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/07_matteo_starter_ORM/07_ORM) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/07_matteo_solution_orm/07_ORM) |
| 8. (11/03/23) Your First CLI                                          | [Notes](https://docs.google.com/document/d/1Mkg0egJlOLxbEwd_SQLPQQdy2NJ1wfu77FDd1mjqmgw/edit?usp=sharing) | [Video](https://youtu.be/p_PE--VWOu4) | [Starter](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/08_matteo_starter_cli/08_CLI) | [Solution](https://github.com/gnappo1/SENG-LIVE-091123-Phase-3-PYTHON/tree/08_matteo_starter_cli/08_CLI) |


## 1: Python Fundamentals
### Lecture Goals:
- Review an introduction to Python and phase trajectory 
- Demonstrate Python package management with `pip`
- Demonstrate debugging in Python with `shell`, `print`, and `ipdb`
- Review Python data types (`str`, `int`, `float`, `complex`, `bol`, `bytes`, `bytearry`, `memoryview`, `None`)
- Demonstrate Python conditionals and control flow
- Demonstrate Python functions
- Review Python variable scope and the global keyword
- Review Python error messages and exceptions 
- Demonstrate handling errors with `try:` and `except:` 
- Stretch Goals
    - Review `pytest`
    - Review the Python Style Guide

### Lecture Topics:
- Python and a Short History
- Package Management with `pip`
- Debugging
    - `print`
    - `ipdb`
    - Python Shell
    - Errors
    - Exceptions
        - `try:` `except:` 
- Python Conditionals and Control Flow
    - `if...else`
    - Comparison Operators
        - `>:` greater than
        - `>=:` greater than or equal to
        - `<:` less than
        - `<=:` less than or equal to
        - `==:` equal to
        - `!=:` not equal to
    - Logical operators
        - `and:` 
        - `or:` 
        - `not:` 
- Conditional Expressions
    - Ternary
- Python Functions
    - Function Definition 
    - Params
    - Default Params
    - Arguments
    - Invoking 
- Error Handling 
    - Reading Errors 
        - Syntax Errors, Logic Errors, and Exceptions
        - `AssertionError`
        - `IndexError` and `KeyError`
        - `NameError`
        - `TypeError`
        - `try:` `except:`
- Stretch Topics
    - `pytest`
        - How to Read Tests 
            - Note: Create tests is not covered in the labs
    - Python Style Guide

## 2: Python Data Structures
### Lecture Goals:
- Demonstrate Sequence types (`list`, `tuple`, `range`)
- Review the different uses for each Sequence type
- Demonstrate standard methods for accessing, updating and deleting values in Lists
- Review Tuples
- Review Ranges 
- Demonstrate Mapping types with Dictionaries
- Demonstrate standard methods for accessing, updating and deleting values in Dictionaries
- Demonstrate Set types with `set()` and `frozenset()`
- Demonstrate `for` and `while` loops
- Demonstrate list compressions 
- Stretch Goals
    - Demonstrate Generator expressions 
    - Demonstrate how to create a `switch` using a Dictionary

### Lecture Topics:
- Sequence Types
    - List
    - Tuple
    - Range
    - Common Sequence Operators 
    - List Methods 
    - Tuples and Immutable vs Mutable 
- Mapping Types
    - Dict 
        - `switch`
- Set Types
    - Set
- Loops
    - `for`
    - `while`
    - List Compression
- Sequence Operators
- Sequence Functions and Methods
- Stretch Topics
    - Generator Expressions 

## 3: Object Oriented Programming in Python
### Lecture Goals:
- Define Object Oriented Programming
- Explain the benefits of Object Oriented Programming
- Explain the principles of Object-Oriented Design
- Demonstrate classes 
- Demonstrate instances 
- Demonstrate `__init__`
- Demonstrate instance method
- Demonstrate the `self` keyword 
- Stretch Goals
    - Demonstrate object properties
    - Demonstrate mass assignment during Class instantiation

### Lecture Topics:
- Object Oriented Programming 
- Benefits of Object Oriented Programming
- Principles of Object-Oriented Design
- Classes 
- Instances
- Initializing with Attributes Using `__init__`
- Instance Methods
- Self
- Stretch Topics
    - Object Properties

## 4: OOP 2: Class Methods, Class Variables, & Object Relationships
### Lecture Goals:
- Demonstrate Decorators 
    - `@decorator`  
- Demonstrate class variables
    - Defining class variables
    - Updating class variables 
- Demonstrate class methods
    - Defining class methods 
    - `@classmethod`
    - `cls` keyword 
- Object Inheritance
- Stretch Goals
    - Super

- Build one-to-many relationships between objects
    - Define one-to-many relationships
    - Discuss their importance and use
    - Emphasize single-source-of-truth
    - Demonstrate building one-way and two-way relationships
- Build many-to-many relationships between objects
    - Define many-to-many relationships
    - Discuss their importance and use
    - Demonstrate building the relationship with and without intermediary class
- Aggregate Methods
    - Write aggregate methods to collect data about objects using their related objects

### Lecture Topics:
- Decorators
- Class Variables
- Class Methods
- Object Inheritance
- Stretch Topic
    - Super

## 5: SQL Fundamentals & Table Relations
### Lecture Goals:
- Explain why we use databases
- Explain what SQL is and why we use it
- Explain the differences between a database, server, and API
- Explain the differences between rows and columns in a table
- Explain the differences between a Foreign Key and a Primary Key
- Explain what a join table is
- Explain what it means to seed a database
- Observe using SQL to communicate with a database
- Explain what an ORM is

### Lecture Topics:
- The Use Value of Databases in Applications
- Domain Modeling
- Join Table
- Mapping Columns and Rows to Classes and Instances
- Primary Keys
- Foreign Keys
- SQL
- ORM

## 6: Object-Relational Mapping
### Lecture Goals:
- Demonstrate configuring an application to connect with sqlite3
- Demonstrate a create table method 
- Review preventative measures for SQL injection
- Demonstrate save and create methods  
    - Save => Persist created instance to DB
    - Create => Instantiate / persist created instance to DB, return new instance 
- Demonstrate query methods to find and retrieve resources 
- Stretch Goal
    - Make a `create_and_find_by` member
    - Make `update` and `delete` members

### Lecture Topics:
- The benefits of ORM
- Connecting ORMs to DBs
- How to Use Data From a Database to Make Python Objects
- Mapping a Database Table to a Python Object
- Turning Database Rows into Python Objects


## 7: SQLAlchemy & Alembic
### Lecture Goals:
- Explain what SQLAlchemy is and how it benefits us as an ORM
    - Demonstrate creating a database with SQLAlchemy 
    - Demonstrate creating a schema
    - Demonstrate creating columns with SQLAlchemy
    - Demonstrate creating column constraints with SQLAlchemy 
    - Demonstrate creating indexes with SQLAlchemy 
    - Demonstrate creating default values 
- Explain Alembic and what it does for us
    - Demonstrate configuring an application to use Alembic 
    - Demonstrate creating migrations using Alembic
    - Demonstrate creating manual migrations using Alembic
    - Demonstrate CRUD in SQLAlcehmy
        - Adding data with .commit
            - `.all`, `.order_by`, `desc`, `limit`, function filter, and loop compression to grab specific columns 
        - Querying data with `.query`
        - Updating data with `.update` and `.commit`
        - Deleting data with `.delete`

### Lecture Topics:
- Creating a Database 
- Creating a Schema 
    - Columns 
    - Constraints
    - Index
    - Default Values
- Alembic
    - Migrations
        - Configuring the Migration Environment
        - Creating Migrations 
        - Manual Migrations 
- CRUD 
    - Sessions 
    - Transactions
    - `__repr__`
    - Creating Records
        - Seeding Data
    - Reading Records
        - Selecting Specific Columns
        - Ordering
        - Limits
        - Filtering 
        - Func
    - Updating Data
    - Deleting Data

## 8: SQLAlchemy Associations
### Lecture Goals:
- Review relationships, Primary keys, and Foreign keys
- Demonstrate creating a table with a Foreign key and referencing another table using `relationship()` and `backref()`
- Demonstrate using Alembic to generate tables with relationships 
- Demonstrate querying methods to view table relationships
- Demonstrate a “one to many” association
- Demonstrate a “many to many” association with a join model 
- Stretch Goal
    - Demonstrate using a CLI to access a backend application

### Lecture Topics:
- Design Database Tables
- One-to-Many 
- Foreign Key Columns 
- `relationship()` and `backref()`
- One-to-One
- Alembic Migrations to Generate Table Relationships
- Relation Query Methods 
- Many-to-Many 
- Stretch Topic
    - Making a CLI

