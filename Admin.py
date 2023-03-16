import mysql.connector as db
from prettytable import from_db_cursor
import maskpass
# import Main
# import tables


class Adminn:
       
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

        #         query='''Create table if not exists TPlaces(Srno int(10) primary key auto_increment,
        #                                                         Places varchar(30),
        #                                                         Travel_places text not null,
        #                                                         Package varchar (50),
        #                                                         Amount bigint)'''

        #         self.cursor.execute(query)
                
        
        #         query='''Insert into TPlaces(Places,Travel_places,Package,Amount) values('Ladakh','i) SHANTI STUPA. ii) THIKSEY MONASTERY. iii) MAGNETIC HILLS. iv) KARGIL.','4D-3N',30000),

        # ('Manali','i) MANIKARAN SAHIB. ii) HIDIMBA DEVI TEMPLE. iii) ROHTANG PASS. iv) SOLANG VALLEY.','5D-4N',40000),

        # ('Shimla','i) KUFRI. ii) KASAULI. iii) MALL ROAD. iv) CHRIST CHURCH.','3D-2N',35000),

        # ('Mussoorie','i) KEMPTY FALLS. ii) DHANAULTI. iii) GUN HILLS. iv) THE CLOUDs END.','2D-1N',15000),

        # ('Gujarat','i)  DWARKA. ii) RANN OF KUTCH. iii) GIR NATIONAL PARK. iv) SOMNATH TEMPLE.','4D-3N',35000),

        # ('Rajasthan','i) JAIPUR. ii) CHITTORGARH. iii) MOUNT ABU. iv) UDAIPUR.','4D-3N',30000),
        
        # ('Mumbai','i) CHURCHGATE. ii) CSMT. ii) SIDDHIVINAYAK TEMPLE. iv) JUHU CHAUPATI.','5D-4N',40000)
        
        
        # '''
                
                # self.cursor.execute(query)
                # self.mydb.commit()
                # mytable=from_db_cursor(self.cursor)
                # print(mytable)

        def dispPass(self):
                try:
                        query='''Select * from tickets '''
                        self.cursor.execute(query)
                        self.mytable=from_db_cursor(self.cursor)
                        print(self.mytable)
                except:
                        print("Table cannot be displayed.")


        def addPlace(self):
                try: 
                        # self.Srno=int(input("\n\n Enter the serial number : \t "))
                        self.Places=input("\n\n Enter City :\t ")
                        self.Travel_places=input("\n\n Enter Travel Places as i)_______ . :\t ")
                        self.Package=input("\n\n Enter Package : \t ")
                        self.Amount=input("\n\n Enter the Amount : \t ")
                        self.data1=[(self.Places,self.Travel_places,self.Package,self.Amount),]

                        query='''Insert into TPlaces (Places,Travel_places,Package,Amount) values (%s,%s,%s,%s)'''
                        # query='''Insert into TPlaces values ("%s,%s,%s,%s")'''
                        self.cursor.executemany(query,self.data1)
                        self.mydb.commit()

                        query='''Select * from tplaces'''
                        self.cursor.execute(query)
                        self.mytab=from_db_cursor(self.cursor)
                        print(self.mytab)

                except :
                        print("Please try after sometime, Insertion unsuccessful. ")

        def delPlace(self):
                try:
                        query='''Select * from tplaces'''
                        self.cursor.execute(query)
                        self.mytable1=from_db_cursor(self.cursor)
                        print(self.mytable1)

                        self.inpdel=input("\n\n From the above Table select the serial number to be deleted: \t")
                        query='''Delete from tplaces where Srno=%s'''
                        data=(self.inpdel,)
                        self.cursor.execute(query,data)
                        self.mydb.commit()
                        print("Deleted Successfully ")

                        query='''Select * from tplaces'''
                        self.cursor.execute(query)
                        self.mytable1=from_db_cursor(self.cursor)
                        print(self.mytable1)
                except:
                        print("Deletion unsuccessful ")
                
        def searchh(self):
                try:
                        self.inpsearch=input("\n\n Enter the Place :\t ")
                        self.data=(self.inpsearch,)
                        query='''Select * from tickets where places= %s'''
                        self.cursor.execute(query,self.data)
                        self.mytable1=from_db_cursor(self.cursor)
                        print(self.mytable1)
                except:
                        print("Invalid, Please try after sometime !")

        def modifyy(self):
                while True: 
                        print('''
                        Select Modifications :
                        >1. Update Place.
                        >2. Update Package.
                        >3. Update Amount.
                        >4. Update City.
                        >5. Exit. 
                        ''')
                        self.inpmodify=input("\n\n Select any one option : \t")

                        if self.inpmodify=="5":
                                exit()
                        elif self.inpmodify=="1":
                                try:
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable1=from_db_cursor(self.cursor)
                                        print(self.mytable1)
                                        self.inpp=input("\n\n Enter the Serial Number of place to be modified : \t")
                                        self.updplace=input("\n\n Enter the Places in the form : i)___ : \t ")
                                        self.data=[(self.updplace,self.inpp),]
                                        # query1='''Select * from tplaces where srno= %s'''
                                        query1='''Update tplaces set travel_places= %s where srno=%s '''
                                        self.cursor.executemany(query1,self.data)
                                        self.mydb.commit()
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable2=from_db_cursor(self.cursor)
                                        print(self.mytable2)
                                        break
                                except :
                                        print("\n\n Data not Updated. ")
                                        break
                        
                        elif self.inpmodify=="2":
                                try:
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable1=from_db_cursor(self.cursor)
                                        print(self.mytable1)
                                        self.inpp=input("\n\n Enter the Serial Number of place to be modified : \t")
                                        self.updpack=input("\n\n Enter the Package : \t ")
                                        self.data=[(self.updpack,self.inpp),]
                                        # query1='''Select * from tplaces where srno= %s'''
                                        query1='''Update tplaces set package= %s where srno=%s '''
                                        self.cursor.executemany(query1,self.data)
                                        self.mydb.commit()
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable2=from_db_cursor(self.cursor)
                                        print(self.mytable2)
                                        break
                                except :
                                        print("\n\n Data not Updated. ")
                                        break
                        
                        elif self.inpmodify=="3":
                                try:
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable1=from_db_cursor(self.cursor)
                                        print(self.mytable1)
                                        self.inpp=input("\n\n Enter the Serial Number of place to be modified : \t")
                                        self.updamt=input("\n\n Enter the Amount : \t ")
                                        if self.updamt.isdigit():
                                                self.data=[(self.updamt,self.inpp),]
                                                # query1='''Select * from tplaces where srno= %s'''
                                                query1='''Update tplaces set Amount= %s where srno=%s '''
                                                self.cursor.executemany(query1,self.data)
                                                self.mydb.commit()
                                                query='''Select * from tplaces'''
                                                self.cursor.execute(query)
                                                self.mytable2=from_db_cursor(self.cursor)
                                                print(self.mytable2)
                                                break
                                        else:
                                                print("\n\n Enter a Valid Digit.")
                                except :
                                        print("\n\n Data not Updated. ")
                                        break

                        elif self.inpmodify=="4":
                                try:
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable1=from_db_cursor(self.cursor)
                                        print(self.mytable1)
                                        self.inpp=input("\n\n Enter the Serial Number of place to be modified : \t")
                                        self.updcity=input("\n\n Enter the City name : \t ")
                                        self.data=[(self.updcity,self.inpp),]
                                        # query1='''Select * from tplaces where srno= %s'''
                                        query1='''Update tplaces set Places= %s where srno=%s '''
                                        self.cursor.executemany(query1,self.data)
                                        self.mydb.commit()
                                        query='''Select * from tplaces'''
                                        self.cursor.execute(query)
                                        self.mytable2=from_db_cursor(self.cursor)
                                        print(self.mytable2)
                                        break
                                except :
                                        print("\n\n Data not Updated. ")
                                        break
                                        
        def opt(self):
                adminLog={"Username":"admin","Password":"1234"}
                self.adminuser=input("\n\n Enter Username: \t")
                if self.adminuser==adminLog["Username"]:
                        self.adminpass=maskpass.askpass(prompt="\n\n Enter Password : \t",mask='*')
                        n=1
                        while n<3:

                                if self.adminpass==adminLog["Password"]:
                                        print("\n\n LogIn Successful. ")
                                        # n+=1
                                        # break
                                while True:
                                        print('''
        >1. Display Passangers.
        >2. Add Places.
        >3. Delete Places.
        >4. Search Passangers for Specific Tour.
        >5. Modify Table values. 
        >6. Back.
        >7. Exit
                                        ''')
                                        self.inpopt=input("\n\n Select Any Option : \t ")
                                        if self.inpopt.isdigit():

                                                if self.inpopt=="7":
                                                        exit()
                                                elif self.inpopt=="6":
                                                        import Main
                                                        Main.Options().selection()
                                                elif self.inpopt=="1":
                                                        obb.dispPass()
                                                elif self.inpopt=="2":
                                                        obb.addPlace()
                                                elif self.inpopt=="3":
                                                        obb.delPlace()
                                                elif self.inpopt=="4":
                                                        obb.searchh()
                                                elif self.inpopt=="5":
                                                        obb.modifyy()

                                        else: 
                                                print("\n\n Enter a Valid Input ")
                        else:
                                print("\n\nIncorrect Password.")
                                n+=1
                else:
                        print("\n\n Invalid username")
obb=Adminn()
obb.opt()

