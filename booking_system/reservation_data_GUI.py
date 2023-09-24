import tkinter as tk
from tkinter import messagebox
from reservation_data_DAO import ReservationDAO

class ReservationDataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation Data Management")

        self.dao = ReservationDAO()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.booking_reference_label = tk.Label(self.root, text="Booking Reference:")
        self.booking_reference_label.grid(row=0, column=0)
        self.staff_member_initials_label = tk.Label(self.root, text="Staff Member Initials:")
        self.staff_member_initials_label.grid(row=1, column=0)
        self.customer_name_label = tk.Label(self.root, text="Customer Name:")
        self.customer_name_label.grid(row=2, column=0)
        self.arrival_date_label = tk.Label(self.root, text="Arrival Date:")
        self.arrival_date_label.grid(row=3, column=0)
        self.departure_date_label = tk.Label(self.root, text="Departure Date:")
        self.departure_date_label.grid(row=4, column=0)
        self.booking_length_label = tk.Label(self.root, text="Booking Length:")
        self.booking_length_label.grid(row=5, column=0)
        self.reservation_status_label = tk.Label(self.root, text="Reservation Status:")
        self.reservation_status_label.grid(row=6, column=0)
        self.repeat_customer_flag_label = tk.Label(self.root, text="Repeat Customer Flag:")
        self.repeat_customer_flag_label.grid(row=7, column=0)
        self.num_adults_label = tk.Label(self.root, text="Number of Adults:")
        self.num_adults_label.grid(row=8, column=0)
        self.num_children_label = tk.Label(self.root, text="Number of Children:")
        self.num_children_label.grid(row=9, column=0)
        self.num_infants_label = tk.Label(self.root, text="Number of Infants:")
        self.num_infants_label.grid(row=10, column=0)
        self.num_rooms_booked_label = tk.Label(self.root, text="Number of Rooms Booked:")
        self.num_rooms_booked_label.grid(row=11, column=0)
        self.room_name_label = tk.Label(self.root, text="Room Name:")
        self.room_name_label.grid(row=12, column=0)
        self.promo_code_flag_label = tk.Label(self.root, text="Promo Code Flag:")
        self.promo_code_flag_label.grid(row=13, column=0)
        self.total_price_label = tk.Label(self.root, text="Total Price:")
        self.total_price_label.grid(row=14, column=0)

        # Entry Fields
        self.booking_reference_entry = tk.Entry(self.root)
        self.booking_reference_entry.grid(row=0, column=1)
        self.staff_member_initials_entry = tk.Entry(self.root)
        self.staff_member_initials_entry.grid(row=1, column=1)
        self.customer_name_entry = tk.Entry(self.root)
        self.customer_name_entry.grid(row=2, column=1)
        self.arrival_date_entry = tk.Entry(self.root)
        self.arrival_date_entry.grid(row=3, column=1)
        self.departure_date_entry = tk.Entry(self.root)
        self.departure_date_entry.grid(row=4, column=1)
        self.booking_length_entry = tk.Entry(self.root)
        self.booking_length_entry.grid(row=5, column=1)
        self.reservation_status_entry = tk.Entry(self.root)
        self.reservation_status_entry.grid(row=6, column=1)
        self.repeat_customer_flag_entry = tk.Entry(self.root)
        self.repeat_customer_flag_entry.grid(row=7, column=1)
        self.num_adults_entry = tk.Entry(self.root)
        self.num_adults_entry.grid(row=8, column=1)
        self.num_children_entry = tk.Entry(self.root)
        self.num_children_entry.grid(row=9, column=1)
        self.num_infants_entry = tk.Entry(self.root)
        self.num_infants_entry.grid(row=10, column=1)
        self.num_rooms_booked_entry = tk.Entry(self.root)
        self.num_rooms_booked_entry.grid(row=11, column=1)
        self.room_name_entry = tk.Entry(self.root)
        self.room_name_entry.grid(row=12, column=1)
        self.promo_code_flag_entry = tk.Entry(self.root)
        self.promo_code_flag_entry.grid(row=13, column=1)
        self.total_price_entry = tk.Entry(self.root)
        self.total_price_entry.grid(row=14, column=1)

        # Buttons
        self.create_button = tk.Button(self.root, text="Create Reservation", command=self.create_reservation)
        self.create_button.grid(row=15, column=0, columnspan=2)
        self.read_button = tk.Button(self.root, text="Read Reservation", command=self.read_reservation)
        self.read_button.grid(row=16, column=0, columnspan=2)
        self.update_button = tk.Button(self.root, text="Update Reservation", command=self.update_reservation)
        self.update_button.grid(row=17, column=0, columnspan=2)
        self.delete_button = tk.Button(self.root, text="Delete Reservation", command=self.delete_reservation)
        self.delete_button.grid(row=18, column=0, columnspan=2)

    def create_reservation(self):
        # Retrieve data from entry fields and create a reservation
        booking_reference = self.booking_reference_entry.get()
        staff_member_initials = self.staff_member_initials_entry.get()
        customer_name = self.customer_name_entry.get()
        arrival_date = self.arrival_date_entry.get()
        departure_date = self.departure_date_entry.get()
        booking_length = int(self.booking_length_entry.get())
        reservation_status = self.reservation_status_entry.get()
        repeat_customer_flag = self.repeat_customer_flag_entry.get()
        num_adults = int(self.num_adults_entry.get())
        num_children = int(self.num_children_entry.get())
        num_infants = int(self.num_infants_entry.get())
        num_rooms_booked = int(self.num_rooms_booked_entry.get())
        room_name = self.room_name_entry.get()
        promo_code_flag = self.promo_code_flag_entry.get()
        total_price = int(self.total_price_entry.get())

        reservation_data = (
            booking_reference,
            staff_member_initials,
            customer_name,
            arrival_date,
            departure_date,
            booking_length,
            reservation_status,
            repeat_customer_flag,
            num_adults,
            num_children,
            num_infants,
            num_rooms_booked,
            room_name,
            promo_code_flag,
            total_price,
        )

        if self.dao.create_reservation(reservation_data):
            messagebox.showinfo("Success", "Reservation created successfully.")
        else:
            messagebox.showerror("Error", "Reservation with the same booking reference already exists.")

    def read_reservation(self):
        booking_reference = self.booking_reference_entry.get()
        reservation = self.dao.read_reservation(booking_reference)
        if reservation:
            # Display reservation details in a messagebox or a label
            messagebox.showinfo("Reservation Details", f"Booking Reference: {reservation[0]}\n"
                                                        f"Staff Member Initials: {reservation[1]}\n"
                                                        f"Customer Name: {reservation[2]}\n"
                                                        f"Arrival Date: {reservation[3]}\n"
                                                        f"Departure Date: {reservation[4]}\n"
                                                        f"Booking Length: {reservation[5]}\n"
                                                        f"Reservation Status: {reservation[6]}\n"
                                                        f"Repeat Customer Flag: {reservation[7]}\n"
                                                        f"Number of Adults: {reservation[8]}\n"
                                                        f"Number of Children: {reservation[9]}\n"
                                                        f"Number of Infants: {reservation[10]}\n"
                                                        f"Number of Rooms Booked: {reservation[11]}\n"
                                                        f"Room Name: {reservation[12]}\n"
                                                        f"Promo Code Flag: {reservation[13]}\n"
                                                        f"Total Price: {reservation[14]}\n"
                                )
        else:
            messagebox.showerror("Error", "Reservation not found.")

    def update_reservation(self):
        # Retrieve data from entry fields and update a reservation
        booking_reference = self.booking_reference_entry.get()
        staff_member_initials = self.staff_member_initials_entry.get()
        customer_name = self.customer_name_entry.get()
        arrival_date = self.arrival_date_entry.get()
        departure_date = self.departure_date_entry.get()
        booking_length = int(self.booking_length_entry.get())
        reservation_status = self.reservation_status_entry.get()
        repeat_customer_flag = self.repeat_customer_flag_entry.get()
        num_adults = int(self.num_adults_entry.get())
        num_children = int(self.num_children_entry.get())
        num_infants = int(self.num_infants_entry.get())
        num_rooms_booked = int(self.num_rooms_booked_entry.get())
        room_name = self.room_name_entry.get()
        promo_code_flag = self.promo_code_flag_entry.get()
        total_price = int(self.total_price_entry.get())

        updated_data = (
            staff_member_initials,
            customer_name,
            arrival_date,
            departure_date,
            booking_length,
            reservation_status,
            repeat_customer_flag,
            num_adults,
            num_children,
            num_infants,
            num_rooms_booked,
            room_name,
            promo_code_flag,
            total_price,
        )

        if self.dao.update_reservation(booking_reference, updated_data):
            messagebox.showinfo("Success", "Reservation updated successfully.")
        else:
            messagebox.showerror("Error", "Reservation not found.")

    def delete_reservation(self):
        booking_reference = self.booking_reference_entry.get()
        self.dao.delete_reservation(booking_reference)
        messagebox.showinfo("Success", "Reservation deleted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationDataGUI(root)
    root.mainloop()
