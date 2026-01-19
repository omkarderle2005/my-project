appoinments = []


def bookappoinments():
    pname = input("enter patient name")
    dname = input("enter doctoer name")
    contact = input("enter contact")
    date = input("enter date (DD-MM-YYYY)")
    time = input("enter time:")
    appoinments.append([pname, dname, contact, date, time])
    print("appointment booked succesfully!\n")


def viewbooking():
    if not appoinments:
        print("no booking found.\n")
    else:
      for a in appoinments:
        print("patient:", a[0], "doctor", a[1], "contact", a[2], "date", a[3], "time", [4])
      print()


def searchbooking():
    sd = input("enter date to search (DD-MM-YYYY):")
    found = False
    for a in appoinments():
        if a[3] == sd:
            print("patient", a[0], "doctor", a[1], "contact", a[2], "time", a[4])
            found = True
        if not found:
            print("No booking found on this date.\n")

def menu():
        print("1. book appointment")
        print("2. view Booking ")
        print("3. search booking by dates")
        print("4. Exit")
        choice = input("enter your choice:")
        if choice == "1":
            bookappoinments()
            menu()
        elif choice == '2':
            viewbooking()
            menu()
        elif choice == '3':
            searchbooking()
            menu()
        else:
            print("thnk you!")
            menu()

menu()
