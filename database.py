import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Pass@123"
    # database = "pg"
)

mycursor = mydb.cursor()
mycursor.execute("create database pg;")
mycursor.execute("use pg;")
mycursor.execute("create table Tenannt(RoomId int , name varchar(15), Id varchar(10)unique, Mo_num BigInt, Age int unsigned, City varchar(16));")
mycursor.execute("create table Tennant_History(name varchar(15), Id varchar(10) unique, Mo_num int, Age int unsigned, City varchar(16), Room_No Int, Entry_Date date, Exit_Date Date) ")
mycursor.execute("create table Rooms(Room_No int primary key, Status varchar(10), Floor int);")


sql = "INSERT INTO Rooms(Room_No, Status, Floor) VALUES(%s,%s,%s);"
val = [(1, 'vacant', 1),
       (2, "vacant", 1),
       (3, "vacant", 1),
       (4, "vacant", 1),
       (5, "vacant", 1),
       (6, 'vacant', 2),
       (7, "vacant", 2),
       (8, "vacant", 2),
       (9, "vacant", 2),
       (10, "vacant", 2)]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, " records inserted successfully")