# create_tables.py
# France Cheong
# 14/09/2021


# ###########
# 1. Libraries
# ###########

import sqlite3


# ###########
# 2. Constants
# ###########
DATABASE_URI = "medical_centre.db"


# For AUTOINCREMENTED PK (whether implied or not)
# Must provide a value of the PK (unlike SQLAlchemy which does not require one)
# If the value is None, it will be autoincremented from the last one inserted
# However, if a value is specified, that value will be inserted

# employee_id INTEGER PRIMARY KEY, 
# Will also create a PK that is AUTOINCREMENTED
DOCTOR_SQL = """
    CREATE TABLE doctor (
        doc_id          INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_firstname   VARCHAR(20) NOT NULL,
        doc_lastname    VARCHAR(50) NOT NULL,
        doc_email       VARCHAR(50) NOT NULL UNIQUE, 
        doc_mobile      VARCHAR(20) NOT NULL UNIQUE
)
"""


PATIENT_SQL = """
    CREATE TABLE patient (
        patient_id          INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_firstname   VARCHAR(20) NOT NULL,
        patient_lastname    VARCHAR(50) NOT NULL,
        patient_title       VARCHAR(10) NOT NULL,
        patient_email       VARCHAR(50) NOT NULL UNIQUE, 
        patient_mobile      VARCHAR(20) NOT NULL UNIQUE
)
"""

APPOINTMENT_SQL = """
    CREATE TABLE appointment (
        appt_id                 INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id                  INTEGER NOT NULL,
        patient_id              INTEGER NOT NULL,
        appt_date               VARCHAR(10) NOT NULL,
        appt_time               VARCHAR(10) NOT NULL,
        appt_notes              VARCHAR(255),
        FOREIGN KEY(doc_id)     REFERENCES doctor(doc_id),
        FOREIGN KEY(patient_id) REFERENCES patient(patient_id)
)
"""

"""
Please note that SQLite does not enforce foreign key constraints by default
To enable it, need to execute the following command after you connect to the database
    PRAGMA foreign_keys = 1

e.g.
conn=sqlite3.connect("yourdatabase.db")
conn.execute("PRAGMA foreign_keys = 1")
cur=conn.cursor()

"""

# ###########
# 3. Functions
# ###########




# ###########
# 4. Main method
# ###########

if __name__ == '__main__':

    print("Creating the database and tables") 
    print("Please ensure that you've deleted medical_centre.db in the currect folder")

    print()
    input("Press Enter to continue or Ctrl+C to cancel ...")

    # Open a connection
    conn = sqlite3.connect(DATABASE_URI)
    print(f"Opened a connection to database {DATABASE_URI}")

    with conn:
        # Get a cursor
        cur = conn.cursor()
        print("Got a cursor to the connection")

        # 1. Create the doctor table
        cur.execute(DOCTOR_SQL)
        print(f"Doctor table created in database {DATABASE_URI}")

        # 2. Create the patient table
        cur.execute(PATIENT_SQL)
        print(f"Patient table created in database {DATABASE_URI}")

        # 3. Create the appoitment table
        cur.execute(APPOINTMENT_SQL)
        print(f"Apppointment table created in database {DATABASE_URI}")

           

    print("\nAll done!")                    

    print("\nPlease use DB Browser for SQLite to check the database!")  