import mysql.connector

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
