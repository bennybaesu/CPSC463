import datetime


class Guest:
    def __init__(self):
        self.firstName = ' '
        self.lastName = ' '
        self.phoneNumber = 0000000000
        self.address = ' '
        self.city = ' '
        self.state = ' '
        self.zip = ' '
        self.email = ' '
        self.ID = [' ', ' ']
        self.licensePlate = ' '
        self.IdPhoto = ' ' # TODO: Set the ID Photo (Benny)

    def setFirstName(self, fn):
        self.firstName = fn

    def setLastName(self, ln):
        self.lastName = ln

    def setPhoneNumber(self, pn):
        self.phoneNumber = pn

    def setAddress(self, a):
        self.address = a

    def setCity(self, c):
        self.city = c

    def setState(self, s):
        self.state = s

    def setZip(self, z):
        self.zip = z

    def setEmail(self, e):
        self.email = e

    def setID(self, st, id):
        self.ID[0] = st
        self.ID[1] = id

    def setLicensePlate(self, lp):
        self.licensePlate = lp

    def setIdPhoto(self, p):
        self.IdPhoto = p

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPhoneNumber(self):
        return self.phoneNumber

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip

    def getEmail(self):
        return self.email

    def getID(self):
        return self.ID

    def getLicensePlate(self):
        return self.licensePlate

    def getIdPhoto(self):
        return self.IdPhoto
