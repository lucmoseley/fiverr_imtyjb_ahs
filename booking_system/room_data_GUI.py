import tkinter as tk
from tkinter import messagebox
from room_data_DAO import RoomDataDAO

class RoomDataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Data Management")

        self.dao = RoomDataDAO()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.room_name_label = tk.Label(self.root, text="Room Name:")
        self.room_name_label.grid(row=0, column=0)
        self.adult_capacity_label = tk.Label(self.root, text="Adult Capacity:")
        self.adult_capacity_label.grid(row=1, column=0)
        self.child_capacity_label = tk.Label(self.root, text="Child Capacity:")
        self.child_capacity_label.grid(row=2, column=0)
        self.base_cost_label = tk.Label(self.root, text="Base Cost:")
        self.base_cost_label.grid(row=3, column=0)
        self.child_cot_cost_label = tk.Label(self.root, text="Child Cot Cost:")
        self.child_cot_cost_label.grid(row=4, column=0)
        self.view_type_label = tk.Label(self.root, text="View Type:")
        self.view_type_label.grid(row=5, column=0)

        # Entry Fields
        self.room_name_entry = tk.Entry(self.root)
        self.room_name_entry.grid(row=0, column=1)
        self.adult_capacity_entry = tk.Entry(self.root)
        self.adult_capacity_entry.grid(row=1, column=1)
        self.child_capacity_entry = tk.Entry(self.root)
        self.child_capacity_entry.grid(row=2, column=1)
        self.base_cost_entry = tk.Entry(self.root)
        self.base_cost_entry.grid(row=3, column=1)
        self.child_cot_cost_entry = tk.Entry(self.root)
        self.child_cot_cost_entry.grid(row=4, column=1)
        self.view_type_entry = tk.Entry(self.root)
        self.view_type_entry.grid(row=5, column=1)

        # Buttons
        self.create_button = tk.Button(self.root, text="Create Room", command=self.create_room)
        self.create_button.grid(row=6, column=0, columnspan=2)
        self.read_button = tk.Button(self.root, text="Read Room", command=self.read_room)
        self.read_button.grid(row=7, column=0, columnspan=2)
        self.update_button = tk.Button(self.root, text="Update Room", command=self.update_room)
        self.update_button.grid(row=8, column=0, columnspan=2)
        self.delete_button = tk.Button(self.root, text="Delete Room", command=self.delete_room)
        self.delete_button.grid(row=9, column=0, columnspan=2)

    def create_room(self):
        room_name = self.room_name_entry.get()
        adult_capacity = int(self.adult_capacity_entry.get())
        child_capacity = int(self.child_capacity_entry.get())
        base_cost = int(self.base_cost_entry.get())
        child_cot_cost = int(self.child_cot_cost_entry.get())
        view_type = self.view_type_entry.get()

        if self.dao.create_room(room_name, adult_capacity, child_capacity, base_cost, child_cot_cost, view_type):
            messagebox.showinfo("Success", "Room created successfully.")
        else:
            messagebox.showerror("Error", "Room with the same name already exists.")

    def read_room(self):
        room_name = self.room_name_entry.get()
        room = self.dao.read_room(room_name)
        if room:
            messagebox.showinfo("Room Details", f"Room Name: {room['room_name']}\n"
                                                f"Adult Capacity: {room['adult_capacity']}\n"
                                                f"Child Capacity: {room['child_capacity']}\n"
                                                f"Base Cost: {room['base_cost']}\n"
                                                f"Child Cot Cost: {room['child_cot_cost']}\n"
                                                f"View Type: {room['view_type']}")
        else:
            messagebox.showerror("Error", "Room not found.")

    def update_room(self):
        room_name = self.room_name_entry.get()
        adult_capacity = int(self.adult_capacity_entry.get())
        child_capacity = int(self.child_capacity_entry.get())
        base_cost = int(self.base_cost_entry.get())
        child_cot_cost = int(self.child_cot_cost_entry.get())
        view_type = self.view_type_entry.get()

        if self.dao.update_room(room_name, adult_capacity, child_capacity, base_cost, child_cot_cost, view_type):
            messagebox.showinfo("Success", "Room updated successfully.")
        else:
            messagebox.showerror("Error", "Room not found.")

    def delete_room(self):
        room_name = self.room_name_entry.get()
        self.dao.delete_room(room_name)
        messagebox.showinfo("Success", "Room deleted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RoomDataGUI(root)
    root.mainloop()
