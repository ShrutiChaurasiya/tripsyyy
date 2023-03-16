import mysql.connector as db
from prettytable import from_db_cursor
# from . Py_pro1 import Main

class Tab:
    def __init__(self):
        # connect server
        # mydb=db.connect(host="localhost",user="root",password="1234")
        # mycursor=mydb.cursor()

        # create database 
        # query='''Create database if not exists BasicDB'''
        # mycursor=mycursor.execute(query)

        # connect to database
        self.mydb=db.connect(host="localhost",user="root",password="1234",database="data")
        self.cursor=self.mydb.cursor()
        # print("connected")

        query='''Create table if not exists Tickets(tid int primary key,
                                                        name varchar(30) not null, 
                                                        surname varchar(35), 
                                                        mobile bigInt not null,  
                                                        Journey_date date,
                                                        booking_time datetime,
                                                        places varchar(20)  
                                                        )'''
        self.cursor.execute(query)

        query='''Create table if not exists Signup(name varchar(30) not null, 
                                                    surname varchar(20),
                                                    mobile varchar(255) primary key,
                                                    email varchar(50) not null,
                                                    passwd varchar(20))
                                                     '''
        self.cursor.execute(query)

        query='''Create table if not exists TPlaces(Srno int primary key auto_increment,
                                                                Places varchar(30) unique,
                                                                Travel_places text not null,
                                                                Package varchar (50),
                                                                Amount bigint)'''

        self.cursor.execute(query)

        query='''Create table Payment(tid int primary key,
                                        status varchar(10))'''
        self.cursor.execute(query)
        
        try: 
                query='''Insert into TPlaces(Places,Travel_places,Package,Amount) values('Ladakh','i) SHANTI STUPA. ii) THIKSEY MONASTERY. iii) MAGNETIC HILLS. iv) KARGIL.','4D-3N',30000),

        ('Manali','i) MANIKARAN SAHIB. ii) HIDIMBA DEVI TEMPLE. iii) ROHTANG PASS. iv) SOLANG VALLEY.','5D-4N',40000),

        ('Shimla','i) KUFRI. ii) KASAULI. iii) MALL ROAD. iv) CHRIST CHURCH.','3D-2N',35000),

        ('Mussoorie','i) KEMPTY FALLS. ii) DHANAULTI. iii) GUN HILLS. iv) THE CLOUDs END.','2D-1N',15000),

        ('Gujarat','i)  DWARKA. ii) RANN OF KUTCH. iii) GIR NATIONAL PARK. iv) SOMNATH TEMPLE.','4D-3N',35000),

        ('Rajasthan','i) JAIPUR. ii) CHITTORGARH. iii) MOUNT ABU. iv) UDAIPUR.','4D-3N',30000),

        ('Mumbai','i) CHURCHGATE. ii) CSMT. ii) SIDDHIVINAYAK TEMPLE. iv) JUHU CHAUPATI.','5D-4N',40000)


        '''
                self.cursor.execute(query)
                self.mydb.commit()

        except :
             print("\n\n Duplicate Entry ")
             import Main
             Main.obj.home()
        # query='''Desc Tickets'''
        # query='''Desc Signup'''
        # self.cursor.execute(query)
        # self.mytable=from_db_cursor(self.cursor)  
        # print(self.mytable)    

obj1=Tab()
