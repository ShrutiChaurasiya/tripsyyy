import re
import maskpass
import mysql.connector as db
from prettytable import from_db_cursor
import random
import datetime
from datetime import *
import threading
# import tables


class Options:
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
    
    def login(self):
            self.username=input("\n\nEnter your registered Email id as Username : \t")
            self.password=input("\n\nEnter Your Password : \t")
            self.datalog=(self.username,self.password)
            query1='''SELECT email,passwd from signup WHERE email=%s and passwd=%s'''
            self.cursor.execute(query1,self.datalog)
            count=0
            for i in self.cursor:
                if i==self.datalog:
                    count+=1
                
            if count==1:
                print("\n\nLog In Successful.")
                while True:
                    print(''' 
>1. View Ticket.
>2. Book Ticket.
>3. Payment Page.
>4. Back. ''')      
                    inpopts=input("Enter Choice: \t")
                    if inpopts=="4":
                            obj.selection()
                    elif inpopts=="2":
                            obj.Book()
                    elif inpopts=="3":
                            obj.payment()
                    elif inpopts=="1":
                            obj.viewtickets()

            else:
                print("\n\nInvalid Credentials.")
                obj.selection()
        
            


    def viewtickets(self):
        self.uinp=input("Enter Your Tid Number :\t ")
        self.data=(self.uinp,)
        try:
            query='''Select tickets.tid,tickets.name,tickets.surname,tickets.mobile,tickets.journey_date,tickets.booking_time,tickets.places,payment.status from tickets inner join payment on tickets.tid=payment.tid where tickets.tid=%s'''
            self.cursor.execute(query,self.data)
            self.mytable=from_db_cursor(self.cursor)
            print(self.mytable)
        except :
                print("Data cannot be displayed / Enter a valid Tid")



    def signup(self):
        self.name=input("\n\nEnter Your First Name : \t")
        if self.name.isalpha():
            self.surname=input("\n\nEnter Your Surname : \t")
            if self.surname.isalpha():
                n=1
                while n<4:
                    self.mobile=input("\n\nEnter Your Mobile No. : \t")
                    if self.mobile.isdigit() and re.match('^[6-9]\d{9}$',self.mobile):
                    # if self.mobile.isdigit():
                        print("\n\nNOTE : your email id will be used for further process. ")
                        break
                    else:
                        print("\nEnter Correct Mobile Number")
                        if n==3:
                            print("Too many attempts.Incorrect Mobile number. ")
                            obj.selection()
                        n+=1  
                e=1
                while e<4:
                    self.email=input("\n\nEnter Your Email Id : \t")
                    self.email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
                    if re.search(self.email_condition,self.email):
                        print("\n\nEmail Validation successful")
                        break
                    else:
                        print("\n\nWrong Email Entered ")
                        if e==3:
                            print("Too many attempts.Invalid Email address ")
                            exit()
                        e+=1
                print('''
\n *Note : The Password should be of atleast 6 characters and combinition of 1 Capital Letter 1 Special Character and 1 Digit
                        ''')
                p=1
                while p<4:
                    self.passwd=maskpass.askpass(prompt="\n\nEnter Your Password : \t",mask='*')
                # self.passwd=input("\n \t Enter Your Password : \t"
                    self.reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
                            # compiling regex
                    self.pat = re.compile(self.reg) 
                            # searching regex				
                    self.mat = re.search(self.pat, self.passwd)
                    if self.mat:
                        print("\n\nPassword is valid.")
                        print(f"\n \nSignup is Successfull !! \nYour Username is : {self.email} and \nYour Password is {self.passwd} \n\nThankyou ")
                        
                        break
                    else:
                        print("\n\nPassword invalid !! ")
                        if p==3:
                            print("Too many attempts. Invalid Password")
                            exit()
                        p+=1
                    
                try:
                    self.l1=[(self.name,self.surname,self.mobile,self.email,self.passwd),]  
                    query='''Insert into Signup(name,surname,mobile,email,passwd) values(%s,%s,%s,%s,%s)'''
                    self.cursor.executemany(query,self.l1)
                    self.mydb.commit()
                    # self.mytab=from_db_cursor(self.cursor)
                    # print(self.mytab)
                    print(f"\n\nWelcome to the BOOKING Page of Tripsyy..... ")
                    event = threading.Event()
                    event.wait(3)
                    obj.Book()
                        
                except:
                    print("\n\nQuery Not Updated , Please Try After Sometime")
                            
            else:
                print("\n\nPlease Enter a Valid Surname.")
        else:
            print("\n\nPlease Enter a Valid Name.")        
                                 
                     
    def Main(self):
        print('''   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                WELCOME TO TRIPSYYY   
        ....................................
                #YourTravelPartner!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        while True:
            print('''
        Select from the Below Options :
        > 1. Login
        > 2. SignUp
        > 3. Exit
        
            ''')

            self.inpLogin=input("\nEnter Your Choice : \t")
            if self.inpLogin=="3":
                exit()
            elif self.inpLogin=="2":
                obj.signup()
            elif self.inpLogin=="1":
                obj.login()
                
    def Book(self):
        self.tid=random.randint(10000,100000)
        print(f"\n\nYour Unique ID is {self.tid} , Save it for further References! \n")
        self.bname=input("\nEnter Your name as to be printed on Ticket : \t")
        if self.bname.isalpha():
            self.bsurname=input("\nEnter Your Surname : \t")

            if self.bsurname.isalpha():
                n=1
                while n<4:
                    self.bmobile=input("\nEnter Your Mobile No. : \t")

                    if self.bmobile.isdigit() and re.match('^[6-9]\d{9}$',self.bmobile):
                        print("\nMobile Number Validated Successfully ")
                        break
                    else: 
                        print("\nEnter a Valid Mobile Number.")
                        if n==3:
                            print("Too many attempts. Invalid Mobile Number.")
                            exit()
                        n+=1
                self.bookdate=datetime.now()
                t=1
                while t<4:    
                    self.bdate=input("\nEnter Your Journey Date as (YYYY-MM-DD) : \t")
                    
                    if datetime.strptime(self.bdate,'%Y-%m-%d')>self.bookdate:
                        print("\nDate Validation Successfull!")
                        print(f"\n\n\t Your Booked Your Tickets on {self.bookdate}, Thankyou\n\n ")
                        break
                    else:
                        print("\nCheck Your format.")
                        if t==3:
                            print("Too many attempts. Invalid Date.")
                            exit()
                        t+=1
                    # self.bookdate=datetime.now()
                    
                try:
                    self.list1=[(self.tid,self.bname,self.bsurname,self.bmobile,self.bdate,self.bookdate,self.listop[self.index]),]  
                    query='''Insert into Tickets values(%s,%s,%s,%s,%s,%s,%s)'''
                    self.cursor.executemany(query,self.list1)
                    self.mydb.commit()
                    self.data1=(self.tid,)
                    query ='''Select * from Tickets where tid= %s'''
                    
                    self.cursor.execute(query,self.data1)
                    self.mytab=from_db_cursor(self.cursor)
                    print(self.mytab)

                    print("\n\nRedirecting to the Payment Page......")
                    event = threading.Event()
                    event.wait(3)
                    obj.payment()

                except  :
                    print("\n\nQuery Not Updated , Please Try After Sometime")

            else:
                print("\nPlease Enter a Valid Surname.")
        else:
            print("\nPlease Enter a Valid Name.") 

    def payment(self):
        n=1
        while n<4:
            self.payid=input("\n\nEnter Your tid given while booking : \t")
            print("\n\nFetching Details , Please wait..........")
            event = threading.Event()
            event.wait(4)
            
            try:
                query='''select * from tickets where tid=%s '''
                self.data=(self.payid,)
                self.cursor.execute(query,self.data)
                for i in self.cursor:
                    self.payid=i[0]
                # mytable=from_db_cursor(self.cursor)
                # print(mytable)
                if self.payid==i[0]:
                    print("\n\nYour Payable amount is as below along with your details : ")
                    break
            except:
                print("\n\nNo such Tid found.")
                n+=1
                if n==4:
                    print("Too many Attempts.")
                    exit()

        try:
            query='''select tickets.tid,tickets.name,tickets.surname,tickets.mobile,tickets.journey_date,tickets.booking_time,tickets.places,tplaces.amount from tickets inner join tplaces on tickets.places=tplaces.places  where tid=%s'''
            self.cursor.execute(query,self.data)
            mytable=from_db_cursor(self.cursor)
            print(mytable)
            

        except :
            print("\n\nNo data found. ")
            

        event = threading.Event()
        event.wait(3)
        
        self.upi=input("\n\nEnter Your UPI Id : \t ")
        self.upi_condition='[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,8}'
        
        # searching regex			
        u=0	
        if re.search(self.upi_condition, self.upi):
            n=0
            while n<4:
                print("\n\nplease Enter the otp given below : \n\n")
                self.otpgen=random.randint(1000,10000)
                print(f"\n {self.otpgen}")
                self.inpotp=input("\n\n here : \t")
                if str(self.otpgen)==self.inpotp:
                    print("Thankyou.....")
                    try:
                        status="SUCCESS"
                        paydata=(self.payid,status,)
                        query='''insert into payment(tid,status) values(%s,%s)'''
                        self.cursor.execute(query,paydata)
                        self.mydb.commit()
                        print("\n\nPayment Successful, Thankyou Enjoy your trip. ")
                        break
                    except:
                        stat1="FAIL"
                        paydata1=(self.payid,stat1,)
                        query='''insert into payment (tid,status) values(%s,%s)'''
                        self.cursor.execute(query,paydata1)
                        self.mydb.commit()
                        print("Payment Unsucessful...!")
                
                    
                else:
                    print("\n\nInvalid Otp .")
                    n+=1
        else:
            print("\n\nEnter a valid upi id .")
            u+=1
            if u==4:
                print("Wrong UPI Id entered many times")
            else:
                obj.payment()
        
    def Ladakh(self):
        
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Ladakh .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
              
        query='''select * from tplaces where places= "Ladakh"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
       
    def Manali(self):
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Manali .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        
        query='''select * from tplaces where places= "Manali"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
        
    def Shimla(self):
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Shimla .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        
        query='''select * from tplaces where places= "Shimla"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
        
    def Mussoorie(self):
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Mussoorie .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        
        query='''select * from tplaces where places= "Mussoorie"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
        
    def Gujarat(self):
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Gujarat .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        query='''select * from tplaces where places= "Gujarat"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
        
    def Rajasthan(self):
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Rajasthan .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        query='''select * from tplaces where places= "Rajasthan"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
        
    def Mumbai(self):
        print(''' 
    ..........................................................

                    Hello from Tripsyy!!

            POV: You are Viewing Places to Tour in Mumbai .
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        query='''select * from tplaces where places= "Mumbai"'''
        self.cursor.execute(query)
        mytable=from_db_cursor(self.cursor)
        print(mytable)

        obj.func()
        
    def func(self):
        print('''
        To Book your Travel with Tripsyy:- 
        >1. Book Tickets.
        >2. Home Page.
        >3. Exit.
        
    ''')

        inpLad=input("\nEnter Your Choice : ")
        if inpLad=="3":
            exit()
        elif inpLad=="1":
            obj.Main()
        elif inpLad=="2":
            obj.selection()

    def selection(self):

        print(''' 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                WELCOME TO TRIPSYYY   
        ....................................
                #YourTravelPartner!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
        
    > 1. HOME PAGE
    > 2. LOGIN PAGE
    > 3. ADMIN CONTROL
*Admin control is only for Admin and is Password Protected.*
    ''')
        n=1
        while n<5:
            self.inpp=input("\n\nEnter your choice : \t")

            if self.inpp=="1":
                obj.home()
                break
            if self.inpp=="2":
                obj.login()
                break
            elif self.inpp=="3":
                import Admin
                Admin.Adminn().opt()
                break
            else:
                print("\n\n Enter a Valid Option.")
                n+=1
                if n==4:
                    print("\n\n Last attempt....")


    def home(self):
        
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                WELCOME TO TRIPSYYY   
        ....................................
                #YourTravelPartner!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Choose your Travel Destination !!

    > 1.LADAKH
    > 2.MANALI
    > 3.SHIMLA
    > 4.MUSSOORIE
    > 5.GUJARAT
    > 6.RAJASTHAN
    > 7.MUMBAI
    > 8.PAYMENT
    > 9.Back
    > 10.EXIT

        ''')
        self.list=([])
        self.index=0
        self.listop=["Ladakh","Manali","Shimla","Mussoorie","Gujarat","Rajasthan","Mumbai"]
        while True:
            inpmain=input("\nEnter Any Single Option : \t ")
            if inpmain.isdigit():
                if inpmain=="1":
                    self.index=self.listop.index("Ladakh")
                    obj.Ladakh()
                    break
                elif inpmain=="2":
                    self.index=self.listop.index("Manali")
                    obj.Manali()
                    break
                elif inpmain=="3":
                    self.index=self.listop.index("Shimla")
                    obj.Shimla()
                    break
                elif inpmain=="4":
                    self.index=self.listop.index("Mussoorie")
                    obj.Mussoorie()
                    break
                elif inpmain=="5":
                    self.index=self.listop.index("Gujarat")
                    obj.Gujarat()
                    break
                elif inpmain=="6":
                    self.index=self.listop.index("Rajasthan")
                    obj.Rajasthan()
                    break
                elif inpmain=="7":
                    self.index=self.listop.index("Mumbai")
                    obj.Mumbai()
                    break
                elif inpmain=="10":
                    exit()
                elif inpmain=="9":
                    obj.selection()
                elif inpmain=="8":
                    obj.payment()
                    break
                
                else:
                    print("\n\nYou entered an Invalid Input \n\n")

            else:
                print("\n\nPlease Enter a Valid Option. ")
obj=Options()
obj.selection()