# main_gui.py
# France Cheong
# 11/10/2020

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox

# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option

# From file xxx.py import class Xxxx
from doctor_gui import DoctorGUI

# ################
# Global Constants 
# ################


# ####################
# MainGUI Class
# ####################

class MainGUI():

    def __init__(self):   

        print("Creating Main GUI ...")

        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("Main System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Person menu
        # do not use self.create_person_gui()
        # Will be executed automatically!
        menubar.add_command(label="Doctor", command=self.create_doctor_gui)

        # Display the menu
        self.root.config(menu=menubar)

        pass
    
    
    """
    # Beware: There is a built-in function called exit() 
    # with no argument
    def exit(self):
        answer = messagebox.askyesno('Procurement System', 
                    'Are you sure you want to exit?', icon="warning")
        if answer:
            self.root.destroy()
            exit()    
    """        
            
    # Functions to create child frames 
    # when menu options are selected
    def create_doctor_gui(self):

        print("\nCreating doctor GUI ...")

        # Destroy whatever the current GUI is 

        # and create the doctor GUI

        if self.current_gui:

            self.current_gui.destroy()

        doctor_gui = DoctorGUI()

        self.current_gui = doctor_gui.create_gui(self.root)




# ###########
# Main method
# ###########

if __name__ == '__main__':

    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = MainGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
