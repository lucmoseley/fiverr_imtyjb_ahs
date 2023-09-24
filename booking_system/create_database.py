# Import relevant modules

import numpy as np
import pandas as pd
import random
import datetime
import names
import ccard
import sqlite3
import sqlalchemy
from sqlalchemy.types import *


# Generate relevant tables with sample data

### Generate table with room data

# Set up a DataFrame 'room_data' to hold room-specific info.

# Create index and column names
room_names_0_9 = ['Room_0{}'.format(i+1) for i in np.arange(9)]
room_names_10_18 = ['Room_{}'.format(i+1) for i in np.arange(9, 18)]
room_names = room_names_0_9 + room_names_10_18
room_details = [
    'adult_capacity', 
    'child_capacity', 
    'base_cost', 
    'child_cot_cost', 
    'view_type'
    ]

# Construct empty DataFrame
room_data = pd.DataFrame(
    index = room_names, 
    columns = room_details
    )
room_data.index.name = 'room_name'


# Populate room_data with sample data

# Set basic data
room_data.loc[:, 'adult_capacity'] = 2
room_data.loc[:, 'child_capacity'] = 2
room_data.loc['Room_01':'Room_09', 'view_type'] = 'garden'
room_data.loc['Room_10':'Room_18', 'view_type'] = 'city'
room_data.loc[:, 'child_cot_cost'] = 20
room_data.loc[:, 'base_cost'] = 100


# Tests/validations?
# make sure all view_types in ['garden', 'city']
# Check final prices are in the 50-200 range
# Check total capacities are <6


### Generate table with customer data

Set up table cust_data to hold customer-specific info.

# Create index and column names
# Make sample data for 1000 example customers
cust_names = list(set(names.get_full_name() for i in range(1000)))
cust_details = [
    'customer_initials',
    'total_visits',
    'credit_card_type',
    'credit_card_number',
    'email',
    'phone_number'
    ]

# Construct empty DataFrame
cust_data = pd.DataFrame(
    index = cust_names,
    columns = cust_details
    )
cust_data.index.name = 'customer_name'


# Populate cust_data with sample data

# Use index to figure out customer initials
cust_data.loc[:, 'customer_initials'] = list(
    map(
        lambda x: '{}'.format(''.join([i[0].upper() for i in x.split()])), 
        cust_data.index
        )
    )

# Assign a random number of total visits between 1 and 7
cust_data.loc[:, 'total_visits'] = np.random.randint(
    low = 1, 
    high = 7, 
    size = cust_data.shape[0]
    )

# Generate sample emails based on customer names
cust_data.loc[:, 'email'] = list(
    map(
        lambda x: '{}@gmail.com'.format('.'.join([i.lower() for i in x.split()])), 
        cust_data.index
        )
    )

# Assign card type as either visa or mastercard to all customers
card_types = ['visa', 'mastercard']
cust_data.loc[:, 'credit_card_type'] = [
    np.random.choice(card_types) for i in range(cust_data.shape[0])
    ]

# Generate appropriate card numbers for customers based on card type
num_visa_cards = np.sum(cust_data['credit_card_type'] == 'visa')
num_master_cards = np.sum(cust_data['credit_card_type'] == 'mastercard')
cust_data.loc[cust_data['credit_card_type'] == 'visa', 'credit_card_number'] = [
    str(ccard.visa()) for i in range(num_visa_cards)
    ]
cust_data.loc[cust_data['credit_card_type'] == 'mastercard', 'credit_card_number'] = [
    str(ccard.mastercard()) for i in range(num_master_cards)
    ]

# Assign random phone numbers to customers
phone_nums = list(
    map(
        str, 
        np.random.randint(
            low = 1000000000, 
            high = 9999999999, 
            size = cust_data.shape[0]
            )
        )
    )
cust_data.loc[:, 'phone_number'] = list(
    map(
        lambda x: '{} {} {}'.format(x[0:2], x[2:6], x[6:10]), 
        phone_nums
        )
    )


# Tests/validations?
# Will need test to make sure first name and last name only entered


### Generate table with reservations data

# Reservation code x (staff member, customer name, num guests, reservation details..., promo code, price)
# - price is more if child

# New entry into reservation table -> generates option for return customer flag if email matches previous, or last name matches


# Set up a DataFrame 'reservation_data' to hold reservation info.

# Create index and column names
reservation_fields = [
    'staff_member_initials',
    'customer_name',
    'arrival_date',
    'departure_date',
    'booking_length',
    'reservation_status',
    'repeat_customer_flag',
    'num_adults',
    'num_children',
    'num_infants', # no charge b/c no cots needed?
    'num_rooms_booked',
    'rooms_booked', # list of room_names
    'promo_code_flag',
    'total_price',
    'booking_reference'
    ]

# Determine total number of reservations using cust_data
num_reservations = sum(cust_data.total_visits)
index_placeholder = np.arange(num_reservations)

# Construct empty DataFrame
reservation_data = pd.DataFrame(
    index = index_placeholder,
    columns = reservation_fields
    )


# Populate reservation_data with sample data

# Assign a random staff member for each reservation
staff_members = ['BR', 'VP', 'KJ', 'JT', 'MT']
reservation_data.loc[:, 'staff_member_initials'] = [
    np.random.choice(staff_members) for i in range(reservation_data.shape[0])
    ]

# Assign a random customer for each reservation
visits_data = cust_data.total_visits
customers = sum(
    [[name] * num_visits 
     for name, num_visits 
     in zip(visits_data.index, visits_data.values)],
    []
    )
random.shuffle(customers)
reservation_data.loc[:, 'customer_name'] = customers

# Assign a random arrival date
# Reservations date range will span last 1 year to 1 month from today
today = datetime.datetime.strptime('20/09/2023', "%d/%m/%Y").date()
date_list = [today + datetime.timedelta(days = x) for x in range(-365, 31)]
reservation_data.loc[:, 'arrival_date'] = [
    np.random.choice(date_list) for i in range(reservation_data.shape[0])
    ]

# Assume stays of uniform probability between 1 and 6 days 
booking_lengths = [
    datetime.timedelta(
        days = np.random.randint(low = 1, 
                                 high = 6
                                )
        ) 
        for i in range(reservation_data.shape[0])
    ]
reservation_data.loc[:, 'departure_date'] = (
    reservation_data.loc[:, 'arrival_date']
    + booking_lengths
    )

# Assign booking lengths
booking_lengths_ints = [x.days for x in booking_lengths]
reservation_data.loc[:, 'booking_length'] = booking_lengths_ints

# Generate reservation statuses based on dates given
# (cancelled/upcoming/active/completed)
reservation_data.loc[:, 'reservation_status'] = 'active'
reservation_data.loc[reservation_data['arrival_date'] > today, 'reservation_status'] = [
    'upcoming']
reservation_data.loc[reservation_data['departure_date'] < today, 'reservation_status'] = [
    'completed']
# Assume 1% of reservations get cancelled
reservation_data.loc[reservation_data.index % 100 == 0, 'reservation_status'] = [
    'cancelled']

# Assign a random flag for repeat customer Y/N
repeat_flags = ['Y', 'N']
reservation_data.loc[:, 'repeat_customer_flag'] = [
    np.random.choice(repeat_flags) for i in range(reservation_data.shape[0])
    ]

# Assign a random number of adults between 1 & 4
num_adults = [1, 2, 3, 4]
reservation_data.loc[:, 'num_adults'] = [
    np.random.choice(num_adults) for i in range(reservation_data.shape[0])
    ]

# Assign a random number of children between 0 & 2
num_children = [0, 1, 2]
reservation_data.loc[:, 'num_children'] = [
    np.random.choice(num_children) for i in range(reservation_data.shape[0])
    ]

# Assign a random number of infants between 0 & 2
num_infants = [0, 1, 2]
reservation_data.loc[:, 'num_infants'] = [
    np.random.choice(num_infants) for i in range(reservation_data.shape[0])
    ]

# Calculate the number of rooms booked based on reservation size
reservation_data.loc[:, 'num_rooms_booked'] = 1
reservation_data.loc[reservation_data['num_adults'] > 2, 'num_rooms_booked'] = 2

# Assign specific rooms randomly based on number of rooms booked
num_single_books = sum(reservation_data['num_rooms_booked'] == 1)
num_double_books = sum(reservation_data['num_rooms_booked'] == 2)
reservation_data.loc[reservation_data['num_rooms_booked'] == 1, 'rooms_booked'] = [
    [np.random.choice(room_names)] for i in range(num_single_books)
    ]
reservation_data.loc[reservation_data['num_rooms_booked'] == 2, 'rooms_booked'] = [
    np.random.choice(
        room_names, 
        size = 2, 
        replace = False
        ) 
        for i in range(num_double_books)
    ]

# Assign promo code flag randomly
# Assume 10% of reservations have a code
reservation_data = reservation_data.sample(frac = 1, ignore_index = True)
reservation_data.loc[:, 'promo_code_flag'] = 'N'
reservation_data.loc[reservation_data.index % 10 == 0, 'promo_code_flag'] = 'Y'

# Calculate total prices based on number of rooms and children
# Assume promo codes are worth a 10% discount
reservation_data.loc[:, 'total_price'] = (
    reservation_data['num_rooms_booked'] * 100).add(
    reservation_data['num_children'] * 20)
reservation_data.loc[reservation_data['promo_code_flag'] == 'Y', 'total_price'] *= 0.9

# Explode & re-cast rooms_booked so rooms can be cross-referenced to room_data
reservation_data = reservation_data.explode('rooms_booked').rename(columns = {'rooms_booked' : 'room_name'})

# Generate booking references using the following formula:
# Reference = agent_initials-date_of_arrival-date_of_departure-room_names-cust_initials-sequential_no
reservation_data.sort_values(by=['arrival_date'], inplace=True, ignore_index=True)
booking_ref_nos = [reservation_data['staff_member_initials'] + '-' 
                   + reservation_data['arrival_date'].apply(lambda x: x.strftime("%d-%m-%y")) + '-'
                   + reservation_data['departure_date'].apply(lambda x: x.strftime("%d-%m-%y")) + '-'
                   + reservation_data['room_name'] + '-'
                   + reservation_data['customer_name'].apply(lambda x: ''.join(
                       [x.split()[0][0], 
                        x.split()[1][0]]
                       )) + '-'
                   + reservation_data.index.astype(str)
                  ]
reservation_data.loc[:, 'booking_reference'] = booking_ref_nos[0]

# Set data index as booking references
reservation_data.set_index('booking_reference', inplace = True)

# Remove double-bookings in sample data
availability_info = reservation_data.loc[:, ['room_name', 'arrival_date', 'departure_date']]
availability_info = availability_info.reset_index().set_index('room_name')
availability_info['dates'] = [
    pd.date_range(x, y) 
    for x , y in 
    zip(availability_info['arrival_date'], availability_info['departure_date'])
    ]
availability_info = availability_info.explode('dates').drop(columns = ['arrival_date', 'departure_date'])
availability_info.reset_index(inplace = True)
availability_info.drop_duplicates(subset = ['room_name', 'dates'], keep = False, inplace = True)
good_references = list(set(availability_info['booking_reference']))
reservation_data = reservation_data.loc[good_references, :]

# Re-format dates as Australian standard
arrive_dates = reservation_data.loc[:, 'arrival_date'].apply(lambda x: x.strftime("%d-%m-%y"))
depart_dates = reservation_data.loc[:, 'departure_date'].apply(lambda x: x.strftime("%d-%m-%y"))
reservation_data['arrival_date'] = arrive_dates
reservation_data['departure_date'] = depart_dates

# Sort by customer name
reservation_data.sort_values(by = 'customer_name', inplace=True)


# Tests/validations?
# Check final prices are in the 50-200 range
# Check total capacities are <6


### Generate table with room availability data
# (populated with reservation code or available)

# Set up and fill a DataFrame 'availability_data' to hold room availability info.

# Use availability_info to fill booked days with booking refs., and un-booked as 'empty'
availability_data = availability_info.pivot(index = 'room_name', columns = 'dates', values = 'booking_reference')
availability_data.fillna(value = 'empty', inplace=True)
availabile_dates = [x.strftime("%d-%m-%y") for x in availability_data.columns]
availability_data.columns = availabile_dates


# Tests/validations?
# Check columns are valid dates?


# Export reservation DataFrames into a database as tables

# Create a database location & connection
DATABASE_URI = 'ahs_reservations.db'
conn = sqlite3.connect(DATABASE_URI)
conn.execute('PRAGMA foreign_keys = 1')
cur = conn.cursor()
cur.execute('PRAGMA foreign_keys = ON')


### Export room_data

# Define room_data table schema
room_data_schema = {
    'room_name' : 'CHAR(7) PRIMARY KEY',    
    'adult_capacity' : 'INTEGER',
    'child_capacity' : 'INTEGER',
    'base_cost' : 'INTEGER',
    'child_cot_cost' : 'INTEGER',
    'view_type' : 'VARCHAR(6)'
    }


# Export room_data DataFrame as table
room_data.to_sql(
    name = 'room_data', 
    con = conn, 
    if_exists = 'replace',
    dtype = room_data_schema
    )


### Export cust_data

# Define room_data table schema
cust_data_schema = {
    'customer_name' : 'VARCHAR(50) PRIMARY KEY',    
    'customer_initials' : 'CHAR(2)',
    'total_visits' : 'INTEGER',
    'credit_card_type' : 'VARCHAR(10)',
    'credit_card_number' : 'CHAR(16)',
    'email' : 'VARCHAR(70)',
    'phone_number' : 'CHAR(12)'
    }


# Export room_data DataFrame as table
cust_data.to_sql(
    name = 'cust_data', 
    con = conn, 
    if_exists = 'replace',
    dtype = cust_data_schema
    )


### Export availability_data

# Define availability_data table schema
availability_data_schema = {'room_name' : 'CHAR(7) PRIMARY KEY'}
availability_data_schema.update({i: 'CHAR(8)' for i in availability_data.columns})


# Export availability_data DataFrame as table
availability_data.to_sql(
    name = 'availability_data', 
    con = conn, 
    if_exists = 'replace',
    dtype = availability_data_schema
    )


### Export reservation_data

# Convert integer columns to integers (fix export bug)
int_columns = [
    'booking_length', 
    'num_adults', 
    'num_children', 
    'num_infants', 
    'num_rooms_booked', 
    'total_price'
    ]
for col in int_columns:
    reservation_data[col] = reservation_data[col].astype(int)

# Define reservation_data table schema
reservation_data_schema = {
    'booking_reference' : 'VARCHAR(40) PRIMARY KEY',
    'staff_member_initials' : 'CHAR(2)',
    'customer_name' : 'VARCHAR(50) REFERENCES cust_data(customer_name)', # Foreign Key
    'arrival_date' : 'CHAR(8)',
    'departure_date' : 'CHAR(8)',
    'booking_length' : 'INTEGER',
    'reservation_status' : 'VARCHAR(9)',
    'repeat_customer_flag': 'VARCHAR(1)',
    'num_adults' : 'INTEGER',
    'num_children' : 'INTEGER',
    'num_infants' : 'INTEGER',
    'num_rooms_booked' : 'INTEGER',
    'room_name' : 'CHAR(7) REFERENCES room_data(room_name)',
    'promo_code_flag' : 'CHAR(1)',
    'total_price' : 'INTEGER'
    }


# Export reservation_data DataFrame as table
reservation_data.to_sql(
    name = 'reservation_data', 
    con = conn, 
    if_exists = 'replace',
    dtype = reservation_data_schema
    )

# Connect room_name as a FOREIGN KEY to availability_data as well
# Can't make this work :( 
# Multiple foreign keys seems not to be supported

#conn.execute('''
#    ALTER TABLE reservation_data
#    ADD FOREIGN KEY (room_name) REFERENCES availability_data(room_name);
#''')




