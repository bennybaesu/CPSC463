import room
import reservation
import sample


class Housekeeping:
    def __init__(self):
        self.room = room.Room()
        self.roomNumber = 0
        self.type = ' '
        self.status = ' '

        self.housekeepName = ' '
        self.clean = True
        self.bathroom = ' '
        self.towels = ' '
        self.bedSheets = ' '
        self.vacuum = ' '
        self.dusting = ' '
        self.electronics = ' '

    def setRoom(self, r):
        self.room = r
        self.roomNumber = self.room.getRoomNumber()
        self.type = self.room.getType()
        self.status = self.room.getStatus()

    def setHousekeepName(self, h):
        self.housekeepName = h

    def setBathroom(self, b):
        self.bathroom = b

    def setTowels(self, t):
        self.towels = t

    def setBedSheets(self, bs):
        self.bedSheets = bs

    def setVacuum(self, v):
        self.vacuum = v

    def setDusting(self, d):
        self.dusting = d

    def setElectronics(self, e):
        self.electronics = e

    def getRoom(self):
        return self.room

    def getRoomNumber(self):
        return self.roomNumber

    def getType(self):
        return self.type

    def getStatus(self):
        return self.status

    def getHousekeepName(self):
        return self.housekeepName

    def getBathroom(self):
        return self.bathroom

    def getTowels(self):
        return self.towels

    def getBedSheets(self):
        return self.bedSheets

    def getVacuum(self):
        return self.vacuum

    def getDusting(self):
        return self.dusting

    def getElectronics(self):
        return self.electronics
