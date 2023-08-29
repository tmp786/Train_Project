# Train_Project
import random


class train_info():
    def __init__(self, train_num, source, destination, avl_seats ):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.avl_seats = avl_seats


    def display_info(self):
        print("----------------")
        print(f'train_num : {self.train_num}')
        print(f'train_source : {self.source}')
        print(f'train_destination : {self.destination}')
        print(f'train_avl_seats : {self.avl_seats}')
        print("------------------")

    def Book_tickets(self,num_tickets):
        if num_tickets > self.avl_seats:
            return  None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.avl_seats -= num_tickets
            return pnr_list

class user:
    def __init__(self,u_name, u_age, u_gender,u_phone):
        self.u_name = u_name
        self.u_age = u_age
        self.u_gender = u_gender
        self.u_phone = u_phone

    def display_info(self):
        print("----------------")
        print(f'u_name : {self.u_name}')
        print(f'u_age : {self.u_age}')
        print(f'u_gender: {self.u_gender}')
        print(f'u_phone : {self.u_phone}')
        print("----------------")

class Ticket:
    def __init__(self,train,source,destination,user,pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.user = user
        self.pnr = pnr

    def display_info(self):
        print(f"Train number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR : {self.pnr}")
        for users in self.user:
            users.display_info()
        print()

class Register():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkpassword(self, password):
        return self.password == password


registers = [
    Register("vigi", "123")
]
login_register = None
while True:
    print("1. create an register:\n ")
    print("2.login")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        username = input("Enter UserName: ")
        password = input("Enter Your pin: ")
        registers.append(Register(username, password))
        print("Signup is Successfully")
    elif choice == 2:
        username = input("Enter UserName: ")
        password = input("Enter Your pin: ")
        for register in registers:
            if register.username == username and register.checkpassword(password):
                login_register = register
                break
        if login_register is None:
            print("Invalid Username or Password")
        else:
            print(
                f"\nLogin in as {login_register.username}\n\n------Avilable Train Details--------\n")
            break
    else:
        print("In valid Choice")
if login_register is not None:
    trains = [train_info("26783", "bangalore", "vellore", 100),
              train_info("17892", "chennai", "mangalore", 150)
    ]
for train in trains:
    train.display_info()


while True:
    try:
        train_num = input("Enter Train Number: ")
        num_tickets = int(input("Enter Number of tickets: "))
        if num_tickets <= 0:
            raise valueError("Number of tickets should be greater than 0")
        for train in trains:
            if train.train_num == train_num:
                if num_tickets > train.avl_seats:
                    raise valueError(
                        "Selected more tickets than available seats")  # If the number of tickets entered is more than
                         # the available seats, it will raise a ValueError with the message "Selected more tickets than available seats".)
                break
        else:
            raise ValueError("Invalid Train Number.")
        break
    except ValueError as e:
        print(f"Invalid Input: {e}")

train = None
for t in trains:
    if t.train_num == train_num:
        train = t
        break


if train is None:
    print("Invalid Train Number.")

else:
    users =[]
    for i in range(num_tickets):
        print(f"\n Enter details for user {i+1}: ")
        while True:
            try:
                u_name = input("Name : ")
                if not u_name:
                    raise ValueError("Name canot be empty")
                u_age = int(input("Age: "))
                if u_age <= 0 or u_age > 120:
                    raise ValueError("Invalid Age")
                u_gender = input("Gender: ")
                u_phone = input("Phone number: ")
                if not u_phone or len(u_phone) != 10 or not u_phone.isdigit():
                    raise valueError("Invalid Phone Number")
                user =user(u_name, u_age, u_gender, u_phone)
                users.append(user)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")

    pnr_list = train.Book_tickets(num_tickets)
    if pnr_list is None:
        print("Tickets not available")


    else:
        print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

        for i in range(num_tickets):
            ticket = Ticket(train, train.source, train.destination, [
                            users[i]], pnr_list[i])
            ticket.display_info()
            print("\n--------Thank You------- \n-------Safe Journey------")

