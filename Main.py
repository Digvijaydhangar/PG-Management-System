import mysql.connector
import pandas as pd 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Pass@123",
    database = "pg"
)
mycursor = mydb.cursor()

def Details():
    ch = 1
    while (ch != 3):
        print("1: Details of Tennants in PG")
        print("2: Details of Rooms in PG")
        print("3: Details of Tennant History Table ")
        print("4: Cancelll")
        ch = int(input("Enter the choice number : "))
        
        if ch==1:
            mycursor.execute("select * from Tenannt ORDER BY RoomId ;")
            Details = mycursor
            # print("Room_no \tname\tId\tMo\tAge\tCity")
            for index, item in enumerate (Details):
                Room_no, name, Id, Mo, Age, City = item
                print(f"{Room_no} \t{name}\t{Id}\t{Mo}\t{Age}\t{City}")
            print("\n")
            break
        elif ch==2:
            mycursor.execute("select * from Rooms;")
            Details = mycursor
            print("Room_no\tStatus\t\tFloor")
            for index, item in enumerate (Details):
                Room_no, Status, Floor = item
                print(f"{Room_no} \t{Status}   \t{Floor}")
            print("\n")
            break
        elif ch==3:
            print("eufgurgfh")
            mycursor.execute("select * from Tennant_History order by Room_No;")
            Details = mycursor
            # print("name \t\t Id\t Mo\t Age\t City\t Room_no\t Entry\t Exit")
            for index, item in enumerate (Details):
                name, Id, Mo, Age, City, Room_no, Entry, Exit = item
                print(f"{name}\t {Id}\t {Mo}\t {Age}\t {City}\t {Room_no}\t {Entry}\t {Exit}")
            print("\n")
            break
        elif ch==4:
            break
        else:
            print("Enter correct choice...\n")
    
    
    
    
    
    
def DeAdmit():
    ch = 1
    while (ch != 3):
        print("1: Delete Data by Romm_no")
        print("2: Delete Data by Id Number")
        print("3: Cancelll")
        ch = int(input("Enter the choice number : "))
        
        if (ch == 1):
            room = input("Enter the Room No which Tennant is Leaving : ")
            Exit_Date = input("Enter the Exit Date of Tenannt (YYYYMMDD) Format : ")
            sql = "update Tennant_History set Exit_Date = %s where Room_No=%s AND Id IN (select Id from Tenannt where RoomId = %s);"
            val = (Exit_Date, room, room)
            mycursor.execute(sql, val)
            sql = "delete from Tenannt where RoomId = %s AND Age > %s;"
            val = (room, 0)
            mycursor.execute(sql, val)
            sql = "update Rooms set Status = %s where Room_No = %s;"
            val2 = ('vacant', room)
            mycursor.execute(sql, val2)
            mydb.commit()
            break
        elif (ch == 2):
            ID = input("Enter Id Number which Tennant is Leaving : ")
            Exit_Date = input("Enter the Exit Date of Tenannt (YYYYMMDD) Format : ")
            sql = "update Rooms set Status = %s where Room_No IN( select RoomId from Tenannt where Id = %s);"
            val2 = ('vacant', ID)
            mycursor.execute(sql, val2)
            sql = "update Tennant_History set Exit_Date = %s where Id=%s AND Room_No IN (select RoomId from Tenannt where Id = %s);"
            val = (Exit_Date, ID, ID)
            mycursor.execute(sql, val)
            sql = "delete from Tenannt where Id = %s;"
            val = []
            val.append(ID)
            mycursor.execute(sql, val)
            # sql = "select RoomId from Tenannt where Id = %s;"
            # mycursor.execute(sql,val)
            print("deleted record ....")
            mydb.commit()
            break
        elif (ch == 3):
            break
        else:
            print("Enter Correct Choice..... ")            
            
def Admit():
    print("Enter The Name of Tennant : ")
    name = input()
    print("Enter Id Number : ")
    ID = input()
    print("Enter Mobile Number : ")
    Mo_Num = int(input())
    print("Enter The Age : ")
    Age = input()
    print("Enter The Name of City : ")
    City = input()
    print("Enter the Current date of Admission: ")
    Entry_Date = input()
    mycursor.execute("select Room_No,Floor from Rooms where Status = 'vacant';")
    Vacant_Rooms = mycursor
    lis = []
    for index, item in enumerate (Vacant_Rooms):
        Room_no, floor = item
        print(f"Room No: {Room_no} \t Floor: {floor}")
        lis.append(Room_no)
            
    room = int(input("Enter the Room No in which you want to Live : "))
    # print(lis)  
    sql = "insert into tenannt(RoomId, name, Id, Mo_num,Age ,City )values (%s,%s,%s,%s,%s,%s);"
    val = (room,name, ID, Mo_Num, Age, City)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "inserted successfully")
    # sql = "insert into Rooms(Status)values ('Occupied') where Room_No =(%s); "
    sql = "update Rooms set Status =%s where Room_No =%s;"
    val =('Occupied',room)
    mycursor.execute(sql, val)
    mydb.commit()
    sql = "insert into Tennant_History(name, Id, Mo_num, Age, City, Room_No, Entry_Date) values(%s,%s,%s,%s,%s,%s,%s);"
    val = (name, ID, Mo_Num, Age, City, room, Entry_Date)
    mycursor.execute(sql, val)
    mydb.commit()    
    

             

ch = 1
while (ch != 4) :
    print("1: Admisssion of new Tennant")
    print("2: DeAdmission of Tennant")
    print("3: Details of PG")
    print("4: Exittt")
    ch = int(input("Enter the choice you want .... : "))
    
    if (ch == 1):
        Admit()
    elif (ch == 2):     
        DeAdmit()
    elif (ch == 3): 
        Details()    
    elif ch==4:
        break      
    else :
        print("Enter Correct Choice.....")
       
        
