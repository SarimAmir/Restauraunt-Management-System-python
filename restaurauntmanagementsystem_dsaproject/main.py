global username
global password
global _username
global _password
global admin_username
global admin_pass

def mainscreen():
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\n\tPress 1 to Login as Customer\n\tPress 2 to Register Yourself as customer\n\tPress 3 for Admin login\n\tPress 4 to View More Features")
    choice=int(input("\tEnter Selected Option:"))
    if choice==1:
        customerlogin()
    elif choice==2:
        customerregister()
    elif choice==3:
        adminlogin()
    elif choice==4:
        hadi_work()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()
def customerlogin():
    print("\n")
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\t\t-------Customer login Screen-------\n")
    _username=str(input("\tEnter Username:"))
    _password=str(input("\tEnter Password:"))
    if not _username or not _password:
        print("!!!!_____Fields cannot be empty._____!!!!")
        customerlogin()
    else:
        with open("registrations.txt") as f:
            if _username in f.read():
                with open("registrations.txt") as fp:
                    if _password in fp.read():
                        print("\tWelcome ,"+_username)
                        print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
                        print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                        choice=int(input("\t"))
                        if choice==1:
                            orders()
                        elif choice==2:
                            reservations()
                        elif choice==3:
                            mainscreen()
                        else:
                            print("\t!!!!_____Enter correct option_____!!!!\n")
                            print("\tWelcome ," + _username)
                            print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
                            print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                            choice = int(input("\t"))
                            if choice == 1:
                                orders()
                            elif choice == 2:
                                reservations()
                            elif choice == 3:
                                mainscreen()
                            else:
                                print("\t!!!!_____Enter correct option_____!!!!\n")

                    else:
                        print("\t!!__Wrong Password.__!!")
                        customerlogin()

            else:
                print("\t!!!___Wrong Username.___!!!\n\tPlease register first!")
                customerlogin()




def customerregister():
    print("\n")
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\t\t\t\t\t-------Customer Register Screen-------\n")
    username=str(input("\tEnter Username:"))
    password=str(input("\tEnter Password:"))
    if not username or not password:
        print("!!!!_____Fields cannot be empty._____!!!!")
        customerregister()
    else:
        file=open('registrations.txt','a')
        file.write(username+","+password+"\n")
        print(("\t===Registered Sucessfully==="))
        file.close()
        mainscreen()



def adminlogin():
    print("\n")
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\t\t\t\t\t-------Admin login screen-------")
    admin_username=str(input("\tEnter Username:"))
    admin_pass=str(input("\tEnter Password:"))
    if admin_username=="rameen" or admin_username=="Rameen" or admin_username=="hadi" or admin_username=="Hadi":
        if admin_pass=="admin":
            print("\t\tLogin Successful.\n\t\t=====Welcome Admin "+admin_username+"=====")
            admindashboard()
        else:
            print("\tIncorrect Password. Try again.!\n")
            adminlogin()
    else:
        print("\tInvalid Username. Try again.!\n")
        adminlogin()
def admindashboard():
    print("\n")
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\t\t\t\t\t-------Hello Admin-------")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()


def orders():
    global bill0
    global drinks
    global bill1
    global bill2
    global bill3
    global name
    global itemname
    global quantity
    global numofitems
    items=[]
    global totalbill
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\t\t-------Menu-------")
    print("\t****Burgers****\t\t****Fries*****\t\t\tMeetha")
    print("\t---------------\t\t--------------\t\t\t------")
    print("\t Zinger Rs 200\t\tPlain Fries Rs 100\t\t\tKheer Rs 120")
    print("\tBeef Burger Rs 170\tMayo Garlic Rs 130\t\t\t Zarda Rs 140")
    print()
    name=str(input("Enter Your Name:"))
    numofitems=int(input("How many categories do you want to order from?"))
    if numofitems==1:
        itemname=str(input("What do you wanna order?"))
        if itemname=="zinger" or itemname=="Zinger":
            items.append(itemname)
            quantity=int(input("How many do you wanna order?"))
            bill0=200*quantity
        elif itemname=="beef burger" or itemname=="Beef burger":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill0 = 170 * quantity
        elif itemname=="plain fries" or itemname=="Plain fries":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill0 = 100 * quantity
        elif itemname=="Mayo Garlic" or itemname=="mayo garlic":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill0 = 170 * quantity
        elif itemname=="kheer" or itemname=="Kheer":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill0 = 120 * quantity
        elif itemname=="zarda" or itemname=="Zarda":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            totalbill = 140 * quantity
        else:
            print("Enter correct name.!")
        print("Would you like a softdrink with your order?")
        choice=str(input("Enter Y for Yes N for No:"))
        if choice=="y" or choice=="Y":
            print("Do you want pepsi or 7up?")
            choice2=str(input())
            if choice2=="pepsi" or choice2=="Pepsi" or choice2=="7up":
                quan=int(input("How many do you want:"))
                drinks=60*quan
                totalbill = bill0 + drinks
                print("\tOrder Placed")
                file = open("orders.txt", 'a')
                file.write("-->Items, Name of Order-->" + name + ", Number of Items order-->" + str(numofitems) + ", Drinks-->" + choice2 + ", Drinks Quantity-->" + str(quan) + ", Drinks Total-->" + str(drinks) + ", Price of 1st item-->" + str(bill0) + ", Bill-->" + str(totalbill) + "\n")
                with open('orders.txt', 'a+') as filehandle:
                    for listitem in items:
                        filehandle.write('%s ,' % listitem)
                file.write("\n")
                file.close()
                print("------------------------------------------------")
                print("\t******Billing******")
                print("\t===================")
                print("Name:" + name)
                print("Ordered 1 item")
                print("1st item:",items, sep="\n")
                print("Price of 1st item:",bill0)
                print("Drinks        \t\t",drinks)
                print("------------------------------")
                print("Totalbill    \t\t", totalbill)
                print("------------------------------------------------")
                print("\n")
                print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                choice = int(input("\t"))
                if choice == 1:
                    orders()
                elif choice == 2:
                    reservations()
                elif choice == 3:
                    mainscreen()
                else:
                    print("!!!__Enter correct Input___!!!")
                    print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                    choice = int(input("\t"))
                    if choice == 1:
                        orders()
                    elif choice == 2:
                        reservations()
                    elif choice == 3:
                        mainscreen()


        else:
            print("\tOrder Placed")
            file = open("orders.txt", 'a')
            file.write("-->Items, Name of Order-->" + name + ", Number of Items order-->" + str(numofitems) + ", Price of 1st item-->" + str(bill0) + ", Bill-->" + str(bill0) + "\n")
            with open('orders.txt', 'a+') as filehandle:
                for listitem in items:
                    filehandle.write('%s ,' % listitem)
            file.write("\n")
            file.close()
            print("------------------------------------------------")
            print("\t******Billing******")
            print("\t===================")
            print("Name:" + name)
            print("Ordered 1 item")
            print("1st item:" ,items, sep="\n")
            print("Price of 1st item:", bill0)
            print("------------------------------")
            print("Totalbill    \t\t", bill0)
            print("------------------------------------------------")
            print("\n")
            print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
            choice = int(input("\t"))
            if choice == 1:
                orders()
            elif choice == 2:
                reservations()
            elif choice == 3:
                mainscreen()
            else:
                print("!!!__Enter correct Input___!!!")
                print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                choice = int(input("\t"))
                if choice == 1:
                    orders()
                elif choice == 2:
                    reservations()
                elif choice == 3:
                    mainscreen()






    elif numofitems==2:
        itemname=str(input("Enter first item name:"))
        if itemname=="zinger" or itemname=="Zinger":
            items.append(itemname)
            quantity=int(input("How many do you wanna order?"))
            bill1=200*quantity
        elif itemname=="beef burger" or itemname=="Beef burger":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill1 = 170 * quantity
        elif itemname=="plain fries" or itemname=="Plain fries":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill1 = 100 * quantity
        elif itemname=="Mayo Garlic" or itemname=="mayo garlic":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill1 = 170 * quantity
        elif itemname=="kheer" or itemname=="Kheer":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill1 = 120 * quantity
        elif itemname=="zarda" or itemname=="Zarda":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill1 = 140 * quantity
        else:
            print("Enter correct name.!")
        itemname = str(input("Enter second item name:"))
        if itemname == "zinger" or itemname == "Zinger":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill2 = 200 * quantity
        elif itemname == "beef burger" or itemname == "Beef burger":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill2 = 170 * quantity
        elif itemname == "plain fries" or itemname == "Plain fries":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill2 = 100 * quantity
        elif itemname == "Mayo Garlic" or itemname == "mayo garlic":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill2 = 170 * quantity
        elif itemname=="kheer" or itemname=="Kheer":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill2 = 120 * quantity
        elif itemname=="zarda" or itemname=="Zarda":
            items.append(itemname)
            quantity = int(input("How many do you wanna order?"))
            bill2 = 140 * quantity
        else:
            print("Enter correct name.!")
        totalbill=bill1+bill2
        print("Would you like a soft drink with your order")
        choice = str(input("Enter Y for Yes N for No:"))
        if choice=="y"or choice=="Y":
            print("Do you want pepsi or 7up?")
            choice2 = str(input())
            if choice2 == "pepsi" or choice2 == "Pepsi" or choice2 == "7up":
                quan = int(input("How many do you want:"))
                drinks=60*quan
                totalbill = totalbill + drinks
                print("\tOrder Placed")
                file=open("orders.txt",'a')
                file.write("-->Items, Name of Order-->"+name+", Number of Items order-->"+str(numofitems)+", Drinks-->"+choice2+", Drinks Quantity-->"+str(quan)+", Drinks Total-->"+str(drinks)+", Price of 1st item-->"+str(bill1)+", Price of 2nd item-->"+str(bill2)+", Bill-->"+str(totalbill)+"\n")
                with open('orders.txt','a+') as filehandle:
                    for listitem in items:
                        filehandle.write('%s ,'% listitem)
                file.write("\n")
                file.close()
                print("------------------------------------------------")
                print("\t******Billing******")
                print("\t===================")
                print("Name:" + name)
                print("Ordered 1 item")
                print("1st Item  2nd Item",items, sep="\n")
                print("Price of 1st item:", bill1)
                print("Price of 2nd item:", bill2)
                print("Drinks        \t\t", drinks)
                print("------------------------------")
                print("Totalbill    \t\t", totalbill)
                print("------------------------------------------------")
                print("\n")
                print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                choice = int(input("\t"))
                if choice == 1:
                    orders()
                elif choice == 2:
                    reservations()
                elif choice == 3:
                    mainscreen()
                else:
                    print("!!!__Enter correct Input___!!!")
                    print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                    choice = int(input("\t"))
                    if choice == 1:
                        orders()
                    elif choice == 2:
                        reservations()
                    elif choice == 3:
                        mainscreen()


        else:
            print("\tOrder Placed")
            file = open("orders.txt", 'a')
            file.write("-->Items, Name of Order-->" + name + ", Number of Items order-->" + str(numofitems) + ", Price of 1st item-->" + str(bill1) + ", Price of 2nd item-->" + str(bill2) + ", Bill-->" + str(totalbill) + "\n")
            with open('orders.txt', 'a+') as filehandle:
                for listitem in items:
                    filehandle.write('%s ,' % listitem)
            file.write("\n")
            file.close()
            print("------------------------------------------------")
            print("\t******Billing******")
            print("\t===================")
            print("Name:" + name)
            print("Ordered 1 item")
            print("1st Item  2nd Item", items, sep="\n")
            print("Price of 1st item:", bill1)
            print("Totalbill    \t\t", totalbill)
            print("------------------------------------------------")
            print("\n")
            print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
            choice = int(input("\t"))
            if choice == 1:
                orders()
            elif choice == 2:
                reservations()
            elif choice == 3:
                mainscreen()
            else:
                print("!!!__Enter correct Input___!!!")
                print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                choice = int(input("\t"))
                if choice == 1:
                    orders()
                elif choice == 2:
                    reservations()
                elif choice == 3:
                    mainscreen()


    elif numofitems==3:
            itemname = str(input("Enter first item name:"))
            if itemname == "zinger" or itemname == "Zinger":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill1 = 200 * quantity
            elif itemname == "beef burger" or itemname == "Beef burger":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill1 = 170 * quantity
            elif itemname == "plain fries" or itemname == "Plain fries":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill1 = 100 * quantity
            elif itemname == "Mayo Garlic" or itemname == "mayo garlic":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill1 = 170 * quantity
            elif itemname=="kheer" or itemname=="Kheer":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill1 = 120 * quantity
            elif itemname=="zarda" or itemname=="Zarda":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill1 = 140 * quantity
            else:
                print("Enter correct name.!")
            itemname = str(input("Enter second item name:"))
            if itemname == "zinger" or itemname == "Zinger":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill2 = 200 * quantity
            elif itemname == "beef burger" or itemname == "Beef burger":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill2 = 170 * quantity
            elif itemname == "plain fries" or itemname == "Plain fries":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill2 = 100 * quantity
            elif itemname == "Mayo Garlic" or itemname == "mayo garlic":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill2 = 170 * quantity
            elif itemname=="kheer" or itemname=="Kheer":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill2 = 120 * quantity
            elif itemname=="zarda" or itemname=="Zarda":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill2 = 140 * quantity
            else:
                print("Enter correct name.!")
            itemname = str(input("Enter third item name:"))
            if itemname == "zinger" or itemname == "Zinger":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill3 = 200 * quantity
            elif itemname == "beef burger" or itemname == "Beef burger":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill3 = 170 * quantity
            elif itemname == "plain fries" or itemname == "Plain fries":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill3 = 100 * quantity
            elif itemname == "Mayo Garlic" or itemname == "mayo garlic":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill3 = 170 * quantity
            elif itemname=="kheer" or itemname=="Kheer":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill3 = 120 * quantity
            elif itemname=="zarda" or itemname=="Zarda":
                items.append(itemname)
                quantity = int(input("How many do you wanna order?"))
                bill3 = 140 * quantity
            else:
                print("Enter correct name.!")
            totalbill=bill1+bill2+bill3
            print("Would you like a soft drink with your order?")
            choice = str(input("Enter Y for Yes N for No:"))
            if choice=="y" or choice=="Y":
                print("Do you want pepsi or 7up?")
                choice2 = str(input())
                if choice2 == "pepsi" or choice2 == "Pepsi" or choice2 == "7up":
                    quan = int(input("How many do you want:"))
                    drinks=60*quan
                    totalbill = totalbill + drinks
                    print("\tOrder Placed")
                    file = open("orders.txt", 'a')
                    file.write("-->Items, Name of Order-->" + name + ", Number of Items order-->" + str(numofitems) + ", Drinks-->" + choice2 + ", Drinks Quantity-->" + str(quan) + ", Drinks Total-->" + str(drinks) + ", Price of 1st item-->" + str(bill1) + ", Price of 2nd item-->" + str(bill2) + ", Price of 3rd item-->"+str(bill3)+", Bill-->" + str(totalbill) + "\n")
                    with open('orders.txt', 'a+') as filehandle:
                        for listitem in items:
                            filehandle.write('%s ,' % listitem)
                    file.write("\n")
                    file.close()
                    print("------------------------------------------------")
                    print("\t******Billing******")
                    print("\t===================")
                    print("Name:" + name)
                    print("Ordered 3 item")
                    print("1st Item  2nd Item   3rd Item", items, sep="\n")
                    print("Price of 1st item:", bill1)
                    print("Price of 2nd item:", bill2)
                    print("Price of 3nd item:", bill3)
                    print("Drinks        \t\t", drinks)
                    print("------------------------------")
                    print("Totalbill    \t\t", totalbill)
                    print("------------------------------------------------")
                    print("\n")
                    print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                    choice = int(input("\t"))
                    if choice == 1:
                        orders()
                    elif choice == 2:
                        reservations()
                    elif choice == 3:
                        mainscreen()
                    else:
                        print("!!!__Enter correct Input___!!!")
                        print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                        choice = int(input("\t"))
                        if choice == 1:
                            orders()
                        elif choice == 2:
                            reservations()
                        elif choice == 3:
                            mainscreen()


            else:
                file = open("orders.txt", 'a')
                file.write("-->Items, Name of Order-->" + name + ", Number of Items order-->" + str(numofitems)+", Price of 1st item-->" + str(bill1) + ", Price of 2nd item-->" + str(bill2) + ", Price of 3rd item-->" + str(bill3) + ", Bill-->" + str(totalbill) + "\n")
                with open('orders.txt', 'a+') as filehandle:
                    for listitem in items:
                        filehandle.write('%s ,' % listitem)
                file.write("\n")
                file.close()
                print("------------------------------------------------")
                print("\t******Billing******")
                print("\t===================")
                print("Name:" + name)
                print("Ordered 3 items")
                print("1st Item  2nd Item   3rd Item", items, sep="\n")
                print("Price of 1st item:", bill1)
                print("Price of 2nd item:", bill2)
                print("Price of 3nd item:", bill3)
                print("Totalbill    \t\t", totalbill)
                print("------------------------------------------------")
                print("\n")
                print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                choice = int(input("\t"))
                if choice == 1:
                    orders()
                elif choice == 2:
                    reservations()
                elif choice == 3:
                    mainscreen()
                else:
                    print("!!!__Enter correct Input___!!!")
                    print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
                    choice = int(input("\t"))
                    if choice == 1:
                        orders()
                    elif choice == 2:
                        reservations()
                    elif choice == 3:
                        mainscreen()


def reservations():
    global reserve_name
    global date
    global seats
    global time
    print("\n\t=====================WElCOME TO HOZZBY RESTAURANT MANAGEMENT SYSTEM========================")
    print("\t\t-------Reserve Your Table -------")
    reserve_name=str(input("\n Enter name for reservation:"))
    if not reserve_name:
        print("\t!!!__Enter a name__!!!")
        reservations()
    else:
        seats=int(input("\tFor how many people you want to reserve table?"))
        date=str(input("\tEnter date for reservation in DD/MM/YY format:"))
        time=str(input("\tEnter time for reservation in format XX.XX PM:"))
        print("\n")
        file=open("reservations.txt",'a')
        file.write(str(seats)+"-->Number of seats, "+reserve_name+"-->Name of reservation, "+str(date)+"--> Date for which reserved, "+str(time)+"-->Time for which reserved"+"\n")
        file.close()
        print("\t=======Reservation Done=======")
        print("\n")
        print("\t************************************************")
        print("\t------Details-------")
        print("\tName by which reservation is done:"+reserve_name)
        print("\tReserved for "+str(seats)+" people")
        print("\tTime for which reserved is:"+time)
        print("\tDate for which reserved is:"+date)
        print("\t************************************************")
        print("\n")
        print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
        choice = int(input("\t"))
        if choice == 1:
            orders()
        elif choice == 2:
            reservations()
        elif choice == 3:
            mainscreen()
        else:
            print("!!!__Enter correct Input___!!!")
            print("\tPress 1 to place Order\n\tPress 2 to make reservation\n\tPress 3 to Logout")
            choice = int(input("\t"))
            if choice == 1:
                orders()
            elif choice == 2:
                reservations()
            elif choice == 3:
                mainscreen()






def view_orders():
    print("***********************************************************************************************************************************************************************************************************************")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tOrder Details")
    file=open("orders.txt",'r')
    _orders = file.read()
    print(_orders)
    file.close()
    print("************************************************************************************************************************************************************************************************************************")
    print("\n")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()

def view_reservations():
    print("*************************************************************************************************************")
    print("\t\t\t\t\t\t\t\t\tReservation Details")
    file = open("reservations.txt", 'r')
    _reservations = file.read()
    print(_reservations)
    file.close()
    print("*************************************************************************************************************")
    print("\n")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()


def sort_reservations():
    print(("\n\tPress I for insertion sort\n\tPress B for bubble sort\n\tPress S for Selection sort\n\tPress Q for quick sort"))
    choice=str(input())
    if choice=="i" or choice=="I":
        insertionsort()
    elif choice=="b" or choice=="B":
        bubblesort()
    elif choice=="s" or choice=="S":
        selectionsort()
    elif choice=="q" or choice=="Q":
        quicksort()
    else:
        print("Enter correct input")
        sort_reservations()

def insertionsort():
    input_file = open('reservations.txt')

    lst = []
    for line in input_file:
        lst.append(line.strip())

    def insertion_sort(items):
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                j -= 1
        return items

    print("\t******Applying Insertion sort.....Done******")
    print(*insertion_sort(lst),sep="\n")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()


def bubblesort():
    input_file = open('reservations.txt')

    lst = []
    for line in input_file:
        lst.append(line.strip())

    def bubble_sort(arr):
        n = len(arr)

        for i in range(n):

            for j in range(0, n - i - 1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    print("\t******Applying Bubble sort.....Done******")
    print(*bubble_sort(lst), sep="\n")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()


def selectionsort():
    input_file = open('reservations.txt')

    lst = []
    for line in input_file:
        lst.append(line.strip())

    def selection_sort(arr):

        for i in range(len(arr)):

            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    print("\t******Applying Selection sort.....Done******")
    print(*selection_sort(lst),sep="\n")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to View Upcoming Menu Items\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()

def quicksort():
    input_file = open('reservations.txt')

    lst = []
    for line in input_file:
        lst.append(line.strip())

    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quick_Sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)

            quick_Sort(arr, low, pi - 1)
            quick_Sort(arr, pi + 1, high)
        return arr

    print("\t******Applying Quick sort.....Done******")
    print(*quick_Sort(lst,0,len(lst)-1),sep="\n")
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to View Upcoming Menu Items\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        mainscreen()


def searching_reservations():
    global datatosearch
    with open("reservations.txt") as openfile:
        datatosearch = input("Enter name of reservation:")
        for line in openfile:
            for part in line.rsplit("\n"):
                if datatosearch in part:
                    print("\tData Found")
                    print(part)
                    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to View Upcoming Menu Items\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
                    choice = int(input("\t"))
                    if choice == 1:
                        view_orders()
                    elif choice == 2:
                        view_reservations()
                    elif choice == 3:
                        sort_reservations()
                    elif choice == 4:
                        viewrecommendation()
                    elif choice == 5:
                        searching_reservations()
                    elif choice == 6:
                        employeenames()
                    elif choice == 7:
                        mainscreen()
                    else:
                        print("\t!!!!_____Enter correct option_____!!!!\n")
                        mainscreen()

                else:
                    print("Data not found")
                    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to View Upcoming Menu Items\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
                    choice = int(input("\t"))
                    if choice == 1:
                        view_orders()
                    elif choice == 2:
                        view_reservations()
                    elif choice == 3:
                        sort_reservations()
                    elif choice == 4:
                        viewrecommendation()
                    elif choice == 5:
                        searching_reservations()
                    elif choice == 6:
                        employeenames()
                    elif choice == 7:
                        mainscreen()
                    else:
                        print("\t!!!!_____Enter correct option_____!!!!\n")
                        mainscreen()


def searchorder():
    input_file = open('reservations.txt')
    lst = input_file.read()
    for line in input_file:
        lst.append(line.strip())
    global datatosearch
    datatosearch = input("\tEnter name of reservation:")

    def binary_search(arr, low, high, x):
        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

    result = binary_search(lst, 0, len(lst) - 1, datatosearch)
    if (result == -1):
        print("Not Found")
    else:
        print("\tData found \n"+str(result))


def searching_order():
    global datatosearch
    with open("orders.txt") as openfile:
        datatosearch = input("Enter name of order:")
        for line in openfile:
            for part in line.rsplit("\n"):
                if datatosearch in part:
                    print("\tData Found")
                    print(part)
                    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
                    choice = int(input("\t"))
                    if choice == 1:
                        view_orders()
                    elif choice == 2:
                        view_reservations()
                    elif choice == 3:
                        sort_reservations()
                    elif choice == 4:
                        viewrecommendation()
                    elif choice == 5:
                        searching_reservations()
                    elif choice == 6:
                        employeenames()
                    elif choice == 7:
                        mainscreen()
                    else:
                        print("\t!!!!_____Enter correct option_____!!!!\n")
                        mainscreen()

                else:
                    print("Data not found")
                    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
                    choice = int(input("\t"))
                    if choice == 1:
                        view_orders()
                    elif choice == 2:
                        view_reservations()
                    elif choice == 3:
                        sort_reservations()
                    elif choice == 4:
                        viewrecommendation()
                    elif choice == 5:
                        searching_reservations()
                    elif choice == 6:
                        employeenames()
                    elif choice == 7:
                        mainscreen()
                    else:
                        print("\t!!!!_____Enter correct option_____!!!!\n")
                        mainscreen()


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def viewrecommendation():
    q = Queue()
    q.enqueue("Pizzas")
    q.enqueue("Milkshakes")
    q.enqueue("Rolls")
    q.enqueue("Parathas")
    q.enqueue("Chai")
    print(q.size())
    print("First item we are going to include in our menu is: ",q.dequeue())
    print("Second item we are going to include in our menu is: ", q.dequeue())
    print("Third item we are going to include in our menu is: ", q.dequeue())
    print("\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        admindashboard()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def top(self):

        return self.head.data

    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def rem_printingofstack(self):

        temp = self.head
        while temp is not None:
            print(str(temp.data) + " ")
            temp = temp.next

def employeenames():
    stack = Stack()
    stack.push("Rameen")
    stack.push("Mehvish")
    stack.push("Zaina")
    stack.push("Zoya ")
    stack.push("Asma")
    stack.push("Tauseef")
    stack.push("Eimen")
    stack.push("Filza")
    stack.push("Zayan")
    stack.push("Sami")

    print("\t\tEmployess present in stack are:")
    print("\t\t------------------------------")
    stack.rem_printingofstack()
    print("\t\t-----------------------------------------------------------")
    print("\t\tNumber of Employees present in Stack:" + str(stack.length()))
    print("\t\tNewest Employee is: ", stack.top()," (top name in stack)")
    print("\t\tMost newest employee is:", stack.pop()," (first name popped out of stack)")
    print("\t\tSecond newest employee is:", stack.pop()," second name popped out of stack")
    print("\t\t-----------------------------------------------------------")
    print("\n\t\tStack after popping of two times is:")
    print("\t\t---------------------------------------")
    stack.rem_printingofstack()
    print(
        "\n\t Press 1 to view Orders\n\tPress 2 to view Reservations\n\tPress 3 to sort Reservations\n\tPress 4 to view recommendation\n\tPress 5 to search a Reservation\n\tPress 6 view name of Employees\n\tPress 7 to go back to main menu ")
    choice = int(input("\t"))
    if choice == 1:
        view_orders()
    elif choice == 2:
        view_reservations()
    elif choice == 3:
        sort_reservations()
    elif choice == 4:
        viewrecommendation()
    elif choice == 5:
        searching_reservations()
    elif choice == 6:
        employeenames()
    elif choice == 7:
        mainscreen()
    else:
        print("\t!!!!_____Enter correct option_____!!!!\n")
        admindashboard()


#_______________Hadi's work beginning now_____________________
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List
class RestaurantManagementSystem:
    def __init__(self):
        self.head = None
        self.tail = None

    # DS
    def append_value(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # DS
    def insertion_sort(self):
        current = self.head
        for _ in range(self.length() - 1):
            temp = current.next
            while temp:
                if temp.data < current.data:
                    current.data, temp.data = temp.data, current.data
                temp = temp.next
            current = current.next
        return self

    # DS
    def remove_value(self, key):
        current = self.head
        if current:
            if current.data == key:
                self.head = current.next
                return
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next

    def search_by_index(self, i):
        current = self.head
        count = 0
        while current:
            if i == count:
                return current.data
            current = current.next
            count += 1

    # DS
    def binary_search(self, key):
        start = 0
        stop = self.length() - 1
        self.insertion_sort()
        while start <= stop:
            mid = (start + stop) // 2
            if key == self.search_by_index(mid):
                return f'{key} found at index: {mid}'
            elif key > self.search_by_index(mid):
                start = mid + 1
            else:
                stop = mid - 1
        return f'{key} not found'

    def __str__(self):
        to_print = ''
        current = self.head
        while current is not None:
            to_print += f'{current.data}->'
            current = current.next
        if to_print:
            return f'[{to_print[:-2]}]'
        return '[]'

    def file(self, something):
        with open('filename', 'a') as file:
            file.write(f'{something}\n')

    def resturant_policies(self):
        print()
        print("\t\t-------------- THE RESTAURANT POLICIES ARE: --------------\n")
        print(
            "1. The most important policies for a restaurant/food service operation to enforce is proper hand washing procedures.\n"
            "2. Please wait for at least 30 minutes after your order.\n"
            "3. Political & inappropriate discussions are not allowed.\n"
            "4. Bring water or drinks as soon as customer asks.\n"
            "5. Don’t clear dishes until the customer is really finished with them.\n"
            "6. Don't Overbook Reservations.\n"
            "7. Understand How Restaurant Tipping Works.\n"
            "8. Always Ask for Customer Feedback\n"
            "9. Know How to Handle Disruptive Customers.\n"
            "10. Smoking Is Not Allowed In Restaurant's Premises.\n")
def hadi_work():
    print("\nPress 1 For Chef\'s Special.... ")
    print("Press 2 For Total Numbers Of Chef....")
    print("Press 3 For Chef\'s In Order....")
    print("Press 4 For Searching Chefs....")
    print("Press 5 For Popular Items....")
    print("Press 6 For Removing Items....")
    print("Press 7 for Restaurant Policies....")
    print("Press 8 for exit....")

    while True:
        # Object
        rms = RestaurantManagementSystem()

        choice = int(input("\nPlease Enter Your Choice: "))

        if choice == 1:
            # Values Append
            rms.append_value("\'\n\ti. Italian Chef\'")
            rms.append_value("\'\n\tii. Mexican Chef\'")
            rms.append_value("\'\n\tiii. Turkish Chef\'")
            rms.append_value("\'\n\tiv. Arabian Chef\'")
            rms.append_value("\'\n\tv. Pakistani Chef\'")
            rms.append_value("\'\n\tvi. Chinese Chef\'")
            rms.append_value("\'\n\tvii. Indian Chef\'")
            rms.append_value("\'\n\tviii. Philippian Chef\'")
            rms.append_value("\'\n\tix. Greek Chef\'")
            rms.append_value("\'\n\tx. Thai Chef\'")
            rms.append_value("\'\n\txi. Swedish Chef\'")
            rms.append_value("\'\n\txii. Australian Chef\'")
            # Returning Values
            print(f'\nChef\'s Special: {rms}\n')
            rms.file(rms)

            choice = input("Enter Your Desire Chef Code: ")
            if choice == "I":
                print("Italian Chef:\nThis Chef Is Expert In Ragu Alla Bolognese.")
            elif choice == "M":
                print("Mexican Chef:\nThis Chef Is Expert In Chiles En Nogada.")
            elif choice == "T":
                print("Turkish Chef:\nThis Chef Is Expert In Döner Kebap.")
            elif choice == "Ar":
                print("Arabian Chef:\nThis Chef Is Expert In Kabsa.")
            elif choice == "P":
                print("Pakistani Chef:\nThis Chef Is Expert In Biryani.")
            elif choice == "C":
                print("Chinese Chef:\nThis Chef Is Expert In Peking Duck.")
            elif choice == "I":
                print("Indian Chef:\nThis Chef Is Expert In Butter Chicken.")
            elif choice == "Ph":
                print("Philippian Chef:\nThis Chef Is Expert In Longganisa.")
            elif choice == "G":
                print("Greek Chef:\nThis Chef Is Expert In Tzatziki.")
            elif choice == "T":
                print("Thai Chef:\nThis Chef Is Expert In Making Pad Thai.")
            elif choice == "S":
                print("Swedish Chef:\nThis Chef Is Expert In Kanelbulle.")
            elif choice == "Au":
                print("Australian Chef:\nThis Chef Is Expert In Roast lamb.")
            else:
                print("Please Enter Valid Chef!!!!")
                pass





        elif choice == 2:
            # Total Number of Chef's
            rms.append_value("\'\n\ti. Italian Chef\'")
            rms.append_value("\'\n\tii. Mexican Chef\'")
            rms.append_value("\'\n\tiii. Turkish Chef\'")
            rms.append_value("\'\n\tiv. Arabian Chef\'")
            rms.append_value("\'\n\tv. Pakistani Chef\'")
            rms.append_value("\'\n\tvi. Chinese Chef\'")
            rms.append_value("\'\n\tvii. Indian Chef\'")
            rms.append_value("\'\n\tviii. Philippian Chef\'")
            rms.append_value("\'\n\tix. Greek Chef\'")
            rms.append_value("\'\n\tx. Thai Chef\'")
            rms.append_value("\'\n\txi. Swedish Chef\'")
            rms.append_value("\'\n\txii. Australian Chef\'")
            print(rms)
            print(f'\nTotal Numbers of Chef\'s: {rms.length()}\n')

        elif choice == 3:

            # DS - Insertion Sort
            rms.append_value("\'\n\tItalian Chef\'")
            rms.append_value("\'\n\tMexican Chef\'")
            rms.append_value("\'\n\tTurkish Chef\'")
            rms.append_value("\'\n\tArabian Chef\'")
            rms.append_value("\'\n\tPakistani Chef\'")
            rms.append_value("\'\n\tChinese Chef\'")
            rms.append_value("\'\n\tIndian Chef\'")
            rms.append_value("\'\n\tPhilippian Chef\'")
            rms.append_value("\'\n\tGreek Chef\'")
            rms.append_value("\'\n\tThai Chef\'")
            rms.append_value("\'\n\tSwedish Chef\'")
            rms.append_value("\'\n\tAustralian Chef\'")

            print(f'\nChef\'s Special - In DisOrder: {rms}\n')

            print(f'Chef\'s Special- In Order: {rms.insertion_sort()}\n')

        elif choice == 4:

            # DS - Search
            rms.append_value("\'\n\ti. Italian Chef\'")
            rms.append_value("\'\n\tii. Mexican Chef\'")
            rms.append_value("\'\n\tiii. Turkish Chef\'")
            rms.append_value("\'\n\tiv. Arabian Chef\'")
            rms.append_value("\'\n\tv. Pakistani Chef\'")
            rms.append_value("\'\n\tvi. Chinese Chef\'")
            rms.append_value("\'\n\tvii. Indian Chef\'")
            rms.append_value("\'\n\tviii. Philippian Chef\'")
            rms.append_value("\'\n\tix. Greek Chef\'")
            rms.append_value("\'\n\tx. Thai Chef\'")
            rms.append_value("\'\n\txi. Swedish Chef\'")
            rms.append_value("\'\n\txii. Australian Chef\'")
            print(rms)

            print("\nChef\'s Positions Are: ")
            print(rms.binary_search("\'\n\tv. Pakistani Chef\'"))
            print(rms.binary_search("\'\n\tii. Mexican Chef\'"))



        elif choice == 5:

            # DS - Pop Items
            print("Popular Items: ")
            rms.append_value("\'\n\ti. Classic comfort food\'")
            rms.append_value("\'\n\tii. Local ingredients\'")
            rms.append_value("\'\n\tiii. Healthy kids' menus\'")
            rms.append_value("\'\n\tiv. CBD-infused foods/drinks\'")
            rms.append_value("\'\n\tv. Desi Foods\'")
            rms.append_value("\'\n\tvi. Vegetable-centric dishes\'")
            rms.append_value("\'\n\tvii. Gourmet versions of classics\'")
            rms.append_value("\'\n\tviii. White Castle Sliders\'")
            rms.append_value("\'\n\tix. Sonic Cherry Limeade\'")
            rms.append_value("\'\n\tx. Wendy's Frosty\'")
            rms.append_value("\'\n\txi. Pumpkin Slice Latte\'")
            rms.append_value("\'\n\txii. Taco Bell Burito\'")
            rms.append_value("\'\n\txiii. Tuity Fruity Shake\'")
            rms.append_value("\'\n\txiv. Mushroom Soup\'")
            rms.append_value("\'\n\txv. Chicken/Beef Chowmin\'")

            print(rms)
            rms.file(rms)

        elif choice == 6:

            # DS - Remove Value

            rms.append_value("\'\n\ti. Classic comfort food\'")
            rms.append_value("\'\n\tii. Local ingredients\'")
            rms.append_value("\'\n\tiii. Healthy kids' menus\'")
            rms.append_value("\'\n\tiv. CBD-infused foods/drinks\'")
            rms.append_value("\'\n\tv. Desi Foods\'")
            rms.append_value("\'\n\tvi. Vegetable-centric dishes\'")
            rms.append_value("\'\n\tvii. Gourmet versions of classics\'")
            rms.append_value("\'\n\tviii. White Castle Sliders\'")
            rms.append_value("\'\n\tix. Sonic Cherry Limeade\'")
            rms.append_value("\'\n\tx. Wendy's Frosty\'")
            rms.append_value("\'\n\txi. Pumpkin Slice Latte\'")
            rms.append_value("\'\n\txii. Taco Bell Burito\'")
            rms.append_value("\'\n\txiii. Tuity Fruity Shake\'")
            rms.append_value("\'\n\txiv. Mushroom Soup\'")
            rms.append_value("\'\n\txv. Chicken/Beef Chowmin\'")
            print(rms)
            print("\nSorry some of the Items are unavailable.Menu After Removing unavailable Items: ")
            rms.remove_value("\'\n\tvii. Gourmet versions of classics\'")
            rms.remove_value("\'\n\tx. Wendy's Frosty\'")
            rms.remove_value("\'\n\txiii. Tuity Fruity Shake\'")
            rms.remove_value("\'\n\tvi. Vegetable-centric dishes\'")

            print(f'\nPopular Items: {rms}\n')
        elif choice == 7:
            # Display Pol
            rms.resturant_policies()

        else:
            print("\n*************Thank You For Visiting. Have A Nice Day :-)***************")
            break

mainscreen()
