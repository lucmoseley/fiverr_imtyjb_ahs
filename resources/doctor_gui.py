# doctor_gui.py

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter
import tkinter.ttk as ttk # for combobox

# #################################################
# Import any of your classes defined in other files
# #################################################

# From file xxx.py import class Xxxx
from doctor_dao import DoctorDAO

# #################
# DoctorGui Class
# #################

class DoctorGUI():
    """GUI class to perform CRUD operations on the doctor table in the database"""

    def __init__(self):   
        """Initialiser"""
    
        # Instantiate a data access object 
        # Contains methods to access the database
        self.doctor_dao = DoctorDAO()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.doc_id = tk.StringVar()
        self.doc_firstname = tk.StringVar()
        self.doc_lastname = tk.StringVar()
        self.doc_email = tk.StringVar()
        self.doc_mobile = tk.StringVar()

        # Option 1. manual type of foreign key required
        # List of doctor ids - lb for listbox
        # self.lb_ids = None

        # Option 2. select a dropdown option required
        # self.lb_ids = tk.StringVar()
    

        # Messagebox title
        self.mb_title_bar = "Doctor CRUD"

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.
        Notice that the "root" window is passed the second parameter in the 
        method header.
        Also notice that the first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """

        # Good practice to print something at the start of the method 
        # e.g. which method is being executed, the values of parameters passes, 
        # etc
        # Good for tracing the execution of the program while debugging it
        # After debugging, you may want to "comment out" some of the 
        # print statements so that they do not execute and print too 
        # much stuff in the console
        print("\nCreating doctor GUI ...")

        # doctor_frame = tk.Frame(root).pack() 
        # cannot write the above as pack() does not return anything
        # and need the variable name to refer to it elsewhere
        # DO NOT SPECIFY ANY WIDTH AND HEIGHT OF THE FRAMES 
        # HERE FOR FLEXIBILITY REASONS
        # The height and width or the root window can be specified 
        # in the main GUI (or in the main() method)
        doctor_frame = tk.Frame(root)
        doctor_frame.pack()

        # Add a frame to contain the form widgets
        # To put a number of widgets in a column one on top of the other, 
        # just use pack() without any options
        # Use the fill=tk.X option to make all widgets as wide as the parent widget
        # To pack widgets side by side, use the side option 
        # e.g. side=tk.LEFT, tk.BOTTOM, tk.RIGHT (default is tk.TOP)
        # Use the fill=tk.Y option to make all widgets as tall as the parent widget
        # have also fill=tk.BOTH option
        # The anchor= option is used to position the widget in the container, 
        # default is tk.CENTER
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding arounf widgets: padx= pady=  default is 0
        form_frame = tk.Frame(doctor_frame)
        form_frame.pack()
    
        # row 0:  title label
        # The variable name is not needed
        # By default, the text is centered
        # To right align use anchor=e (east) not justify=RIGHT which is used 
        # for aligning multiple lines
        # Labels have padx= and pady= options but no ipadx= and ipady=
        # Check the ulr above, to finc out more about the many options 
        # available for configuring labels!!!
        # STICK TO THE DEFAULT VALUES,  
        # UNLESS YOU HAVE A GOOD REASON TO CHANGE THEM!!!!!!!!!!!!!!!!
        # For spanning multiple rows and columns, 
        # use rowspan= and columnspan= options (default is 1)
        # Use the sticky= option for positioning 
        # (instead of anchor= as used in pack) - 
        # (default is centered) values are: n, w, e, w, nw, etc
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding around widgets: padx= pady=  default is 0
        # Use the width= option to specify how wide in terms of number of characters
        tk.Label(
            form_frame, 
            font=('arial', 12), 
            text = "Doctor").grid(row=0, column=0, columnspan=3)

        # row 1: doc_id label, doc_id entry and list_of_ids label
        tk.Label(
            form_frame, 
            text= "Doctor Id", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=1, column=0)
        # Need to use both padx and pady to leave a vertical space between rows of labels
        # And a space between the  label and its entry field
        # Entry has no padding options
        # Use the width= option to specify how wide in terms of number of characters
        tk.Entry(
            form_frame, 
            textvariable=self.doc_id, 
            width=30, 
            bd=1, 
            state=tk.DISABLED).grid(row=1, column=1)
        # doc_id is disabled to prevent user from entering a value
        # doc_id is generated by the database because AUTOINCREMENT 
        # was specified in the database schema
        tk.Label(
            form_frame, 
            text= "Doctor IDs", 
            font=('arial', 10)).grid(row=1, column=2)
        
        # row 2: firstname label, firstname entry and listbox of ids
        tk.Label(
            form_frame, 
            text= "First name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=2, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.doc_firstname, 
            width=30, 
            bd=1).grid(row=2, column=1)
        # Use the height= option to specify the height, default is 10
        # Use the width= option to specify the number of characters, default is 20
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=5) 
        # 'self' means instance attribute rather than local variable
        # since python allows using variables before they are declared
        # it does not matter whether lb_ids has been declared or not at the 
        # top of the file before the methods definition
        # Set the method to be called when an item is clicked on the listbox 
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        # row 3: lastname label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Last name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=3, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.doc_lastname, 
            width=30, 
            bd=1).grid(row=3, column=1)

        # row 4: email label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Email", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=4, column=0) # ***you have to specify row to avoid overwrite!
        tk.Entry(
            form_frame, 
            textvariable=self.doc_email, 
            width=30, 
            bd=1).grid(row=4, column=1) # ***you have to specify row to avoid overwrite!

        # row 4: email label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Mobile", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=5, column=0) 
        tk.Entry(
            form_frame, 
            textvariable=self.doc_mobile, 
            width=30, 
            bd=1).grid(row=5, column=1)

        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid with row 
        # and col locations
        # pady to leave a space from frame on top
        button_frame = tk.Frame(doctor_frame, pady=10) 
        button_frame.pack()
        # Use the anchor= option to position the button
        # External padding around buttons: padx= pady=  default is 0
        # Use the width= option to specify the number of characters, 
        # otherwise calculated based on text width
        tk.Button(
            button_frame, 
            width=10, text="Clear", 
            command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Save", 
            command=self.save).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Delete", 
            command=self.delete).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Load", 
            command=self.load).pack(side=tk.LEFT)       

        # Return a reference to the high level frame created
        # Will need the reference to be able to destroy it in the calling function
        return doctor_frame

    def clear_fields(self):
        """Clear the fields of the form"""

        print("\nClearing fields ...")

        # Just blank all the fields
        self.doc_id.set("")
        self.doc_firstname.set("")
        self.doc_lastname.set("")
        self.doc_email.set("")
        self.doc_mobile.set("")

    def save(self):
        """Save the data displayed on the form to the database."""

        print("\nSaving a doctor ...")

        # Get the data
        data = self.get_fields()   

        if (len(data['doc_id'])==0):
            print("Calling create() as docid is absent")
            self.create(data)
        else:
            print("Calling update() as doc_id is present")
            self.update(data) 

    def get_fields(self):
        """Get the data entered in the fields of the form"""

        print("\nGetting fields ...")

        doctor = {}
        # doc_id is ignored when creating a record
        doctor['doc_id'] = self.doc_id.get() 
        doctor['doc_firstname'] = self.doc_firstname.get()
        doctor['doc_lastname'] = self.doc_lastname.get()
        doctor['doc_email'] = self.doc_email.get()
        doctor['doc_mobile'] = self.doc_mobile.get()

        print(f"doctor: {doctor}")
 
        return doctor    

    def create(self, data):
        """Create a new record in the database"""

        print("\nCreating a person ...")
        print(f"data: {data}")

        result = self.doctor_dao.create(data)

        # Display the returned message to the user - use a messagebox
        # Format: message.function(title, message [, options])
        # Functions: showinfo, showwarning, showerror, askquestion, 
        #            askokcancel, askyesno, or askretrycancel
        # Use the icon= option to specify which icon to display 
        # e.g. icon="warning", "error", "info", "question"     
        # Display everything that is returned in the result
        messagebox.showinfo(self.mb_title_bar, result)

    def update(self, data):
        """Update a record in the database"""

        print("\nUpdating a person ...")
        print(f"data: {data}")

        result = self.doctor_dao.update(data['doc_id'], data)

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)

    def delete(self):
        """Delete a record from the database"""

        print("\nDeleting  a person ...")
        
        # Grab the person_id from the stringvar
        id = self.doc_id.get() 
        print(f"id: {id}")
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        result = self.doctor_dao.delete(id)   

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)

    def load(self):
        """Retrieve a list of IDs from the database and load them into a listbox"""
        print("\nLoading IDs in list box ...")

        result = self.doctor_dao.find_ids()
        print(f"result: {result}")

        # Check if there is an entry in the result dictionary

        # Option 1. manual type of foreign key required
        if "doctor_ids" in result: 
            list_ids = result['doctor_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting doc_ids in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                # print(x)
            pass

        # Option 2. select a dropdown option required



    def on_list_select(self, evt):
        """on_list_select() is triggered when a user clicks an item in the listbox"""

        print("\nSelecting an item from the list box ...")

        w = evt.widget

        # index = position of the item clicked in the list, first item is item 0 not 1
        index = int(w.curselection()[0]) 
          
         # value of the item clicked, in our case it's the doc_id  
        value = w.get(index) 
         
        print(f"index: {index}") 
        print(f"value: {value}")

        # Call find_by_id and populate the stringvars of the form
        result = self.doctor_dao.find_by_id(value)

        # { "doctor" : {"doc_id": "", "firstname": "", etc}}
        print(f"result: {result}") 

        # Grab doctor dict from result dict and use it to populate the fields on the form  
        doctor = result['doctor']
        self.populate_fields(doctor)



    def populate_fields(self, doctor):
        """Populate the fields of the form with data"""

        print("\nPopulating fields ...")
        print(f"doctor: {doctor}")

        # Set the values from the dict to the stringvars
        self.doc_id.set(doctor['doc_id'])
        self.doc_firstname.set(doctor['doc_firstname'])
        self.doc_lastname.set(doctor['doc_lastname'])
        self.doc_email.set(doctor['doc_email'])
        self.doc_mobile.set(doctor['doc_mobile'])

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
    root.title("Doctor System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = DoctorGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass
