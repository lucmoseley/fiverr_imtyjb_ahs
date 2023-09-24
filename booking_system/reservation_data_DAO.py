import sqlite3

class ReservationDAO:
    def __init__(self, db_name = 'ahs_reservations.db'):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS reservation_data (
                            booking_reference VARCHAR(40) PRIMARY KEY,
                            staff_member_initials CHAR(2),
                            customer_name VARCHAR(50),
                            arrival_date CHAR(8),
                            departure_date CHAR(8),
                            booking_length INTEGER,
                            reservation_status VARCHAR(9),
                            repeat_customer_flag VARCHAR(1),
                            num_adults INTEGER,
                            num_children INTEGER,
                            num_infants INTEGER,
                            num_rooms_booked INTEGER,
                            room_name CHAR(7),
                            promo_code_flag CHAR(1),
                            total_price INTEGER,
                            FOREIGN KEY(customer_name) REFERENCES cust_data(customer_name),
                            FOREIGN KEY(room_name) REFERENCES room_data(room_name),
                            FOREIGN KEY(room_name) REFERENCES availability_data(room_name)
                        )''')
        conn.commit()
        conn.close()

    def create_reservation(self, reservation_data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO reservation_data (
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
                            total_price
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', reservation_data)
        conn.commit()
        conn.close()

    def read_reservation(self, booking_reference):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservation_data WHERE booking_reference = ?', (booking_reference,))
        reservation = cursor.fetchone()
        conn.close()
        return reservation

    def update_reservation(self, booking_reference, updated_data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''UPDATE reservation_data
                            SET staff_member_initials = ?,
                                customer_name = ?,
                                arrival_date = ?,
                                departure_date = ?,
                                booking_length = ?,
                                reservation_status = ?,
                                repeat_customer_flag = ?,
                                num_adults = ?,
                                num_children = ?,
                                num_infants = ?,
                                num_rooms_booked = ?,
                                room_name = ?,
                                promo_code_flag = ?,
                                total_price = ?
                            WHERE booking_reference = ?''', (*updated_data, booking_reference))
        conn.commit()
        conn.close()

    def delete_reservation(self, booking_reference):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reservation_data WHERE booking_reference = ?', (booking_reference,))
        conn.commit()
        conn.close()

# Example usage:
if __name__ == "__main__":
    db_name = 'ahs_reservations.db'
    res_dao = ReservationDAO(db_name)
    
    # Create table if it doesn't exist
    res_dao.create_table()
    
    # Example data for reservation
    reservation_data = (
        'VP-20-09-22-22-09-22-Room_01-JD-8',
        'VP',
        'John Doe',
        '02-12-22',
        '05-12-22',
        3,
        'completed',
        'Y',
        2,
        1,
        0,
        1,
        'Room_01',
        'N',
        1500
    )
    
    # Create a reservation
    res_dao.create_reservation(reservation_data)
    
    # Read a reservation
    reservation = res_dao.read_reservation('VP-20-09-22-22-09-22-Room_01-JD-8')
    print("Reservation details: ", reservation)
    
    # Update a reservation
    new_res_data = (
        'SM',
        'Jane Smith',
        '03-12-22',
        '07-12-22',
        4,
        'upcoming',
        'N',
        2,
        2,
        0,
        1,
        'Room_02',
        'N',
        1600
    )
    res_dao.update_reservation('VP-20-09-22-22-09-22-Room_01-JD-8', new_res_data)
    updated_res_data = res_dao.read_reservation('VP-20-09-22-22-09-22-Room_01-JD-8')
    print("Updated reservation details: ", updated_res_data)
    
    # Delete a reservation
    deleted_res_data = res_dao.read_reservation('VP-20-09-22-22-09-22-Room_01-JD-8')
    res_dao.delete_reservation('VP-20-09-22-22-09-22-Room_01-JD-8')
    print("Deleted Reservation Data:", deleted_res_data)
