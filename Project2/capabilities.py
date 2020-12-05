from tkinter import *
from tkinter import font as tkFont
import datetime

import sample

guestList, roomList, reservationList = sample.getSampleData()
housekeepingList = sample.getSampleHouskeeping()


# Function to display ID photos
def viewIdPhoto(fileName):
    top = Toplevel()
    canvas = Canvas(top, width=500, height=300)
    canvas.pack()
    img = PhotoImage(file=fileName)
    canvas.create_image(20, 20, anchor=NW, image=img)
    top.mainloop()

def editInfo():
    top = Toplevel()
    canvas = Canvas(top, width=500, height=300)
    canvas.pack()
    top.mainloop()


# Capability by Frank Mirando
def cap1():
    room_win = Tk()  # Creating a window object
    room_win.title('All Rooms')
    room_win.geometry("500x500")

    top_frame = Frame(room_win)
    top_frame.grid()

    button_list = []
    # Initialize empty button list before loop
    for y in range(len(roomList)):
        button_list.append(Button(text=' '))

    # TODO if room that is clicked is available, lead to screen for cap6 so user can enter guest info. Changes to occupied
    # TODO if room that is clicked is occupied, lead to screen for cap6 and user can mod any info
    # TODO if room is dirty, warns and asks user: yes -> change to available, no -> do nothing
    # TODO if room is in maintenance, warns and asks user: yes -> change to available, no -> do nothing

    # Verification that a room button is clicked
    def printMsg():
        print("Room clicked!")

    # TODO pass in reservation object according to which room was clicked
    # TODO
    # For loop to print room buttons
    for f in range(len(roomList)):
        button_list[f] = Button(top_frame, text=roomList[f].printInfo(), fg="BLACK",
                                command=lambda: cap6(reservationList[1]))
        button_list[f].grid(row=0, column=f)

    # Separate loop to display different colored status
    status_labels = []
    # Initialize empty list before loop
    for a in range(len(roomList)):
        status_labels.append(Label(text=' '))

    # Displays different colored statuses
    # If room is available, displayed as green. Anything else is displayed as red
    for x in range(len(roomList)):
        if roomList[x].getStatus() == 'Available':
            status_labels[x] = (Label(top_frame, text=roomList[x].getStatus(), fg="GREEN"))
            status_labels[x].grid(row=1, column=x)
        else:
            status_labels[x] = (Label(top_frame, text=roomList[x].getStatus(), fg="RED"))
            status_labels[x].grid(row=1, column=x)

    room_win.mainloop()





# Capability by Frank Mirando
def cap2():
    # TODO get guest information on each room along with the days they are staying
    # Window settings
    week_win = Tk()
    week_win.title('Weekly Schedule')
    week_win.geometry("900x600")
    cap2_frame = Frame(week_win)
    cap2_frame.pack()

    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

    # Will show the next 7 days in (mm/dd/yyyy)
    curr_date = datetime.datetime.today()  # Today's date

    # Initializing list for date buttons
    date_buttons = []
    for c in range(7):
        date_buttons.append(Button(text=' '))

    # Displays the next 7 dates
    for d in range(7):
        date_buttons[d] = Button(cap2_frame, text=curr_date.strftime("%m/%d/%y"), fg="BLACK", font=boldFont)
        date_buttons[d].grid(row=0, column=d + 1)
        curr_date = curr_date + datetime.timedelta(days=1)  # increments days

    room_col = []
    # Initialize empty list before loop
    for c in range(len(roomList)):
        room_col.append(Button(text=' '))

    # TODO get guest information on each room along with the days they are staying(if anything just hardcode for now)
    for r in range(len(roomList)):
        room_col[r] = Button(cap2_frame, text="Room " + str(roomList[r].getRoomNumber()), fg="BLACK", font=boldFont)
        room_col[r].grid(row=r + 1, column=0)




    # Hard coding names into columns for now for display purposes
    name1 = guestList[0].getFirstName() + ' ' + guestList[0].getLastName()
    name2 = guestList[1].getFirstName() + ' ' + guestList[1].getLastName()
    name3 = guestList[2].getFirstName() + ' ' + guestList[2].getLastName()
    name4 = guestList[3].getFirstName() + ' ' + guestList[3].getLastName()

    # Checked in
    guest1_ci = Label(cap2_frame, text=name1, fg="BLUE")
    guest1_ci.grid(row=1, column=6)

    guest2_ci = Label(cap2_frame, text=name2, fg="BLUE")
    guest2_ci.grid(row=2, column=6)

    guest3_ci = Label(cap2_frame, text=name3, fg="BLUE")
    guest3_ci.grid(row=3, column=6)

    guest4_ci = Label(cap2_frame, text=name4, fg="BLUE")
    guest4_ci.grid(row=4, column=6)

    # Checked out
    guest1_co = Label(cap2_frame, text=name1, fg="BLUE")
    guest1_co.grid(row=1, column=7)

    guest2_co = Label(cap2_frame, text=name2, fg="BLUE")
    guest2_co.grid(row=2, column=7)

    guest3_co = Label(cap2_frame, text=name3, fg="BLUE")
    guest3_co.grid(row=3, column=7)

    guest4_co = Label(cap2_frame, text=name4, fg="BLUE")
    guest4_co.grid(row=4, column=7)

    week_win.mainloop()


# Capability by Jeremy Viray
def cap3():
    tk = Tk()
    tk.title('Current Reservations')
    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)
    b = []
    for i in range(25):
        b.append(Button(text=' '))

    b[0] = Button(text='Guest Name', font=boldFont)
    b[0].grid(row=0, column=0)
    b[1] = Button(text="Check In")
    b[1].grid(row=0, column=1)
    b[2] = Button(text="Check Out")
    b[2].grid(row=0, column=2)
    b[3] = Button(text="Room Number")
    b[3].grid(row=0, column=3)
    b[4] = Button(text="Total Charge")
    b[4].grid(row=0, column=4)
    b[5] = Button(text="Current Balance")
    b[5].grid(row=0, column=5)
    b[6] = Button(text="Reservation Site")
    b[6].grid(row=0, column=6)

    count = 0
    rowNum = 1
    for r in reservationList:
        name = r.getGuest().getFirstName() + " " + r.getGuest().getLastName()
        b[count] = Button(text=name)
        b[count].grid(row=rowNum, column=0)

        checkin = r.getCheckIn()
        b[count] = Button(text=checkin)
        b[count].grid(row=rowNum, column=1)

        checkout = r.getCheckOut()
        b[count] = Button(text=checkout)
        b[count].grid(row=rowNum, column=2)

        room = r.getRoom().getRoomNumber()
        b[count] = Button(text=room)
        b[count].grid(row=rowNum, column=3)

        totalCharge = r.getTotalCharge()
        b[count] = Button(text=totalCharge)
        b[count].grid(row=rowNum, column=4)

        totalBalance = r.getBalance()
        b[count] = Button(text=totalBalance)
        b[count].grid(row=rowNum, column=5)

        site = r.getReservationWebsite()
        b[count] = Button(text=site)
        b[count].grid(row=rowNum, column=6)

        count += 1
        rowNum += 1

    tk.mainloop()


# Capability by Jeremy Viray
def cap4():
    tk = Tk()
    tk.title('Housekeeping')

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)
    b = []

    sizeOf = 8 + (len(housekeepingList) * 8)
    for i in range(sizeOf):
        b.append(Button(text=' '))

    b[0] = Button(text='Room', font=boldFont)
    b[0].grid(row=0, column=0)
    b[1] = Button(text="House Keeper", font=boldFont)
    b[1].grid(row=0, column=1)
    b[2] = Button(text="Bathroom", font=boldFont)
    b[2].grid(row=0, column=2)
    b[3] = Button(text="Towels", font=boldFont)
    b[3].grid(row=0, column=3)
    b[4] = Button(text="Bed Sheets", font=boldFont)
    b[4].grid(row=0, column=4)
    b[5] = Button(text="Vacuum", font=boldFont)
    b[5].grid(row=0, column=5)
    b[6] = Button(text="Dusting", font=boldFont)
    b[6].grid(row=0, column=6)
    b[7] = Button(text="Electronics", font=boldFont)
    b[7].grid(row=0, column=7)

    count = 8
    rowNumb = 1

    def printTrueFalse(value):
        if value:
            return "Yes"
        else:
            return "No"

    for r in housekeepingList:
        room = r.getRoomNumber()
        b[count] = Button(text=room)
        b[count].grid(row=rowNumb, column=0)
        count += 1

        housekeeper = r.getHousekeepName()
        b[count] = Button(text=housekeeper)
        b[count].grid(row=rowNumb, column=1)
        count += 1

        bathroom = r.getBathroom()
        b[count] = Button(text=printTrueFalse(bathroom))
        b[count].grid(row=rowNumb, column=2)
        count += 1

        towels = r.getTowels()
        b[count] = Button(text=printTrueFalse(towels))
        b[count].grid(row=rowNumb, column=3)
        count += 1

        bedsheets = r.getBedSheets()
        b[count] = Button(text=printTrueFalse(bedsheets))
        b[count].grid(row=rowNumb, column=4)
        count += 1

        vacuum = r.getVacuum()
        b[count] = Button(text=printTrueFalse(vacuum))
        b[count].grid(row=rowNumb, column=5)
        count += 1

        dust = r.getDusting()
        b[count] = Button(text=printTrueFalse(dust))
        b[count].grid(row=rowNumb, column=6)
        count += 1

        electronics = r.getElectronics()
        b[count] = Button(text=printTrueFalse(electronics))
        b[count].grid(row=rowNumb, column=7)
        count += 1
        rowNumb += 1

    tk.mainloop()


# Capability by Benjamin Baesu
def cap5(guest):
    tk = Tk()

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

    # Title & Geometry Creation
    tk.title('Guest Profile')
    tk.geometry("1300x100+400+250")

    b = []

    for i in range(25):
        b.append(Button(text=' '))

    # Print Column Titles:
    b[0] = Button(text='Fist Name', font=boldFont)
    b[0].grid(row=0, column=0)

    b[1] = Button(text='Last Name', font=boldFont)
    b[1].grid(row=0, column=1)

    b[2] = Button(text='Phone Number', font=boldFont)
    b[2].grid(row=0, column=2)

    b[3] = Button(text='Address', font=boldFont)
    b[3].grid(row=0, column=3)

    b[4] = Button(text='City', font=boldFont)
    b[4].grid(row=0, column=4)

    b[5] = Button(text='State', font=boldFont)
    b[5].grid(row=0, column=5)

    b[6] = Button(text='Zip Code', font=boldFont)
    b[6].grid(row=0, column=6)

    b[7] = Button(text='Email', font=boldFont)
    b[7].grid(row=0, column=7)

    b[8] = Button(text='ID State', font=boldFont)
    b[8].grid(row=0, column=8)

    b[9] = Button(text='ID Number', font=boldFont)
    b[9].grid(row=0, column=9)

    b[11] = Button(text='License Plate Number', font=boldFont)
    b[11].grid(row=0, column=10)

    b[12] = Button(text='ID Photo', font=boldFont)
    b[12].grid(row=0, column=11)

    # Print the guest information

    b[13] = Button(text=guest.getFirstName())
    b[13].grid(row=1, column=0)

    b[14] = Button(text=guest.getLastName())
    b[14].grid(row=1, column=1)

    b[15] = Button(text=str(guest.getPhoneNumber()))
    b[15].grid(row=1, column=2)

    b[16] = Button(text=guest.getAddress())
    b[16].grid(row=1, column=3)

    b[17] = Button(text=guest.getCity())
    b[17].grid(row=1, column=4)

    b[18] = Button(text=guest.getState())
    b[18].grid(row=1, column=5)

    b[19] = Button(text=str(guest.getZip()))
    b[19].grid(row=1, column=6)

    b[20] = Button(text=guest.getEmail())
    b[20].grid(row=1, column=7)

    temp = guest.getID()

    b[21] = Button(text=temp[0])
    b[21].grid(row=1, column=8)

    b[22] = Button(text=temp[1])
    b[22].grid(row=1, column=9)

    b[23] = Button(text=guest.getLicensePlate(), command=lambda: editInfo())
    b[23].grid(row=1, column=10)

    b[24] = Button(text='Click to view ID', command=lambda: viewIdPhoto(guest.getIdPhoto()))
    b[24].grid(row=1, column=11)

    tk.mainloop()


# Capability by Benjamin Baesu
def cap6(reservation):
    tk = Toplevel()

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

    # Title & Geometry Creation
    tk.title('Current Stay')
    tk.geometry("1300x100+400+250")

    b = []

    for i in range(25):
        b.append(Button(text=' '))

    # Print Column Titles:
    b[0] = Button(tk, text='Name', font=boldFont)
    b[0].grid(row=0, column=0)

    b[1] = Button(tk, text='Check In (yyyy-mm-dd)', font=boldFont)
    b[1].grid(row=0, column=1)

    b[3] = Button(tk, text='Check Out (yyyy-mm-dd)', font=boldFont)
    b[3].grid(row=0, column=2)

    b[5] = Button(tk, text='Room Number', font=boldFont)
    b[5].grid(row=0, column=3)

    b[6] = Button(tk, text='Room Type', font=boldFont)
    b[6].grid(row=0, column=4)

    b[7] = Button(tk, text='Room Rate', font=boldFont)
    b[7].grid(row=0, column=5)

    b[8] = Button(tk, text='Total Charge', font=boldFont)
    b[8].grid(row=0, column=6)

    b[9] = Button(tk, text='Payments Made', font=boldFont)
    b[9].grid(row=0, column=7)

    b[11] = Button(tk, text='Balance', font=boldFont)
    b[11].grid(row=0, column=8)

    # Print the reservation information
    guest = reservation.getGuest()
    room = reservation.getRoom()

    name = guest.getLastName() + ', ' + guest.getFirstName()
    b[13] = Button(tk, text=name)
    b[13].grid(row=1, column=0)

    b[14] = Button(tk, text=reservation.getCheckIn())
    b[14].grid(row=1, column=1)

    b[15] = Button(tk, text=reservation.getCheckOut())
    b[15].grid(row=1, column=2)

    b[16] = Button(tk, text=str(room.getRoomNumber()))
    b[16].grid(row=1, column=3)

    b[17] = Button(tk, text=room.getType())
    b[17].grid(row=1, column=4)

    txt = '$' + str(room.getRate()) + ' per day'
    b[18] = Button(tk, text=txt)
    b[18].grid(row=1, column=5)

    txt = '$' + str(reservation.getTotalCharge())
    b[19] = Button(tk, text=txt)
    b[19].grid(row=1, column=6)

    txt = '$' + str(reservation.getPaymentsMade())
    b[20] = Button(tk, text=txt)
    b[20].grid(row=1, column=7)

    txt = '$' + str(reservation.getBalance())
    b[21] = Button(tk, text=txt)
    b[21].grid(row=1, column=8)

    tk.mainloop()


def cap7():
    print('\n')

    while True:
        options = ['(1) - First Name',
                   '(2) - Last Name',
                   '(3) - Room Number',
                   '(4) - Phone Number',
                   '(5) - Street Address',
                   '(6) - Check In Date',
                   '(7) - Check Out Date']

        print("Search for guest by:")
        for o in options:
            print(o)

        choice = int(input("Enter choice: "))

        if 1 <= choice <= 7:
            break
        else:
            print("That was an invalid option. Try again.")

    searcher = ' '
    searchList = []


    if choice == 1:
        searcher = input("Enter first name you want to search by: ")
        for g in guestList:
            if g.getFirstName() == searcher:
                searchList.append(g)

    elif choice == 2:
        searcher = input("Enter last name you want to search by: ")
        for g in guestList:
            if g.getLastName() == searcher:
                searchList.append(g)
    elif choice == 3:
        searcher = input("Enter room number you want to search by: ")
        for r in reservationList:
            temp = r.getRoom()
            temp = temp.getRoomNumber()
            if str(temp) == searcher:
                searchList.append(r.getGuest())
    elif choice == 4:
        searcher = int(input("Enter phone number you want to search by: "))
        for g in guestList:
            if g.getPhoneNumber() == searcher:
                searchList.append(g)
    elif choice == 5:
        searcher = input("Enter street address you want to search by: ")
        for g in guestList:
            if g.getAddress() == searcher:
                searchList.append(g)
    elif choice == 6:
        searcher = input("Enter check-in date you want to search by (yyyy-mm-dd): ")
        for r in reservationList:
            if r.getCheckIn() == searcher:
                searchList.append(r.getGuest())
    elif choice == 7:
        searcher = input("Enter check-out date you want to search by (yyyy-mm-dd): ")
        for r in reservationList:
            if r.getCheckOut() == searcher:
                searchList.append(r.getGuest())

    if len(searchList) == 0:
        print("No guest matching that search criteria exists.")
    else:
        while True:
            print('List of guests matching search:')
            count = 1
            for i in searchList:
                name = '(' + str(count) + ') - ' + i.getFirstName() + ' ' + i.getLastName()
                print(name)

            choice = int(input("Enter the choice of which guest you would like to view: "))
            if 1 <= choice <= len(searchList):
                break
            else:
                print("That is an invalid option. Try again.")

        cap5(searchList[choice - 1])


def cap8():

    def quitWindow():
        tk.destroy()


    listOfReservationsToday = []
    today = datetime.date(2000, 1, 1)  # Hardcoded date, for now

    for r in reservationList:
        if r.getReservationDate() == today:
            listOfReservationsToday.append(r)

    tk = Tk()

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD)

    # Title & Geometry Creation
    tk.title("Today's Reservations")
    tk.geometry("1300x400+400+250")

    b = []
    moneyMade = 0

    for i in range(7 + (len(reservationList) * 5)):
        b.append(Button(text=' '))

    # Print Column Titles:
    b[0] = Button(text='Room Number', font=boldFont)
    b[0].grid(row=0, column=0)

    b[1] = Button(text='Guest Name', font=boldFont)
    b[1].grid(row=0, column=1)

    b[2] = Button(text='Date In (yyyy-mm-dd)', font=boldFont)
    b[2].grid(row=0, column=2)

    b[3] = Button(text='Date Out (yyyy-mm-dd)', font=boldFont)
    b[3].grid(row=0, column=3)

    b[4] = Button(text='Amount Paid', font=boldFont)
    b[4].grid(row=0, column=4)
    count = 5
    row = 1

    for r in reservationList:
        room = r.getRoom()
        b[count] = Button(text=room.getRoomNumber())
        b[count].grid(row=row, column=0)
        count += 1

        guest = r.getGuest()
        guestName = guest.getLastName() + ', ' + guest.getFirstName()
        b[count] = Button(text=guestName)
        b[count].grid(row=row, column=1)
        count += 1

        b[count] = Button(text=r.getCheckIn())
        b[count].grid(row=row, column=2)
        count += 1

        b[count] = Button(text=r.getCheckOut())
        b[count].grid(row=row, column=3)
        count += 1

        amountPaid = '$' + str(r.getTotalCharge())
        moneyMade += int(r.getTotalCharge())
        b[count] = Button(text=amountPaid)
        b[count].grid(row=row, column=4)
        count += 1
        row += 1

    row += 2
    b[count] = Button(text='Total Money Made Today:', font=boldFont)
    b[count].grid(row=row, column=0)

    moneyMadeString = '$' + str(moneyMade)
    b[count] = Button(text=moneyMadeString)
    b[count].grid(row=row, column=1)

    row += 1
    b[count] = Button(text='Quit back to Main Menu', command=lambda: quitWindow().grid(row=row, column=1, pady=4))
    b[count].grid(row=row, column=0)
    tk.mainloop()
