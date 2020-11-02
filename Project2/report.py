import datetime
import guest
import reservation
import room


class Report:
    def __init__(self):
        self.rented = 'Occupied'
        self.roomNumber = 000
        self.firstName = ' '
        self.lastName = ' '
        self.dateIn = datetime.datetime(2000, 1, 1)
        self.dateOut = datetime.datetime(2000, 1, 2)
        self.amountPaid = 0.00
        self.totalPaid = 0.00

    def setRented(self, r):
        self.rented = r

    def setRoomNumber(self, ro):
        self.roomNumber = ro

    def setFirstName(self, fn):
        self.firstName = fn

    def setLastName(self, ln):
        self.lastName = ln

    def setDateIn(self, di):
        self.dateIn = di

    def setDateOut(self, do):
        self.dateOut = do

    def setAmountPaid(self, ap):
        self.amountPaid = ap

    def setTotalPaid(self, tp):
        self.totalPaid = tp

    def getRented(self):
        return self.rented

    def getRoom(self):
        return self.room

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getDateIn(self):
        return self.dateIn

    def getDateOut(self):
        return self.dateOut

    def getAmountPaid(self):
        return self.amountPaid

    def getTotalPaid(self):
        return self.totalPaid
