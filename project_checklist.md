# General instructions
Design information system  
Develop information system in Python:  
- must have layers that include:  
    - data layer -- communicates with database and makes data available on request  
    - interface layer -- interfaces with the data layer via a GUI  
    - validation code module! that can be plugged into the GUI  
- all layers must include "test methods" that ensure code is operating correctly  
Generate "analysis and design" documentation  
Write an instruction manual  
Justify all best practices used in the system created  
Code should be tested for boundary and extreme conditions (what does this mean?)
PEP-8 naming conventions should be used everywhere (there are PEP8 checkers & explainers!)  

# Data layer instructions
Write a python script to programmatically create a SQLite database and all its tables  
- can be one script or multiple to populate tables

As part of this step, you should inspect the database created by the python script using DB Browser for SQLite  

## Data access object (part of data layer) instructins
One DAO per data table (only need for 2, not all)  
- one must be for a table without foreign keys  
- one must be for a table with foreign keys (foreign keys has something to do with accessing other tables)  

DAOs Must be OOP classes  
These DAOs must each be able to create, read, update and delete items from tables  
DAOs must have assocaited test files/methods to ensure they work properly (setUp tables and test things go well)  
All data entered must be validated  
- check if email is valid email, credit card, etc.
- check if functions that do x really do x

# Interface layer (GUI) instructions  
One GUI for each of the two DAOs made  

# Testing specific instructions
Use and expand the validation methods given in validation.py  
For all new methods added to validation.py, add tests in validation_test.py  
Can re-structure these, this just gives a nice starting library  

# Instruction manual (system documentation)

# Best practices document  