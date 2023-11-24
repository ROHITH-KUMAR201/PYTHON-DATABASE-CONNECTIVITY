from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root",password="", database="library")
def insert(id,name,author,amount,quantity):
    res = con.cursor()
    sql = "insert into bookinfo (id,name,author,amount,quantity) values (%s,%s,%s,%s,%s)"
    user = (id,name,author,amount,quantity)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")
def update(id,name,author,amount,quantity):
    res = con.cursor()
    sql = "update bookinfo set name=%s, author=%s, amount=%s,quantity=%s where id=%s"
    user = (id,name,author,amount,quantity)
    res.execute(sql, user)
    con.commit()
    print("Data Update Successfully")
def select():
    res = con.cursor()
    sql = "select * from bookinfo"
    res.execute(sql)
    #result=res.fetchone()
    #result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=[id,name,author,amount,quantity]))
def delete(id):
    res = con.cursor()
    sql = "delete from bookinfo where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")


while True:
    print("1.Insert Data")
    print("2.Update data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if (choice == 1):
        id = int(input("Enter the customer id:"))
        name = input("Enter the name of the book:")
        author = input("Enter the author name:")
        amount = int(input("amount:"))
        quantity = input("quantity:")
        total=quantity*amount
        print(("Your data saved successfullt"))
        insert(id,name,author,amount,quantity)
    elif choice == 2:
        id = int(input("enter the customer id:"))
        name = input("enter the name:")
        author = input("Enter the author name:")
        amount = int(input("amount:"))
        quantity =int(input("quantity:"))
        print(("Your data saved successfullt"))
        update(id,name,author,amount,quantity)
    elif choice == 3:
        select()
    elif choice == 4:
        id = int(input("Enter The id to Delete : "))
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try")