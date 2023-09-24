# User guide for files in this folder  

1. Use create_database.ipynb or create_database.py to generate the database 'ahs_reservations.db'  
    - Database tables come populated with sample data  
    - Recommended to use the notebook version as it is easier to read  

2. reservation_data_DAO.py and room_data_DAO.py are Data Access Objects that can access the tables "reservation_data" and "room_data" within ahs_reservations.db  
    - These include examples on how to execute them  
    - Running "python file_name.py" from the command line will execute the examples  
  
3. reservation_data_GUI.py and room_data_GUI.py are GUIs that plug into the DAOs  
    - Running "python file_name.py" from the command line will launch the relevant GUI  
    - Reservation_data_GUI.py pertains to a table with foreign keys (reservation_data)  