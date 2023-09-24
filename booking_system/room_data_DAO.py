import sqlite3

class RoomDataDAO:
    def __init__(self, db_name = 'ahs_reservations.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS room_data (
            room_name CHAR(7) PRIMARY KEY,
            adult_capacity INTEGER,
            child_capacity INTEGER,
            base_cost INTEGER,
            child_cot_cost INTEGER,
            view_type VARCHAR(6)
        )
        """
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def create_room(
            self, 
            room_name, 
            adult_capacity, 
            child_capacity, 
            base_cost, 
            child_cot_cost, 
            view_type
            ):
        insert_sql = """
        INSERT INTO room_data (
            room_name, 
            adult_capacity, 
            child_capacity, 
            base_cost, 
            child_cot_cost, 
            view_type
            )
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.cursor.execute(
                insert_sql, 
                (room_name, adult_capacity, child_capacity, 
                 base_cost, child_cot_cost, view_type)
                )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Primary key violation (room_name already exists)
            return False

    def read_room(self, room_name):
        select_sql = "SELECT * FROM room_data WHERE room_name = ?"
        self.cursor.execute(select_sql, (room_name,))
        room = self.cursor.fetchone()
        if room:
            return {
                'room_name': room[0],
                'adult_capacity': room[1],
                'child_capacity': room[2],
                'base_cost': room[3],
                'child_cot_cost': room[4],
                'view_type': room[5]
            }
        else:
            return None

    def update_room(
            self, 
            room_name, 
            adult_capacity, 
            child_capacity, 
            base_cost, 
            child_cot_cost, 
            view_type
            ):
        update_sql = """
        UPDATE room_data
        SET adult_capacity = ?, 
            child_capacity = ?, 
            base_cost = ?, 
            child_cot_cost = ?, 
            view_type = ?
        WHERE room_name = ?
        """
        try:
            self.cursor.execute(
                update_sql, 
                (adult_capacity, child_capacity, base_cost, 
                 child_cot_cost, view_type, room_name)
                )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Primary key violation (room_name does not exist)
            return False

    def delete_room(self, room_name):
        delete_sql = "DELETE FROM room_data WHERE room_name = ?"
        self.cursor.execute(delete_sql, (room_name,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Usage example:
if __name__ == "__main__":
    room_dao = RoomDataDAO()

    # Create a new room
    room_dao.create_room('Room_19', 2, 1, 200, 50, 'garden')

    # Read a room's data
    room_data = room_dao.read_room('Room_19')
    print("Room Data:", room_data)

    # Update a room's data
    room_dao.update_room('Room_19', 3, 2, 250, 60, 'city')
    updated_room_data = room_dao.read_room('Room_19')
    print("Updated Room Data:", updated_room_data)

    # Delete a room
    deleted_room_data = room_dao.read_room('Room_19')
    room_dao.delete_room('Room_19')
    print("Deleted Room Data:", deleted_room_data)

    room_dao.close_connection()
