from tkinter import *
from tkinter import font as tkFont
import datetime

import sample

guestList, roomList, reservationList = sample.getSampleData()


# Function to display ID photos
def viewIdPhoto(fileName):
    top = Toplevel()
    canvas = Canvas(top, width=500, height=300)
    canvas.pack()
    img = PhotoImage(file=fileName)
    canvas.create_image(20, 20, anchor=NW, image=img)
    top.mainloop()


def cap1():
    print(" ")
    # Capability 1 can go here


def cap2():
    print(" ")
    # Capability 2 can go here


def cap3():
    print(" ")
    # Capability 3 can go here


def cap4():
    print(" ")
    # Capability 4 can go here


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

    b[23] = Button(text=guest.getLicensePlate())
    b[23].grid(row=1, column=10)

    b[24] = Button(text='Click to view ID', command=lambda: viewIdPhoto(guest.getIdPhoto()))
    b[24].grid(row=1, column=11)

    tk.mainloop()


def cap6(reservation):
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
    b[0] = Button(text='Name', font=boldFont)
    b[0].grid(row=0, column=0)

    b[1] = Button(text='Check In (yyyy-mm-dd)', font=boldFont)
    b[1].grid(row=0, column=1)

    b[3] = Button(text='Check Out (yyyy-mm-dd)', font=boldFont)
    b[3].grid(row=0, column=2)

    b[5] = Button(text='Room Number', font=boldFont)
    b[5].grid(row=0, column=3)

    b[6] = Button(text='Room Type', font=boldFont)
    b[6].grid(row=0, column=4)

    b[7] = Button(text='Room Rate', font=boldFont)
    b[7].grid(row=0, column=5)

    b[8] = Button(text='Total Charge', font=boldFont)
    b[8].grid(row=0, column=6)

    b[9] = Button(text='Payments Made', font=boldFont)
    b[9].grid(row=0, column=7)

    b[11] = Button(text='Balance', font=boldFont)
    b[11].grid(row=0, column=8)

    # Print the reservation information
    guest = reservation.getGuest()
    room = reservation.getRoom()

    name = guest.getLastName() + ', ' + guest.getFirstName()
    b[13] = Button(text=name)
    b[13].grid(row=1, column=0)

    b[14] = Button(text=reservation.getCheckIn())
    b[14].grid(row=1, column=1)

    b[15] = Button(text=reservation.getCheckOut())
    b[15].grid(row=1, column=2)

    b[16] = Button(text=str(room.getRoomNumber()))
    b[16].grid(row=1, column=3)

    b[17] = Button(text=room.getType())
    b[17].grid(row=1, column=4)

    txt = '$' + str(room.getRate()) + ' per day'
    b[18] = Button(text=txt)
    b[18].grid(row=1, column=5)

    txt = '$' + str(reservation.getTotalCharge())
    b[19] = Button(text=txt)
    b[19].grid(row=1, column=6)

    txt = '$' + str(reservation.getPaymentsMade())
    b[20] = Button(text=txt)
    b[20].grid(row=1, column=7)

    txt = '$' + str(reservation.getBalance())
    b[21] = Button(text=txt)
    b[21].grid(row=1, column=8)

    tk.mainloop()


def cap7():
    print(" ")
    # Capability 7 can go here


def cap8():
    print(" ")
    # Capability 8 can go here
