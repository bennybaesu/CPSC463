from tkinter import *
from tkinter import font as tkFont
from tkinter import Label as lb
from tkinter import Entry as entry
from datetime import datetime, timedelta
import reservation
import guest
import room

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


def onClick(args):
    if args == 1:
        name = input("Enter guest first name: ")
        lastName = input("Enter guest last name: ")
        checkin = input("Check in date: ")
        checkout = input("Check out date: ")
        roomType = input("Room Type: ")
        roomNumber = input("Room Number: ")
        totalCharge = input("Total Charge: ")
        rate = input("Rate: ")
        reservationSite = input("Reservation Site: ")

        newRoom = room.Room()
        newRoom.setRate(rate)
        newRoom.setType(roomType)
        newRoom.setRoomNumber(roomNumber)
        newRoom.setRate(rate)

        newGuest = guest.Guest()
        newGuest.setFirstName(name)
        newGuest.setLastName(lastName)

        r = reservation.Reservation()
        r.setGuest(newGuest)
        r.setCheckIn(checkin)
        r.setCheckOut(checkout)
        r.setRoom(newRoom)
        r.setReservationWebsite(reservationSite)
        r.setTotalCharge(totalCharge)
        reservationList.append(r)

    if args == 2:
        name = input("Enter Guest First Name to remove: ")
        for r in reservationList:
            if r.getGuest().getFirstName() == name:
                reservationList.remove(r)


def onReserveClick(btn):
    text = btn.cget("text")
    firstName = text.split()[0]

    for r in reservationList:
        if firstName == r.getGuest().getFirstName():
            print("            GUEST INFORMATION\n-----------------------------------------")
            print(firstName + " " + r.getGuest().getLastName())
            print("Checkin: %s Checkout: %s" % (r.getCheckIn(), r.getCheckOut()))
            print("%s Room #%s" % (r.getRoom().getType(), r.getRoom().getRoomNumber()))
            print("Nightly Rate: $%s Total Charge: $%s" % (r.getRoom().getRate(), r.getTotalCharge()))
            print("Booked at %s" % (r.getReservationWebsite()))

            response = input(
                "-----------------------------------------\nWould you like to make any changes? (y/n)\n-----------------------------------------\n")
            while response == "y":
                print("What would you like to change? ")
                change = input(
                    "(1) Check in\n(2) Checkout\n(3) Room Type\n(4) Room Number\n(5) Rate\n(6) Total Charge\n(7) Reservation Site\n")
                if change == "1":
                    checkIn = input("New Check In: ")
                    r.setCheckIn(checkIn)
                    response = input("Any other Changes? (y/n)")
                elif change == "2":
                    checkOut = input("New Check Out: ")
                    r.setCheckOut(checkOut)
                    response = input("Any other Changes? (y/n)")
                elif change == "3":
                    type = input("New Room Type: ")
                    r.getRoom().setType(type)
                    response = input("Any other Changes? (y/n)")
                elif change == "4":
                    number = input("New Room Number: ")
                    r.getRoom().setRoomNumber(number)
                    response = input("Any other Changes? (y/n)")
                elif change == "5":
                    rate = input("New Nightly Rate: ")
                    r.getRoom().setRate(rate)
                    response = input("Any other Changes? (y/n)")
                elif change == "6":
                    total = input("New Total Charge: ")
                    r.setTotalCharge(total)
                    response = input("Any other Changes? (y/n)")
                elif change == "7":
                    site = input("New Reservation Site: ")
                    r.setReservationWebsite(site)
                    response = input("Any other Changes? (y/n)")
            if response == "n":
                checkGuest = input("Check guest in? (y/n)")
                if checkGuest == "y":
                    cap6(r)
            print("Please close window to save changes and return to main menu")


# Added by Frank Mirando
def cap1_button_click(room_num):
    for res in reservationList:
        room_temp = res.getRoom()  # stores room object
        if room_temp.getRoomNumber() == room_num:  # if room match is found

            # Checks if the clicked room is Unavailable/Dirty
            if room_temp.getStatus() == 'Unavailable/Dirty':
                print("WARNING: Room " + str(room_num) + " is dirty. Would you like to change to available?")
                user_resp_dirt = input("y/n?\n")
                if user_resp_dirt == "y":
                    room_temp.setStatus('Available')
                    print("Room " + str(room_temp.getRoomNumber()) + " is now available.")
                elif user_resp_dirt == "n":
                    print("Room " + str(room_temp.getRoomNumber()) + " is still dirty.")
                    break

            # Checks if the clicked room is Unavailable/Maintenance
            elif room_temp.getStatus() == 'Unavailable/Maintenance':
                print(
                    "WARNING: Room " + str(room_num) + " is under maintenance. Would you like to change to available?")
                user_resp_maint = input("y/n?\n")
                if user_resp_maint == "y":
                    room_temp.setStatus('Available')
                    print("Room " + str(room_temp.getRoomNumber()) + " is now available.")
                elif user_resp_maint == "n":
                    print("Room " + str(room_temp.getRoomNumber()) + " is still under maintenance.")
                    break
            # If neither dirty or under maintenance, cap6 is displayed with guest info
            else:
                cap6(res)
                print("Room passed in: " + str(room_num))
                break


# Capability by Frank Mirando
def cap1():
    room_win = Tk()  # Creating a window object
    room_win.title('All Rooms')
    room_win.geometry("700x500")

    top_frame = Frame(room_win)
    top_frame.grid()

    button_list = []
    # Initialize empty button list before loop
    for y in range(len(roomList)):
        button_list.append(Button(text=' '))

    # TODO if room that is clicked is available, lead to screen for cap6 so user can enter guest_test info. Changes to occupied
    # TODO if room that is clicked is occupied, lead to screen for cap6 and user can mod any info

    # Verification that a room button is clicked
    def printMsg():
        print("Room clicked!")

    res_iter = 0
    # For loop to print room buttons
    for f in range(len(roomList)):
        button_list[f] = Button(top_frame, text=roomList[f].printInfo(), fg="BLACK",
                                command=lambda f=f: cap1_button_click(roomList[f].getRoomNumber()))
        button_list[f].grid(row=0, column=f)
        roomList[f].getRoomNumber()

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
    # TODO get guest_test information on each room along with the days they are staying
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

    # TODO get guest_test information on each room along with the days they are staying(if anything just hardcode for now)
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
    b[3] = Button(text="Room Type")
    b[3].grid(row=0, column=3)
    b[4] = Button(text="Room Number")
    b[4].grid(row=0, column=4)
    b[5] = Button(text="Total Charge")
    b[5].grid(row=0, column=5)
    b[6] = Button(text="Rate")
    b[6].grid(row=0, column=6)
    b[7] = Button(text="Reservation Site")
    b[7].grid(row=0, column=7)
    b[8] = Button(text="Status")
    b[8].grid(row=0, column=8)

    b[9] = Button(command=lambda: onClick(1), text="Add Reservation")
    b[9].grid(row=0, column=9)
    b[10] = Button(command=lambda: onClick(2), text="Delete Reservation")
    b[10].grid(row=1, column=9)

    count = 0
    rowNum = 1
    for r in reservationList:
        name = r.getGuest().getFirstName() + " " + r.getGuest().getLastName()
        b[count] = Button(text=name)
        b[count].grid(row=rowNum, column=0)
        b[count].configure(command=lambda btn=b[count]: onReserveClick(btn))

        checkin = r.getCheckIn()
        b[count] = Button(text=checkin)
        b[count].grid(row=rowNum, column=1)

        checkout = r.getCheckOut()
        b[count] = Button(text=checkout)
        b[count].grid(row=rowNum, column=2)

        roomType = r.getRoom().getType()
        b[count] = Button(text=roomType)
        b[count].grid(row=rowNum, column=3)

        room = r.getRoom().getRoomNumber()
        b[count] = Button(text=room)
        b[count].grid(row=rowNum, column=4)

        totalCharge = r.getTotalCharge()
        b[count] = Button(text=totalCharge)
        b[count].grid(row=rowNum, column=5)

        rate = r.getRoom().getRate()
        b[count] = Button(text=rate)
        b[count].grid(row=rowNum, column=6)

        site = r.getReservationWebsite()
        b[count] = Button(text=site)
        b[count].grid(row=rowNum, column=7)

        status = r.getRoom().getStatus()
        b[count] = Button(text=status)
        b[count].grid(row=rowNum, column=8)

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

    def onRoomClick(btn):
        print(btn.cget("text"))
        room = btn.cget("text")

        for r in housekeepingList:
            if r.getRoom().getRoomNumber() == room:
                print("--------------House Keeping Check List--------------")
                print("input (y) or leave blank")
                print("Room #%s: %s" % (r.getRoom().getRoomNumber(), r.getStatus()))
                bath = input("Bathroom: ")
                towels = input("Towels: ")
                sheets = input("Bed Sheets: ")
                vacuum = input("Vacuum: ")
                dust = input("Dusting: ")
                elec = input("Electronics: ")
                checkedIn = input("Is guest checked in? ")

                if bath == "y":
                    r.setBathroom(True)
                else:
                    r.setBathroom(False)
                if towels == "y":
                    r.setTowels(True)
                else:
                    r.setTowels(False)
                if sheets == "y":
                    r.setBedSheets(True)
                else:
                    r.setBedSheets(False)
                if vacuum == "y":
                    r.setVacuum(True)
                else:
                    r.setVacuum(False)
                if dust == "y":
                    r.setDusting(True)
                else:
                    r.setDusting(False)
                if elec == "y":
                    r.setElectronics(True)
                else:
                    r.setElectronics(False)

                for x in roomList:
                    if x.getRoomNumber() == r.getRoom().getRoomNumber():
                        if r.getBathroom() and r.getTowels() and r.getBedSheets() and r.getVacuum() and r.getDusting() and r.getElectronics():
                            if checkedIn == "y":
                                x.setStatus("Occupied")
                            else:
                                x.setStatus("Available")
                        else:
                            x.setStatus("Dirty")

                        print("Room #%s: %s" % (r.getRoom().getRoomNumber(), x.getStatus()))

                        changeStatus = input("Change room status? (y/n)")
                        if changeStatus == "y":
                            statusInput = input("What is the status of the room? ")
                            x.setStatus(statusInput)

                        print("Please Select another room or close the window to save and return to main menu")

    for r in housekeepingList:
        room = r.getRoomNumber()
        b[count] = Button(text=room)
        b[count].grid(row=rowNumb, column=0)
        b[count].configure(command=lambda btn=b[count]: onRoomClick(btn))
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
def cap5(guest_test):
    tk = Tk()

    # Function to edit the values
    def editInfo(attribute):
        newW = Toplevel()

        def quit():
            newW.destroy()
            newW.update()

        def update(var):
            reservationIndex = 0
            guestIndex = 0

            for c in range(0, len(guestList)):
                if guest_test == guestList[c]:
                    guestIndex = c
            for j in range(0, len(reservationList)):
                if guest_test == reservationList[j].getGuest():
                    reservationIndex = j

            if attribute == "First Name":
                guest_test.setFirstName(var)
                b[13]['text'] = var
            elif attribute == "Last Name":
                guest_test.setLastName(var)
                b[14]['text'] = var
            elif attribute == "Phone Number":
                guest_test.setPhoneNumber(int(var))
                b[15]['text'] = var
            elif attribute == "Address":
                guest_test.setAddress(var)
                b[16]['text'] = var
            elif attribute == "City":
                guest_test.setCity(var)
                b[17]['text'] = var
            elif attribute == "State":
                guest_test.setState(var)
                b[18]['text'] = var
            elif attribute == "Zip Code":
                guest_test.setZip(int(var))
                b[19]['text'] = var
            elif attribute == "Email Address":
                guest_test.setEmail(var)
                b[20]['text'] = var
            elif attribute == "ID State":
                guest_test.setID(var, guest_test.getID()[1])
                b[21]['text'] = var
            elif attribute == "ID Number":
                guest_test.setID(guest_test.getID()[0], var)
                b[22]['text'] = var
            elif attribute == "License Plate Number":
                guest_test.setLicensePlate(var)
                b[23]['text'] = var

            guestList[guestIndex] = guest_test
            reservationList[reservationIndex].setGuest(guest_test)

            tk.update()

            # Quit the pop-up window
            newW.destroy()
            newW.update()

        txt = "Enter " + attribute

        # Create text box:
        lb(newW, text=txt).grid(row=0, column=0)
        e1 = entry(newW)
        e1.grid(row=0, column=1)

        Button(newW, text='Cancel', command=quit).grid(row=3, column=0, pady=4)
        Button(newW, text='Update', command=lambda: update(e1.get())).grid(row=3, column=1, pady=4)

        print(e1.get())
        newW.mainloop()

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

    # Title & Geometry Creation
    tk.title('Guest Profile')
    tk.geometry("1300x100+400+250")

    b = []

    for i in range(26):
        b.append(Button(text=' '))

    # Print Column Titles:
    b[0] = Button(tk, text='Fist Name', font=boldFont)
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

    # Print the guest_test information

    b[13] = Button(tk, text=guest_test.getFirstName(), command=lambda: editInfo("First Name"))
    b[13].grid(row=1, column=0)

    b[14] = Button(tk, text=guest_test.getLastName(), command=lambda: editInfo("Last Name"))
    b[14].grid(row=1, column=1)

    b[15] = Button(tk, text=str(guest_test.getPhoneNumber()), command=lambda: editInfo("Phone Number"))
    b[15].grid(row=1, column=2)

    b[16] = Button(tk, text=guest_test.getAddress(), command=lambda: editInfo("Address"))
    b[16].grid(row=1, column=3)

    b[17] = Button(tk, text=guest_test.getCity(), command=lambda: editInfo("City"))
    b[17].grid(row=1, column=4)

    b[18] = Button(tk, text=guest_test.getState(), command=lambda: editInfo("State"))
    b[18].grid(row=1, column=5)

    b[19] = Button(tk, text=str(guest_test.getZip()), command=lambda: editInfo("Zip Code"))
    b[19].grid(row=1, column=6)

    b[20] = Button(tk, text=guest_test.getEmail(), command=lambda: editInfo("Email Address"))
    b[20].grid(row=1, column=7)

    temp = guest_test.getID()

    b[21] = Button(tk, text=temp[0], command=lambda: editInfo("ID State"))
    b[21].grid(row=1, column=8)

    b[22] = Button(tk, text=temp[1], command=lambda: editInfo("ID Number"))
    b[22].grid(row=1, column=9)

    b[23] = Button(tk, text=guest_test.getLicensePlate(), command=lambda: editInfo("License Plate Number"))
    b[23].grid(row=1, column=10)

    b[24] = Button(tk, text='Click to view ID', command=lambda: viewIdPhoto(guest_test.getIdPhoto()))
    b[24].grid(row=1, column=11)

    b[25] = Label(tk, text='Select attribute to edit')
    b[25].grid(row=2, column=0)

    tk.mainloop()


# Capability by Benjamin Baesu
def cap6(reservation_test):
    tk = Toplevel()

    # Function to edit the values
    def editInfo(attribute):
        newW = Toplevel()

        def quit_window():
            newW.destroy()
            newW.update()

        def update(var):
            reservationIndex = 0
            guestIndex = 0
            roomIndex = 0

            for j in range(0, len(reservationList)):
                if reservation_test == reservationList[j]:
                    reservationIndex = j
            for k in range(0, len(guestList)):
                if guest_temp == guestList[k]:
                    guestIndex = 0
            for l in range(0, len(roomList)):
                if room_temp == roomList[l]:
                    roomIndex = 0

            if attribute == "First Name":
                guest_temp.setFirstName(var)
                b[10]['text'] = var
            elif attribute == "Last Name":
                guest_temp.setLastName(var)
                b[11]['text'] = var
            elif attribute == "Room Number":
                room_temp.setRoomNumber(int(var))
                b[14]['text'] = var
            elif attribute == "Room Type":
                room_temp.setAddress(var)
                b[15]['text'] = var
            elif attribute == "Room Rate":
                guest_temp.setCity(var)
                b[16]['text'] = var
            elif attribute == "Total Charge":
                guest_temp.setState(var)
                b[17]['text'] = var
            elif attribute == "Payments Made":
                guest_temp.setZip(int(var))
                b[18]['text'] = var
            elif attribute == "Balance":
                guest_temp.setEmail(var)
                b[19]['text'] = var

            guestList[guestIndex] = guest_temp
            reservationList[reservationIndex].setGuest(guest_temp)
            reservationList[reservationIndex].setRoom(room_temp)
            roomList[roomIndex] = room_temp

            tk.update()

            # Quit the pop-up window
            newW.destroy()
            newW.update()

        attributeText = "Enter " + attribute

        # Create text box:
        lb(newW, text=attributeText).grid(row=0, column=0)
        e1 = entry(newW)
        e1.grid(row=0, column=1)

        Button(newW, text='Cancel', command=quit_window).grid(row=3, column=0, pady=4)
        Button(newW, text='Update', command=lambda: update(e1.get())).grid(row=3, column=1, pady=4)

        print(e1.get())
        newW.mainloop()

    def upDate(var):
        reservationIndex = 0
        for j in range(0, len(reservationList)):
            if reservation_test == reservationList[j]:
                reservationIndex = j

        if var == "checkin":
            if reservation_test.getCheckIn() < reservation_test.getCheckOut():
                x = reservation_test.getCheckIn() + timedelta(days=1)
                reservation_test.setCheckIn(x)
                b[12]['text'] = x
        else:
            x = reservation_test.getCheckOut() + timedelta(days=1)
            reservation_test.setCheckOut(x)
            b[13]['text'] = x

        reservationList[reservationIndex] = reservation_test

    def downDate(var):
        reservationIndex = 0
        for j in range(0, len(reservationList)):
            if reservation_test == reservationList[j]:
                reservationIndex = j

        if var == "checkin":
            if reservation_test.getCheckIn() >= datetime.today():
                x = reservation_test.getCheckIn() - timedelta(days=1)
                reservation_test.setCheckIn(x)
                b[12]['text'] = x
        else:
            if reservation_test.getCheckOut() >= reservation_test.getCheckIn():
                x = reservation_test.getCheckOut() - timedelta(days=1)
                reservation_test.setCheckOut(x)
                b[13]['text'] = x

        reservationList[reservationIndex] = reservation_test

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

    # Title & Geometry Creation
    tk.title('Current Stay')
    tk.geometry("1300x100+400+250")

    b = []

    for i in range(27):
        b.append(Button(text=' '))

    # Print Column Titles:
    b[0] = Button(tk, text='First Name', font=boldFont)
    b[0].grid(row=0, column=0)

    b[1] = Button(tk, text='Last Name', font=boldFont)
    b[1].grid(row=0, column=1)

    b[2] = Button(tk, text='Check In (yyyy-mm-dd)', font=boldFont)
    b[2].grid(row=0, column=2)

    b[3] = Button(tk, text='Check Out (yyyy-mm-dd)', font=boldFont)
    b[3].grid(row=0, column=3)

    b[4] = Button(tk, text='Room Number', font=boldFont)
    b[4].grid(row=0, column=4)

    b[5] = Button(tk, text='Room Type', font=boldFont)
    b[5].grid(row=0, column=5)

    b[6] = Button(tk, text='Room Rate', font=boldFont)
    b[6].grid(row=0, column=6)

    b[7] = Button(tk, text='Total Charge', font=boldFont)
    b[7].grid(row=0, column=7)

    b[8] = Button(tk, text='Payments Made', font=boldFont)
    b[8].grid(row=0, column=8)

    b[9] = Button(tk, text='Balance', font=boldFont)
    b[9].grid(row=0, column=9)

    # Print the reservation_test information
    guest_temp = reservation_test.getGuest()
    room_temp = reservation_test.getRoom()

    b[10] = Button(tk, text=guest_temp.getFirstName(), command=lambda: editInfo("First Name"))
    b[10].grid(row=2, column=0)

    b[11] = Button(tk, text=guest_temp.getLastName(), command=lambda: editInfo("Last Name"))
    b[11].grid(row=2, column=1)

    b[20] = Button(tk, text="up", command=lambda: upDate("checkin"))
    b[20].grid(row=1, column=2)

    checkin = reservation_test.getCheckIn()
    b[12] = Button(tk, text=checkin)
    b[12].grid(row=2, column=2)

    b[22] = Button(tk, text="down", command=lambda: downDate("checkin"))
    b[22].grid(row=3, column=2)

    b[21] = Button(tk, text="up", command=lambda: upDate("checkout"))
    b[21].grid(row=1, column=3)

    checkout = reservation_test.getCheckOut()
    b[13] = Button(tk, text=checkout)
    b[13].grid(row=2, column=3)

    b[23] = Button(tk, text="down", command=lambda: downDate("checkout"))
    b[23].grid(row=3, column=3)

    b[14] = Button(tk, text=str(room_temp.getRoomNumber()), command=lambda: editInfo("Room Number"))
    b[14].grid(row=2, column=4)

    b[15] = Button(tk, text=room_temp.getType(), command=lambda: editInfo("Room Type"))
    b[15].grid(row=2, column=5)

    txt = '$' + str(room_temp.getRate()) + ' per day'
    b[16] = Button(tk, text=txt, command=lambda: editInfo("Room Rate"))
    b[16].grid(row=2, column=6)

    txt = '$' + str(reservation_test.getTotalCharge())
    b[17] = Button(tk, text=txt, command=lambda: editInfo("Total Charge"))
    b[17].grid(row=2, column=7)

    txt = '$' + str(reservation_test.getPaymentsMade())
    b[18] = Button(tk, text=txt, command=lambda: editInfo("Payments Made"))
    b[18].grid(row=2, column=8)

    txt = '$' + str(reservation_test.getBalance())
    b[19] = Button(tk, text=txt, command=lambda: editInfo("Balance"))
    b[19].grid(row=2, column=9)

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

        print("Search for guest_test by:")
        for o in options:
            print(o)

        choice = int(input("Enter choice: "))

        if 1 <= choice <= 7:
            break
        else:
            print("That was an invalid option. Try again.")

    searcher = ' '
    searchList = []
    newList = []
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
        print("No guest_test matching that search criteria exists.")
    else:
        while True:
            print('List of guests matching search:')
            count = 1
            for i in searchList:
                name = '(' + str(count) + ') - ' + i.getFirstName() + ' ' + i.getLastName()
                print(name)

            choice = int(input("Enter the choice of which guest_test you would like to view: "))
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
    b[count] = Button(text = 'Quit back to Main Menu', command = lambda: quitWindow().grid(row=row, column=1, pady=4))
    b[count].grid(row=row, column=1)

    tk.mainloop()
