class Room:
    def __init__(self):
        self.number = 000
        self.rate = 0000
        self.type = 'none'
        self.status = 'vacant'

    def setRoomNumber(self, n):
        self.number = n

    def setRate(self, r):
        self.rate = r

    def setType(self, t):
        self.type = t

    def setStatus(self, s):
        self.status = s

    def getRoomNumber(self):
        return self.number

    def getRate(self):
        return self.rate

    def getType(self):
        return self.type

    def getStatus(self):
        return self.status

    def printInfo(self):  # added by Frank
        # Return a formatted string with room number and type
        # Will print room status separately so I can change colors on button
        return 'Room {} \n({})\n'.format(self.number, self.type)
