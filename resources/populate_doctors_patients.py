# populate_doctors_patients.py
# France Cheong
# 11/10/2021


# ###########
# 1. Libraries
# ###########

import sqlite3


# ###########
# 2. Constants
# ###########
DATABASE_URI = "medical_centre.db"


# ###########
# 3. Functions
# ###########

def populate_doctors(cur):

    # List of doctors
    doctors = [
        {
            "doc_id"        : None, 
            "doc_firstname" :"John", 
            "doc_lastname"  : "Ranson", 
            "doc_email"     :"john.ranson@gmail.com", 
            "doc_mobile"    : "+61 422 834 246"
        },

        {
            "doc_id"        : None, 
            "doc_firstname" :"Aidan", 
            "doc_lastname"  : "Timms", 
            "doc_email"     :"aidan.timms@gmail.com", 
            "doc_mobile"    : "+61 413 224 322"
        },

        {
            "doc_id"        : None, 
            "doc_firstname" :"Eva", 
            "doc_lastname"  : "Mocatta", 
            "doc_email"     :"eva.mocatta@gmail.com", 
            "doc_mobile"    : "+61 560 345 233"
        },

        # More doctors if any

    ]

    sql = "INSERT INTO doctor VALUES (?, ?, ?, ?, ?);" # 5 values
    for doc in doctors:    
        print(f"\nInserting: {doc}")
        param_tuple = [value for value in doc.values()] # Cant' use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)

def populate_patients(cur):

    # List of patients
    patients = [

        {
            "patient_id"        : None, 
            "patient_firstname" : "Jamie", 
            "patient_lastname"  : "Farleigh", 
            "patient_title"     : "Mr",
            "patient_email"     : "jamie.farleigh@gmail.com",
            "patient_mobile"    : "+61 340 371 432",
        },

        {
            "patient_id"        : None, 
            "patient_firstname" : "Jade", 
            "patient_lastname"  : "Baldessin", 
            "patient_title"     : "Ms",
            "patient_email"     : "jade.balsessin@gmail.com",
            "patient_mobile"    : "+61 355 713 555",
        },

        {
            "patient_id"        : None, 
            "patient_firstname" : "Emma", 
            "patient_lastname"  : "Stonham", 
            "patient_title"     : "Ms",
            "patient_email"     : "emma.stonham@gmail.com",
            "patient_mobile"    : "+61 032 675 111",
        },

        # More doctors if any

    ]

    sql = "INSERT INTO patient VALUES (?, ?, ?, ?, ?, ?);" # 6 values
    for patient in patients:    
        print(f"\nInserting: {patient}")
        param_tuple = [value for value in patient.values()] # Cant' use a tuple, use a list
        print(f"param_tuple: {param_tuple}")
        cur.execute(sql, param_tuple)



# ###########
# 4. Main method
# ###########

if __name__ == '__main__':

    print("\nPopulating tables ....") 

    input("\nPress Enter to continue or Ctrl+C to cancel ...")

    # Open a connection
    conn = sqlite3.connect(DATABASE_URI)

    with sqlite3.connect(DATABASE_URI) as conn:
        print(f"Opened a connection to database {DATABASE_URI}")

        # 1. Get a cursor
        cur = conn.cursor()
        print("Got a cursor to the connection")

        # 2. Populate doctor table
        populate_doctors(cur)
        print(f"Doctor table populated in database {DATABASE_URI}")

        # 3. Populate patient table
        populate_patients(cur)
        print(f"Patient table populated in database {DATABASE_URI}")

        # 4. Save the records
        conn.commit()

        # No need to close the cursor and connection when using the with statement
        # Will be closed automatically

    print("\nAll done!")                    