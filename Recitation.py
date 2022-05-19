import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Recitation\Database01.accdb;')
    print("Database is Connected")

    user_id=3
    FullName = 'Roy Millamis'
    Age = '21'
    Address = 'Cavite'
    Birthdate = '1/29/2001'
    SemGrade = '90'
    database = connect.cursor()
    database.execute('update Table1 set FullName=? where id=?', (FullName, user_id))
    database.execute('update Table1 set Age=? where id=?', (Age, user_id))
    database.execute('update Table1 set Address=? where id=?', (Address, user_id))
    database.execute('update Table1 set Birthdate=? where id=?', (Birthdate, user_id))
    database.execute('update Table1 set SemGrade=? where id=?', (SemGrade, user_id))
    database.commit()
    print("Data is updated")

except pyodbc.Error:
    print("Error in Connection")