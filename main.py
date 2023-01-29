import mysql.connector as s

mydb = s.connect(host='127.0.0.1', user='root', passwd='Falguni@1', database='falguni')
if mydb.is_connected():
    print('successfully connected')
mycursor = mydb.cursor()
g = 0
h = 0
m = 0

# TABLE CREATION
# mycursor.execute("create table ward(ward varchar(20), ward_stat varchar(20),beds varchar(20));")
# mycursor.execute("create table bill (b_name varchar(20), b_day int, b_room int, b_pd int, b_pl int, b_mtd varchar(3));")
# mycursor.execute("create table transport (t_ambno int, t_drv varchar(20), t_mob bigint);")
# mycursor.execute("create table patient(p_name varchar(20),p_admt varchar(20) ,p_age int,p_mob bigint,p_add varchar(30),p_stat varchar(1));")
# mycursor.execute("create table family (k varchar(20), n varchar(20), d varchar(20));")
# mycursor.execute("create table doctor (d_name varchar(20), d_dept int, d_mob bigint);")
# mycursor.execute("create table vaccine_detail (v_date varchar(20), v_no float, v_pat float, v_left float);")

users = ["devvrat", "falguni"]

print('*********************************************')
print(":	:")
print(":   WELCOME TO COVID MANAGEMENT SYSTEM	:")
print(":	:")
print('*********************************************')
print("_______________________________________________")
print(" ---MAKING HEALTH CARE BETTER TOGETHER --- ")
print("________________________________________________")
print("PRESS 1 TO LOGIN")
print("_____________")
print("PRESS 2 TO EXIT")
print("______________")
choice = int(input("ENTER YOUR CHOICE:"))

##########login menu#############

users = ["Falguni", "Devvrat"]
if choice == 1:
    u1 = input("enter Admin name:")
    pwd1 = input("enter the password:")
    while u1 in users and pwd1 == '1234':
        print('logged in succesfully')
        print("****************************")
        print(":::::WELCOME ADMIN ::::::::")
        print("****************************")
        # MAIN MENU
        print('1.Reception details ')
        print("____________________________________________")
        print('2.Transport details')
        print("____________________________________________")
        print("3.Patient and family details")
        print("____________________________________________")
        print("4 Doctor details")
        print("____________________________________________")
        print("5.Vaccine details")
        print("____________________________________________")
        print('6.View all records')

        choice = int(input('ENTER YOUR CHOICE:'))
        if choice == 1:  # 1. Reception details	#SUB MENU1
            print('1.Wards Data ')
            print("___________________________________")
            print('2.Patient Transaction details')
            print("____________________________________________")

            ch1 = int(input('ENTER YOUR CHOICE:'))
            if ch1 == 1:  # Wards Data	#These are the choices in SUB MENU1
                ward = input('ward no:')
                ward_stat = input('occupied or vacant')
                beds = int(input('enter the no.of beds in ward:'))
                q1 = "insert into ward values('{}','{}',{})".format(ward, ward_stat, beds)
                mycursor.execute(q1)
                mydb.commit()

            elif ch1 == 2:  # Patient Transaction details
                b_name = input("enter the name of patient:")
                b_day = int(input("Enter the no. of days patient was admitted:"))
                b_room = int(input("Enter room no. of patient:"))
                b_pd = int(input("Enter the amount already deposited:"))
                b_pl = b_day * 30000 - b_pd
                b_mtd = input("Enter the payment method\a=cash\b=check\ c=online:")
                q = "insert into bill values('{}',{},{},{},{},'{}')".format(b_name, b_day, b_room, b_pd, b_pl, b_mtd)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED')
            else:
                print('please press valid key')

        elif choice == 2:  # 2. Transport details
            t_ambno = int(input("Enter the ambulance no."))
            t_drv = input("Enter the name of driver")
            t_mob = int(input("Enter the mobile no. of driver"))
            mycursor.execute("insert into transport values({},'{}',{})".format(t_ambno, t_drv, t_mob))
            mydb.commit()
            print('SUCCESSFULLY REGISTERED')

        elif choice == 3:  # 3. Patient and family details	#SUB MENU2
            print('1.Enter Patient Details')
            print("____________________________________________")
            print('2.Enter Patients family details:')
            print("____________________________________________")
            # this is the choices in 2nd submenu
            print("3.total no. of patients tested positive")
            print("____________________________________________")
            print("4.total patients recovered")
            print("____________________________________________")
            print("5.total patients died")
            print("____________________________________________")
            print("6.total patients under treatment")
            print("____________________________________________")
            print("7,update patient status")

            ch2 = int(input('ENTER YOUR CHOICE:'))

            if ch2 == 1:  # Patient details	#These are the choices in SUB MENU2
                p_name = input('Enter Patient Name:')
                p_admt = input('enter the admit date of patient:')
                p_age = int(input('Enter Age:'))
                p_mob = int(input('Enter Phone number:'))
                p_add = input("Enter patients locality:")
                p_stat = input("enter the present condition of patient => under treatment/recovered/dead")
                q = "insert into patient value('{}','{}',{},{},'{}','{}')".format(p_name, p_admt, p_age, p_mob, p_add,
                                                                                  p_stat)
                mycursor.execute(q)
                mydb.commit()
                print('SUCCESSFULLY REGISTERED')

            elif ch2 == 2:  # Family details
                k = int(input('No. of family members in contact with patient:'))
                n = int(input("No. of family members tested positive if any:"))
                d = int(input("No. of family members undergoing medical treatment:"))
                q = "insert into family values({},{},{})".format(k, n, d)
                mycursor.execute(q)
                mydb.commit()

            elif ch2 == 3:  # Total positive patients
                mycursor.execute("select count(p_name) as covid_patients from patient")
                c = mycursor.fetchone()
                for i in c:
                    print(i, "is the no. of covid payients till date")

            elif ch2 == 4:  # Recovered patients
                mycursor.execute("select count(p_stat) from patient where p_stat='recovered'")
                s = mycursor.fetchone()
                for i in s:
                    print(i, "is the no. of covid patients recovered")

            elif ch2 == 5:  # Total deaths
                mycursor.execute("select count(p_stat) from patient where p_stat='dead'")
                s = mycursor.fetchone()
                for i in s:
                    print(i, "is the no. of covid related deaths")

            elif ch2 == 6:  # Under treatment
                mycursor.execute("select count(p_stat) from patient where p_stat='under treatment'")
                s = mycursor.fetchone()
                for i in s:
                    print(i, "is the no. of covid patients under treatment")

            elif ch2 == 7:  # Update patient status
                l = input("enter the name of the patient for whom records are to be updated")
                k = input("enter new status")
                q = "update patient set p_stat='{}' where p_name='{}'".format(k, l)
                mycursor.execute(q)
                mydb.commit()

            else:
                print('please press valid key')

        elif choice == 4:  # 4. Doctor details
            d_name = input('Enter Doctor Name:')
            d_dept = int(input('Enter the Department:'))
            d_mob = int(input('Enter Phone number:'))
            mycursor.execute("insert into doctor values('{}',{},{})".format(d_name, d_dept, d_mob))
            print('successfully registered')
            mydb.commit()

        elif choice == 5:  # 5. Vaccine details	#SUB MENU3print('1.vaccine details')
            print("____________________________________________")
            print('2.total vaccinated patients')
            print("____________________________________________")
            print('3.check for aviliable vaccines')
            print("____________________________________________")
            ch3 = int(input('ENTER YOUR CHOICE:'))

            if ch3 == 1:  # Vaccine details	#These are the choices in SUB MENU3
                v_date = input("enter the date of arrival")
                v_no = int(input("enter the no. of vaccine arrived on perticular day"))
                v_pat = int(input("enter the no. of patients vaccinated on the day"))
                v_left = v_no - v_pat
                mycursor.execute(
                    "insert into vaccine_details values('{}',{},{},{})".format(v_date, v_no, v_pat, v_left))
                mydb.commit()

            elif ch3 == 2:  # Total vaccinated patients
                mycursor.execute("select sum(v_pat) as total_vaccinated_patient from vaccine_detail")
                c = mycursor.fetchone()
                for i in c:
                    print(i, "is the no. of patient vccinated")

            elif ch3 == 3:  # Check for available vaccines
                mycursor.execute("select sum(v_left) as total_vaccines_left from vaccine_detail")
                c = mycursor.fetchone()
                for i in c:
                    print(i, "are the total no. of vaccines left")

            else:
                print("please press a valid key")



        elif choice == 6:  # 6. View all records	#SUB MENU4
            print("1.Bill records ")
            print("____________________________________________")
            print('2.Transport records')
            print("____________________________________________")
            print("3.Patient records")
            print("____________________________________________")
            print("4.Family records")
            print("____________________________________________")
            print("5.Doctor  records")
            print("____________________________________________")
            print("6.Vaccine records")

            ch4 = int(input('ENTER YOUR CHOICE:'))

            if ch4 == 1:  # Reception: Ward & Bill records	#These are the choices in SUB MENU4
                print("--------Bill details---------")
                mycursor.execute("select*from bill")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 2:  # Transport records
                print("--------Transport details--------")
                mycursor.execute("select*from transport")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 3:  # Patient records
                print("--------Patient details--------")
                mycursor.execute("select*from patient")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 4:  # Family records
                print("--------Family details--------")
                mycursor.execute("select*from family")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 5:  # Doctor records
                print("--------Doctor details--------")
                mycursor.execute("select*from doctor")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            elif ch4 == 6:  # Vaccine records
                print("--------Vaccine details--------")
                mycursor.execute("select*from vaccine_detail")
                s = mycursor.fetchall()
                for i in s:
                    print(i)

            else:
                print("please press a valid key")
    else:
        print('wrong username&password')

if choice == 2:
    exit()

