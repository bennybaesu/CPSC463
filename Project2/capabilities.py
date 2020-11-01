from tkinter import *
from tkinter import font as tkFont

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


def cap5():
    tk = Tk()

    # Font of bold Text
    boldFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

    # Title & Geometry Creation
    tk.title('Guest Profile')
    tk.geometry("1400x400+400+250")

    b = []

    # Initialize b:
    size_of_b = 12 + (len(guestList) * 12)
    for i in range(size_of_b):
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
    b[11].grid(row=0, column=9)

    b[12] = Button(text='ID Photo', font=boldFont)
    b[12].grid(row=0, column=10)

    # Print the guest information
    count = 12
    rowCount = 1
    for g in guestList:
        b[count] = Button(text=g.getFirstName())
        b[count].grid(row=rowCount, column=0)
        count = count + 1

        b[count] = Button(text=g.getLastName())
        b[count].grid(row=rowCount, column=1)
        count = count + 1

        b[count] = Button(text=str(g.getPhoneNumber()))
        b[count].grid(row=rowCount, column=2)
        count = count + 1

        b[count] = Button(text=g.getAddress())
        b[count].grid(row=rowCount, column=3)
        count = count + 1

        b[count] = Button(text=g.getCity())
        b[count].grid(row=rowCount, column=4)
        count = count + 1

        b[count] = Button(text=g.getState())
        b[count].grid(row=rowCount, column=5)
        count = count + 1

        b[count] = Button(text=str(g.getZip()))
        b[count].grid(row=rowCount, column=6)
        count = count + 1

        b[count] = Button(text=g.getEmail())
        b[count].grid(row=rowCount, column=7)
        count = count + 1

        temp = g.getID()

        b[count] = Button(text=temp[0])
        b[count].grid(row=rowCount, column=8)
        count = count + 1

        b[count] = Button(text=temp[1])
        b[count].grid(row=rowCount, column=9)
        count = count + 1

        b[count] = Button(text=g.getLicensePlate())
        b[count].grid(row=rowCount, column=9)
        count = count + 1

        b[count] = Button(text='Click to view ID', command=lambda: viewIdPhoto(g.getIdPhoto()))
        b[count].grid(row=rowCount, column=10)
        count = count + 1

        rowCount = rowCount + 1

    tk.mainloop()


def cap6():
    print(" ")
    # Capability 6 can go here


def cap7():
    print(" ")
    # Capability 7 can go here


def cap8():
    print(" ")
    # Capability 8 can go here
