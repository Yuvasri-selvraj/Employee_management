from tabulate import tabulate
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    password="uvashrii",
    database="employee_datas"
)


def add_data(Emp_name, Emp_role):
    cursor = mydb.cursor()
    sql = "INSERT INTO DATAS(EMP_NAME,EMP_ROLE) VALUES (%s,%s)"
    user = (Emp_name, Emp_role)
    cursor.execute(sql, user)
    mydb.commit()
    print("DATA ADDED SUCCESSFULLY")


def update_data(Emp_name, Emp_role, Emp_id):
    cursor = mydb.cursor()
    sql = "update datas set Emp_name=%s,Emp_role=%s where Emp_id=%s"
    user = (Emp_name, Emp_role, Emp_id)
    cursor.execute(sql, user)
    mydb.commit()
    print("DATA UPDATED SUCCESSFULLY")


def delete_data(Emp_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM DATAS WHERE EMP_ID = %s"
    user = [Emp_id]
    cursor.execute(sql, user)
    mydb.commit()
    print("DATA DELETED SUCCESSFULLY")


def select_data():
    cursor = mydb.cursor()
    sql = "SELECT EMP_ID,EMP_NAME,EMP_ROLE FROM DATAS"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result, headers=["EMP_ID", "EMP_NAME", "EMP_ROLE"]))


while True:
    print("1.ADD DATA")
    print("2.UPDATE DATA")
    print("3.DELETE DATA")
    print("4.SELECT DATA")
    print("5.EXIT")

    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        Emp_name = input("ENTER NAME:")
        Emp_role = input("ENTER ROLE:")
        add_data(Emp_name, Emp_role)

    elif choice == 2:
        Emp_id = int(input("ENTER THE ID:"))
        Emp_name = input("ENTER NAME:")
        Emp_role = input("ENTER ROLE:")
        update_data(Emp_name, Emp_role, Emp_id)

    elif choice == 3:
        Emp_id = int(input("ENTER ID TO  DELETE:"))
        delete_data(Emp_id)

    elif choice == 4:
        select_data()
    elif choice == 5:
        quit()
    else:
        print("INVALID SELECTION , PLEASE TRY AGAIN")

