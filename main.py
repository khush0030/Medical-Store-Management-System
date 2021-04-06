import mysql.connector
from datetime import datetime


con= mysql.connector.connect(
    host="localhost",
    user="root",
    
    database="project"
)
if con.is_connected():
    print('Successfully Connected to MySQL database')
cur=con.cursor()


def vinsertion():
    x = 1
    while x>=0:
        vSno = int(input("Enter SNo: "))
        vMedicine = input("Enter name of Medicine: ")
        vComp = input("Enter name of Company: ")
        vQty = int(input("Enter Quantity: "))
        vPrice = float(input("Enter price: "))
        i=input("Do you want to enter more data:")
        if i=='yes':
            x=1
        if i=="no":
            x=-1
        sql = "insert into stock values (%s, %s, %s, %s, %s)"
        valus = (vSno,vMedicine, vComp, vQty, vPrice)
        cur.execute(sql, valus)
        con.commit()
    con.close()


def vupdate():
    y = 1
    while y >= 0:
        vSno_ = (input("Enter the Name of medicine you want to update: "))
        vques= input('What do you want to update:(price,quantity or both)')
        if vques == "price":
            i = input("Enter new price:")
            sql_update_query = "Update stock SET price = %s where medicine = %s"
            values = (i, vSno_)
        elif vques == "quantity":
            i = input("Enter new quantity:")
            sql_update_query = "Update stock SET quantity = %s where medicine = %s"
            values = (i, vSno_)
        elif vques == "both":
            i = input("Enter new quantity:")
            vprice = input("Enter the new price:")
            sql_update_query = "Update stock SET quantity = %s, price = %s where medicine = %s"
            values = (i,vprice,vSno_)
        ap = input('Do you want to enter more data:')
        if ap == 'yes':
            y = 1
        if ap == "no":
            y = -1
        cur.execute(sql_update_query,values)
        con.commit()
        print("Record Updated successfully ")
    con.close()


def vdelete():
    z = 1
    while z >= 0:
        vvno = (input("Enter the S.No of the medicine you want to remove : "))
        vvname = (input("Enter the name of the medicine you want to remove :"))
        i = input("Do you want to delete more data:")
        if i == 'yes':
            z = 1
        if i == "no":
            z = -1
        sql_update_query = "delete from stock where sno = %s and Medicine = %s;"
        values = (vvno, vvname)
        cur.execute(sql_update_query, values)
        con.commit()
        print("Record deleted successfully ")


def availaibility():
    cur = con.cursor()
    sql = 'select * from stock'
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        print(row)
    con.close()


def find():
    ap = input("Enter the name you want to search:")
    cur = con.cursor()
    sql = 'select * from stock'
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        ao = row[1]
        if ao.upper()==ap.upper():
            print(row)
    con.close


def entry():
    m = 0
    vSno = int(input('Enter the serial number:'))
    vPN = input("Enter the patient's name:")
    vDN = input("Enter the doctor's name:")
    date = datetime.now()

    p = 1
    while p>=0:
        vMN = input("Enter the name of medicine:")
        vQN = int(input("Enter the quantity:"))
        vP = int(input("Enter the price:"))
        m = m + vP
        sql1 = "insert into Bill_items values(%s,%s,%s,%s)"
        val1 = (vSno,vMN,vQN,vP)
        cur.execute(sql1,val1)
        c = input("Do you want to enter medicine:")
        if c=='yes':
            p = 1
        if c=='no':
            p = -1
            sql = "insert into sell values(%s,%s,%s,%s,%s)"
            val = (vSno, vPN, vDN, date, m)
            cur.execute(sql, val)
        con.commit()
    con.close()


def read():
    cur = con.cursor()
    sql = 'select * from sell'
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        print(row)
    con.close()


def findcustomers():
    p = input("Enter name you want information for:")
    cur = con.cursor()
    sql = 'select * from sell'
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        ao = row[1]
        if ao.lower()==p.lower():
            l = row[0]
            sql1 = 'select * from bill_items'
            cur.execute(sql1)
            data1 = cur.fetchall()
            for g in data1:
                m = g[0]
                if l==m:
                    print(g)
    con.close()

def total():
    x = ''
    c = 0
    ap = input("Enter date:")
    cur = con.cursor()
    sql = 'select * from sell'
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        ao = row[3]
        x = str(ao)
        if x== ap:
            v = row[4]
            c = v + c
    print("The total amount for",ap,'is',c)
    con.close

def date():
    x = ''
    c = 0
    ap = input("Enter date:")
    cur = con.cursor()
    sql = 'select * from sell'
    cur.execute(sql)
    data = cur.fetchall()
    for row in data:
        ao = row[3]
        x = str(ao)
        if x == ap:
            v = row[1]
            print("The customer who bought medicine on",ao,"is",v)
    con.close



print("What do you want to do:")
print("Insert Stock(Press 1)")
print("Update existing stock (Press 2)")
print("Delete record(Press 3)")
print("Show record of stock(press 4)")
print("Search data(Press 5)")
print("Enter data for bill(press 6)")
print("Shows record of customer purchase(press 7)")
print("Shows record of medicine that customer bought(press 8)")
print("Shows total amount of money earned on a particular date(press 9)")
print("Shows all customers who bought medicine on a particular date(press 10)")


vque=input('Enter what you want to do:')


if vque=="1":
    vinsertion()
if vque=="2":
    vupdate()
if vque=="3":
    vdelete()
if vque=="4":
    availaibility()
if vque=='5':
    find()
if vque=='6':
    entry()
if vque=='7':
    read()
if vque=='8':
    findcustomers()
if vque=='9':
    total()
if vque=='10':
    date()

