import pymysql



id=int()
name=""
address=""
sallary=int()
empid=int()


while True:
    def addemployee():
        print("\n\nPlease choice Any one option from below:")
        print("1. Add Employee")
        print("2. View Employees list")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        return choice

    choice=addemployee()



    if choice==1:
        

        option='y'
        while option=='y':
            conn=pymysql.connect(host="localhost",user="root",password="",db="mydata")
            mycursor = conn.cursor()

            name = input("Enter Employee name: ")
            address = input("Enter Employee Address: ")
            sallary = int(input("Enter Employee Sallary: "))
            
            myquery=f"insert into employees values('','{name}','{address}','{sallary}')"

            mycursor.execute(myquery)
            print("Data Inserted !")

            conn.commit()
            conn.close()
            sure=input("\nDo you want add more employees? (y/n): ")
            if sure=='y':
                option='y'
            else:
                option='n'       
            
        
    elif choice==2:
        conn=pymysql.connect(host="localhost",user="root",password="",db="mydata")

        mycursor = conn.cursor()

        myquery="select * from employees"


        mycursor.execute(myquery)

        results = mycursor.fetchall()
        print("Employee List Below:",end="\n\n")
        print("__ID______________Name_________Address______________________Sallery_")
        for row in results:
            
            print("ID:",row[0],"\tName:",row[1],"\tAddress:",row[2],"\tSallery:",row[3])

        conn.commit()
        conn.close()
            

    elif choice==3:
        conn=pymysql.connect(host="localhost",user="root",password="",db="mydata")

        mycursor = conn.cursor()
        
        empid=int(input("Enter Employee ID:"))
        myquery=f"select * from employees where id={empid}"
        mycursor.execute(myquery)
        results = mycursor.fetchall()

        print("Employee List Below:",end="\n\n")
        print("__ID______________Name_________Address______________________Sallery_")
        for row in results:
            
            print("ID:",row[0],"\tName:",row[1],"\tAddress:",row[2],"\tSallery:",row[3])
        
        conn.commit()
        conn.close()

        option='y'
        while option=='y':
            conn=pymysql.connect(host="localhost",user="root",password="",db="mydata")

            mycursor = conn.cursor()
        
            name = input("Enter Employee name: ")
            address = input("Enter Employee Address: ")
            sallary = int(input("Enter Employee Sallary: "))

            myquery=f"update employees set name='{name}',address='{address}',sallary={sallary} where id={empid}"
            mycursor.execute(myquery)
            print("Employees Data Updated\n")
            
            option=input("Do you want update more Employee(y/n)")
            conn.commit()
            conn.close()
            if option=='n':
                break

    elif choice==4:
        
        option='y'
        while option=='y':
            conn=pymysql.connect(host="localhost",user="root",password="",db="mydata")

            mycursor = conn.cursor()
        
            empid=int(input("Enter Employee ID:"))
            myquery=f"select * from employees where id={empid}"
            mycursor.execute(myquery)
            results = mycursor.fetchall()

            print("Employee List Below:",end="\n\n")
            print("__ID______________Name_________Address______________________Sallery_")
            for row in results:
                print("ID:",row[0],"\tName:",row[1],"\tAddress:",row[2],"\tSallery:",row[3])
            
            conn.commit()
            conn.close()
            sure=input("Are you sure Delete this employee?(y/n)")
            if sure=='y':

                conn=pymysql.connect(host="localhost",user="root",password="",db="mydata")
                mycursor = conn.cursor()
                
                myquery=f"delete from employees where id={empid}"
                mycursor.execute(myquery)
                print("Employees Data Deleted")
                conn.commit()
                conn.close()

                option=input("Do you want to delete more employee?(y/n):")
                if option=='n':
                    break
            else:
                break
                
            
    else:
        sure=input("Make Sure you want to exit?(y/n):")
        
        if sure=='y':
            option='n'
            exit()
        else:
            option='y'