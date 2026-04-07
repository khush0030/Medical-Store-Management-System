# Medical Store Management System

## About
A school project built using **Python** and **MySQL** for managing a medical store. It provides a simple, menu-driven interface for handling medicine inventory, billing, and sales records.

## Features
- Add, update, and delete medicines from stock
- View all available medicines in inventory
- Search for a specific medicine by name
- Generate bills for customers with doctor and patient details
- View customer purchase history and itemized bills
- Calculate total revenue for a specific date
- Look up customers who purchased on a given date

## Tech Stack
- **Language:** Python
- **Database:** MySQL
- **Connector:** mysql-connector-python

## Database Structure

| Table | Description |
|-------|-------------|
| `stock` | Medicine inventory (SNo, Medicine, Company, Quantity, Price) |
| `sell` | Sales records (SNo, Patient Name, Doctor Name, Date, Total) |
| `bill_items` | Itemized bill entries (SNo, Medicine, Quantity, Price) |

## How to Run

1. Install MySQL and start the server
2. Create a database called `project`
3. Install the Python dependency:
   ```
   pip install mysql-connector-python
   ```
4. Create the required tables:
   ```sql
   CREATE TABLE stock (sno INT, medicine VARCHAR(100), company VARCHAR(100), quantity INT, price FLOAT);
   CREATE TABLE sell (sno INT, patient_name VARCHAR(100), doctor_name VARCHAR(100), date DATETIME, total FLOAT);
   CREATE TABLE bill_items (sno INT, medicine VARCHAR(100), quantity INT, price FLOAT);
   ```
5. Run the program:
   ```
   python main.py
   ```

## Menu Options
```
1  - Insert Stock
2  - Update existing stock
3  - Delete record
4  - Show record of stock
5  - Search data
6  - Enter data for bill
7  - Shows record of customer purchase
8  - Shows record of medicine that customer bought
9  - Shows total amount earned on a particular date
10 - Shows all customers who bought medicine on a particular date
```
