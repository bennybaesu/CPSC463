import guest
import room
import datetime


class Reservation:
    def __init__(self):
        self.guest = ' '
        self.checkIn = datetime.datetime(2000, 1, 1, 15, 00)
        self.checkOut = datetime.datetime(2000, 1, 2, 11, 00)
        self.reservationDate = datetime.date(2000, 1, 1)
        self.room = ' '
        self.totalCharge = 0.00
        self.paymentsMade = 0.00
        self.balance = 0.00
        self.reservationWebsite = ' '

    def setGuest(self, g):
        self.guest = g

    def setCheckIn(self, ci):
        self.checkIn = ci

    def setCheckOut(self, co):
        self.checkOut = co

    def setReservationDate(self, rd):
        self.reservationDate = rd

    def setRoom(self, r):
        self.room = r

    def setTotalCharge(self, tc):
        self.totalCharge = tc

    def setPaymentsMade(self, pm):
        self.paymentsMade = pm

    def setBalance(self, b):
        self.balance = b

    def setReservationWebsite(self, rw):
        self.reservationWebsite = rw

    def getGuest(self):
        return self.guest

    def getCheckIn(self):
        return self.checkIn

    def getCheckOut(self):
        return self.checkOut

    def getRoom(self):
        return self.room

    def getTotalCharge(self):
        return self.totalCharge

    def getPaymentsMade(self):
        return self.paymentsMade

    def getBalance(self):
        return self.balance

    def getReservationWebsite(self):
        return self.reservationWebsite

    def getReservationDate(self):
        return self.reservationDate
