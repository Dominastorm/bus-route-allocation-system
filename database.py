import mysql.connector
from mysql.connector import IntegrityError
import streamlit as st

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bus_route_allocation_system"
)

cursor = db.cursor()

'''
Functions to create the tables in the database
'''
def create_tables() -> None:
    cursor.execute('''CREATE TABLE IF NOT EXISTS Student (
    StudentID VARCHAR(255) PRIMARY KEY,
    Password VARCHAR(255),
    BusCode INT,
    StopCode INT,
    StudentName VARCHAR(255),
    StudentPhone VARCHAR(255),
    StudentAddress VARCHAR(255),
    TransportFees FLOAT,
    isAdmin BOOLEAN);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bus (
    BusCode INT AUTO_INCREMENT PRIMARY KEY,
    RouteCode INT,
    BusNumber VARCHAR(255),
    DriverName VARCHAR(255),
    DriverPhone VARCHAR(255),
    Capacity INT,
    isFull BOOLEAN);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Stop (
    RouteCode INT,
    StopCode INT,
    StopName VARCHAR(255),
    StopAddress VARCHAR(255),
    PickupTime TIME,
    DropTime TIME,
    DistanceFromCollege FLOAT,
    PRIMARY KEY (RouteCode, StopCode));''')

    cursor.execute('''ALTER TABLE Student
    ADD FOREIGN KEY (Bus_Code) REFERENCES Bus(Bus_Code);

    ALTER TABLE Student
    ADD FOREIGN KEY (Stop_Code) REFERENCES Stop(Stop_Code);

    ALTER TABLE Bus
    ADD FOREIGN KEY (Route_Code) REFERENCES Stop(Route_Code);''')


'''insert values in Student table'''


def insert_student_data(student_id, password, bus_code, stop_code, student_name, student_phone, student_address,
                        transport_fees, is_admin):
    try:
        cursor.execute(
            "INSERT INTO student (student_id, password, bus_code, stop_code, student_name, student_phone, student_address, transport_fees, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (student_id, password, bus_code, stop_code, student_name, student_phone, student_address, transport_fees, is_admin))
        db.commit()
        st.success("Student Data Inserted Successfully")
    except IntegrityError:
        st.error("Student ID already exists")
    except ValueError:
        st.error("Invalid data type")


def insert_student_data_st() -> None:
    st.write("Insert Student Data")
    student_id = st.text_input("Student ID")
    password = st.text_input("Password")
    bus_code = st.text_input("Bus Code")
    stop_code = st.text_input("Stop Code")
    student_name = st.text_input("Student Name")
    student_phone = st.text_input("Student Phone")
    student_address = st.text_input("Student Address")
    transport_fees = st.text_input("Transport Fees")
    is_admin = st.text_input("Is Admin")
    if st.button("Insert"):
        insert_student_data(student_id, password, bus_code, stop_code, student_name, student_phone, student_address,
                            transport_fees, is_admin)


'''insert values in Bus table'''


def insert_bus_data(bus_code, route_code, bus_number, driver_name, driver_phone, capacity, is_full):
    try:
        cursor.execute("INSERT INTO Bus (BusCode, RouteCode, BusNumber, DriverName, DriverPhone, Capacity, isFull) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (bus_code, route_code, bus_number, driver_name, driver_phone, capacity, is_full))
        db.commit()
        st.write("Inserted successfully")
    except IntegrityError:
        st.write("Code already exists")
    except ValueError:
        st.write("Invalid data type")


def insert_bus_data_st() -> None:
    st.write("Insert Bus Data")
    bus_code = st.text_input("Bus Code")
    route_code = st.text_input("Route Code")
    bus_number = st.text_input("Bus Number")
    driver_name = st.text_input("Driver Name")
    driver_phone = st.text_input("Driver Phone")
    capacity = st.text_input("Capacity")
    is_full = st.text_input("Is Full")
    if st.button("Insert"):
        insert_bus_data(bus_code, route_code, bus_number,
                        driver_name, driver_phone, capacity, is_full)


'''insert values in Stop table'''


def insert_stop_data(route_code, stop_code, stop_name, stop_address, pickup_time, drop_time, distance_from_college):
    try:
        cursor.execute("INSERT INTO Stop (RouteCode, StopCode, StopName, StopAddress, PickupTime, DropTime, "
                       "DistanceFromCollege) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (route_code, stop_code, stop_name, stop_address, pickup_time, drop_time, distance_from_college))
        db.commit()
        st.write("Inserted successfully")
    except IntegrityError:
        st.write("Code already exists")
    except ValueError:
        st.write("Invalid data type")


def insert_stop_data_st() -> None:
    st.write("Insert Stop Data")
    route_code = st.text_input("Route Code")
    stop_code = st.text_input("Stop Code")
    stop_name = st.text_input("Stop Name")
    stop_address = st.text_input("Stop Address")
    pickup_time = st.text_input("Pickup Time")
    drop_time = st.text_input("Drop Time")
    distance_from_college = st.text_input("Distance From College")
    if st.button("Insert"):
        insert_stop_data(route_code, stop_code, stop_name, stop_address,
                         pickup_time, drop_time, distance_from_college)


'''delete record from Student table'''


def delete_student_data(student_id):
    try:
        cursor.execute(
            "DELETE FROM Student WHERE StudentID = %s", (student_id,))
        db.commit()
        st.write("Deleted successfully")
    except IntegrityError:
        st.write("ID doesn't exist")


def delete_student_data_st() -> None:
    st.write("Delete Student Data")
    student_id = st.text_input("Student ID")
    if st.button("Delete"):
        delete_student_data(student_id)


'''delete record from Bus table'''


def delete_bus_data(bus_code):
    try:
        cursor.execute("DELETE FROM Bus WHERE BusCode = %s", (bus_code,))
        db.commit()
        st.write("Deleted successfully")
    except IntegrityError:
        st.write("Code doesn't exist")


def delete_bus_data_st() -> None:
    st.write("Delete Bus Data")
    bus_code = st.text_input("Bus Code")
    if st.button("Delete"):
        delete_bus_data(bus_code)


'''delete record from Stop table'''


def delete_stop_data(route_code, stop_code):
    try:
        cursor.execute(
            "DELETE FROM Stop WHERE RouteCode = %s AND StopCode = %s", (route_code, stop_code))
        db.commit()
        st.write("Deleted successfully")
    except IntegrityError:
        st.write("Code doesn't exist")


def delete_stop_data_st() -> None:
    st.write("Delete Stop Data")
    route_code = st.text_input("Route Code")
    stop_code = st.text_input("Stop Code")
    if st.button("Delete"):
        delete_stop_data(route_code, stop_code)


'''update record in Student table'''


def update_student_data(student_id, password, bus_code, stop_code, student_name, student_phone, student_address,
                        transport_fees, is_admin):
    try:
        cursor.execute("UPDATE Student SET Password = %s, BusCode = %s, StopCode = %s, StudentName = %s, "
                       "StudentPhone = %s, StudentAddress = %s, TransportFees = %s, isAdmin = %s WHERE StudentID = %s",
                       (password, bus_code, stop_code, student_name, student_phone, student_address, transport_fees,
                        is_admin, student_id))
        db.commit()
        st.write("Updated successfully")
    except IntegrityError:
        st.write("ID doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def update_student_data_st() -> None:
    st.write("Update Student Data")
    student_id = st.text_input("Student ID")
    password = st.text_input("Password")
    bus_code = st.text_input("Bus Code")
    stop_code = st.text_input("Stop Code")
    student_name = st.text_input("Student Name")
    student_phone = st.text_input("Student Phone")
    student_address = st.text_input("Student Address")
    transport_fees = st.text_input("Transport Fees")
    is_admin = st.text_input("Is Admin")
    if st.button("Update"):
        update_student_data(student_id, password, bus_code, stop_code, student_name, student_phone, student_address,
                            transport_fees, is_admin)


'''update record in Bus table'''


def update_bus_data(bus_code, route_code, bus_number, driver_name, driver_phone, capacity, is_full):
    try:
        cursor.execute("UPDATE Bus SET RouteCode = %s, BusNumber = %s, DriverName = %s, DriverPhone = %s, "
                       "Capacity = %s, isFull = %s WHERE BusCode = %s",
                       (route_code, bus_number, driver_name, driver_phone, capacity, is_full, bus_code))
        db.commit()
        st.write("Updated successfully")
    except IntegrityError:
        st.write("Code doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def update_bus_data_st() -> None:
    st.write("Update Bus Data")
    bus_code = st.text_input("Bus Code")
    route_code = st.text_input("Route Code")
    bus_number = st.text_input("Bus Number")
    driver_name = st.text_input("Driver Name")
    driver_phone = st.text_input("Driver Phone")
    capacity = st.text_input("Capacity")
    is_full = st.text_input("Is Full")
    if st.button("Update"):
        update_bus_data(bus_code, route_code, bus_number,
                        driver_name, driver_phone, capacity, is_full)


'''update record in Stop table'''


def update_stop_data(route_code, stop_code, stop_name, stop_address, pickup_time, drop_time, distance_from_college):
    try:
        cursor.execute("UPDATE Stop SET StopCode = %s, StopName = %s, StopAddress = %s, PickupTime = %s, "
                       "DropTime = %s, DistanceFromCollege = %s WHERE RouteCode = %s AND StopCode = %s",
                       (stop_code, stop_name, stop_address, pickup_time, drop_time, distance_from_college, route_code,
                        stop_code))
        db.commit()
        st.write("Updated successfully")
    except IntegrityError:
        st.write("Code doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def update_stop_data_st() -> None:
    st.write("Update Stop Data")
    route_code = st.text_input("Route Code")
    stop_code = st.text_input("Stop Code")
    stop_name = st.text_input("Stop Name")
    stop_address = st.text_input("Stop Address")
    pickup_time = st.text_input("Pickup Time")
    drop_time = st.text_input("Drop Time")
    distance_from_college = st.text_input("Distance From College")
    if st.button("Update"):
        update_stop_data(route_code, stop_code, stop_name, stop_address,
                         pickup_time, drop_time, distance_from_college)


'''search record in Student table'''


def search_student_data(student_id):
    try:
        cursor.execute(
            "SELECT * FROM Student WHERE StudentID = %s", (student_id,))
        st.write(cursor.fetchall())
    except IntegrityError:
        st.write("ID doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def search_student_data_st() -> None:
    st.write("Search Student Data")
    student_id = st.text_input("Student ID")
    if st.button("Search"):
        search_student_data(student_id)


'''search record in Bus table'''


def search_bus_data(bus_code):
    try:
        cursor.execute("SELECT * FROM Bus WHERE BusCode = %s", (bus_code,))
        st.write(cursor.fetchall())
    except IntegrityError:
        st.write("Code doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def search_bus_data_st() -> None:
    st.write("Search Bus Data")
    bus_code = st.text_input("Bus Code")
    if st.button("Search"):
        search_bus_data(bus_code)


'''search record in Stop table'''


def search_stop_data(route_code, stop_code):
    try:
        cursor.execute(
            "SELECT * FROM Stop WHERE RouteCode = %s AND StopCode = %s", (route_code, stop_code))
        st.write(cursor.fetchall())
    except IntegrityError:
        st.write("Code doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def search_stop_data_st() -> None:
    st.write("Search Stop Data")
    route_code = st.text_input("Route Code")
    stop_code = st.text_input("Stop Code")
    if st.button("Search"):
        search_stop_data(route_code, stop_code)


'''display record from Student table'''


def display_student_data():
    try:
        cursor.execute("SELECT * FROM Student")
        st.write(cursor.fetchall())
    except IntegrityError:
        st.write("Table doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def display_student_data_st() -> None:
    st.write("Display Student Data")
    if st.button("Display"):
        display_student_data()


'''display record from Bus table'''


def display_bus_data():
    try:
        cursor.execute("SELECT * FROM Bus")
        st.write(cursor.fetchall())
    except IntegrityError:
        st.write("Table doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def display_bus_data_st() -> None:
    st.write("Display Bus Data")
    if st.button("Display"):
        display_bus_data()


'''display record from Stop table'''


def display_stop_data():
    try:
        cursor.execute("SELECT * FROM Stop")
        st.write(cursor.fetchall())
    except IntegrityError:
        st.write("Table doesn't exist")
    except ValueError:
        st.write("Invalid data type")


def display_stop_data_st() -> None:
    st.write("Display Stop Data")
    if st.button("Display"):
        display_stop_data()
