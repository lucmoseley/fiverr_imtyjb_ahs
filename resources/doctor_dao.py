# doctor_dao.py
# France Cheong
# 11/10/2021
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = 'medical_centre.db'

class DoctorDAO():

    def create(self, data):

        # Print info for debugging
        print("\nCreating a doctor ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Using Parameterized Query i.e. question marks as placeholders for the actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO doctor VALUES (?, ?, ?, ?, ?);" # doctor table has 5 attributes
            param_tuple = (
                None, # doc_id is set to None for database to autoincrement
                data['doc_firstname'], 
                data['doc_lastname'],  
                data['doc_email'], 
                data['doc_mobile'])
            cur.execute(query, param_tuple)
            result['message'] = 'Doctor added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_doc_id = cur.lastrowid
            print(f"inserted_doc_id: {inserted_doc_id}")
            result['doc_id'] = inserted_doc_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create doctor failed!' 
            print(f"Database {DATABASE_URI} - Create doctor failed!")
            print(error)
        finally:
            # The finally block is always executed - even if an exception happened
            # This is the ideal place to close the connection
            # It's always a good idea to check if the object exists before calling a method/function from the object
            # Invoking a method on object which does not exist will cause your code to crash
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary  

    def find_by_id(self, doc_id):

        # Print info for debugging
        print("\nFinding a doctor ...\n")
        print(f"doc_id: {doc_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM doctor WHERE doc_id=?;"
            #param_tuple = (doc_id) # Does not work as it's converted to an int, need the comma at the end
            param_tuple = (doc_id, ) # Works as this is a tuple of length 1
            cur.execute(query, param_tuple)
            row = cur.fetchone() # get the next row - there would be just one row returned by the database
            if row:
                # cursor.description contains the name of the columns
                # Use dictionary compejension to build the dictionary
                # Use list comprehension to get the list of column names from cursor.description
                # The column name is at index 0 i.e. the first position
                col_names = [description[0] for description in cur.description]
                #print(f"Column names: {col_names}")
                # Using dictionary comprehension and enumerate() to match the column names with their index positions
                d = {key: row[i] for i, key in enumerate(col_names)} # works
                result['doctor'] = d
            else:    
                result['message'] = "Doctor not found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by id failed!' 
            print(f"Database {DATABASE_URI} - Find by id failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        #print(f"result: {result}")
        return result # return the result as a dictionary

    def find_by_lastname(self, lastname): 

        # Print info for debugging
        print("\nFinding doctors(s) by lastname ...\n")
        print(f"lastname: {lastname}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            #query = "SELECT * FROM doctor WHERE doc_lastname LIKE ?" # Partial match
            query = "SELECT * FROM doctor WHERE doc_lastname = ?;" # exact match
            param_tuple = (lastname, )
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['doctors'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one doctors - so create a list
                list_doctors = [] # Create an empty list to append doctor dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary compejension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    d = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_doctors.append(d) # Append the doctor dict to the doctor list
                      
                # Store the doctor list in the result dict under key "doctors"              
                result['doctors'] = list_doctors              

            else:    
                result['message'] = "No doctors found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by lastname failed!' 
            print(f"Database {DATABASE_URI} - Find by lastname failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):

        # Print info for debugging
        print("\nFinding all doctors ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM doctor;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                #result['doctors'] = rows # Issue: will return a list of tuples - need a list of dicts

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one doctors - so create a list
                list_doctors = [] # Create an empty list to append doctors dicts
                for x in rows: # rows is a list of SQLite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary comprehension to build the dictionary
                    # Use list comprehension to get the list of column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() to match the column names with their index positions
                    d = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_doctors.append(d) # Append the doctor dict to the doctor list
                    pass     

                # After the for loop
                # Store the doctoe list in the result dict under key "doctors" - PLURAL             
                result['doctors'] = list_doctors    
            else:    
                result['message'] = "No doctors found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find all failed!' 
            print(f"Database {DATABASE_URI} - Find all failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")    
        return result # return the result as a dictionary


    def find_ids(self):
        """
        This is a special method similar to find_all but returns doc_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all doctor ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT doc_id FROM doctor;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['doctor_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No doctors found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find ids failed!' 
            print(f"Database {DATABASE_URI} - Find ids failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}") 
        return result # return the result as a dictionary

    def update(self, doc_id, data):

        # Print info for debugging
        print("\nUpdating doctor ...\n")
        print(f"doc_id: {doc_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in doctor table except doc_id
            query = """UPDATE doctor
               SET 
                  doc_firstname=?, 
                  doc_lastname=?, 
                  doc_email=?, 
                  doc_mobile=? 
               WHERE 
                  doc_id = ?;"""
            param_tuple = (
                data['doc_firstname'], 
                data['doc_lastname'], 
                data['doc_email'], 
                data['doc_mobile'], 
                doc_id)
            cur.execute(query, param_tuple)
            result['message'] = 'Doctor Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Doctor NOT updated!' 
            print(f"Database {DATABASE_URI} - Update doctor failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, doc_id):

        # Print info for debugging
        print("\nDeleting doctor ...\n")
        print(f"doc_id: {doc_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "DELETE FROM doctor WHERE doc_id = ?;"
            param_tuple = (doc_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'Doctor deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Doctor NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete doctor failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    