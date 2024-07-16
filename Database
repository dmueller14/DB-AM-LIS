import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="",
  password="",
  database="accountantdb",
  port=3306
)


# Creating a cursor
cursor = conn.cursor()

# Creating the Database
cursor.execute("CREATE DATABASE IF NOT EXISTS accountantdb")

# Creating the Tables
# Table: Patients
cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
    patient_id INT PRIMARY KEY, 
    name VARCHAR(255), 
    prename VARCHAR(255), 
    birthdate DATE,
    address VARCHAR(255),
    city VARCHAR(255),
    zip_code VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    mobile VARCHAR(255),""")

# Table: Receipts
cursor.execute("""CREATE TABLE IF NOT EXISTS receipts ( 
    receipt_number VARCHAR(255) PRIMARY KEY, 
    order_number VARCHAR(255), 
    receipt_date DATE,
    canceled BOOLEAN,
    canceld_date DATE,
    warned_date DATE,
    extended BOOLEAN,
    extended_date DATE,
    payed BOOLEAN,
    payed_date DATE,
    warned BOOLEAN,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id))""")

# Table: Receiver
cursor.execute("""CREATE TABLE IF NOT EXISTS receiver(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    prename VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    zip_code VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    mobile VARCHAR(255),
    patient_connection VARCHAR(255),
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id))""")

# Table: Submitter
cursor.execute("""Create TABLE IF NOT EXISTS submitter(
    submitter_id INT PRIMARY KEY,
    name VARCHAR(255),
    prename VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    zip_code VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    mobile VARCHAR(255),
    title VARCHAR(255),
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id))""")

# Table: Orders
cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
    order_number VARCHAR(255) PRIMARY KEY,
    order_date DATE,
    patient_id INT,
    submitter_id INT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (submitter_id) REFERENCES submitter(submitter_id))""")

# Table: Comments
cursor.execute("""CREATE TABLE IF NOT EXISTS comments(
    comment_id INT PRIMARY KEY,
    comment VARCHAR(1000),
    comment_date DATE,
    patient_contact Date,
    receiver_contact Date,
    submitter_contact Date,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id))""")

conn.commit()

conn.close()
