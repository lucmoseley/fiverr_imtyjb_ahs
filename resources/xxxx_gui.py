# xxxx_gui.py
# xxx := name of person

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox

# #################################################
# Import any of your classes defined in other files
# #################################################

# From file xxx.py import class Xxxx
from xxxx_dao import XxxxDAO

# #################
# PersonGUI Class
# #################

class XxxxGUI():
    """GUI class to perform CRUD operations on the person table in the database"""

    def __init__(self):   
        """Initialiser"""
        pass 

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.
        """
        pass

    def clear_fields(self):
        """Clear the fields of the form"""
        pass

    def save(self):
        """Save the data displayed on the form to the database."""
        pass

    def get_fields(self):
        """Get the data entered in the fields of the form"""
        pass

    def create(self, data):
        """Create a new record in the database"""
        pass

    def update(self, data):
       """Update a record in the database"""
       pass

    def delete(self):
        """Delete a record from the database"""
        pass

    def load(self):
        """Retrieve a list of IDs from the database and load them into a listbox"""
        pass

    def on_list_select(self, evt):
        """on_list_select() is triggered when a user clicks an item in the listbox"""
        pass


    def populate_fields(self, person):
        """Populate the fields of the form with data"""
        pass

    def validate_fields(self, data):
        """
        Validate the data entered in the fields of the form"""
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """The main method is only executed when the file is 'run' (not imported in another file)"""
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("XXXXXX System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = XxxxGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass
