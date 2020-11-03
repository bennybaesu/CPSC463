# coding=utf-8
# CPSC 463 | SOFTWARE TESTING
# WRITTEN BY:
#           Benjamin Baesu (Capabilities 5 and 6)
#           Tristan Bui (Capabilities 7 and 8)
#           Frank Mirando (Capabilities 1 and 2)
#           Jeremy Viray (Capabilites 3 and 4)

import menu
import capabilities
import sample

guestList, roomList, reservationList = sample.getSampleData()

# Capability 1: Screen that shows all rooms and their current status.
# Capability 2: Screen showing a list of the rooms and who is staying in the room for each day for the next 7 days.
# Capability 3: A reservation screen showing a list of all reservations currently in the system
# Capability 4: A housekeeping screen to manage housekeeping
# Capability 5: A guest profile screen to show guest information
# Capability 6: Current stay screen showing a guest’s information for their current stay.
# Capability 7: A search screen to search for guests
# Capability 8: A daily report screen

print('Welcome to Hotel Management System\n')


while True:
    menuChoice = menu.printMenu()
    if menuChoice == 1:
        capabilities.cap1()

    elif menuChoice == 2:
        capabilities.cap2()

    elif menuChoice == 3:
        capabilities.cap3()

    elif menuChoice == 4:
        capabilities.cap4()

    elif menuChoice == 5:
        capabilities.cap5(guestList[1])

    elif menuChoice == 6:
        capabilities.cap6(reservationList[1])

    elif menuChoice == 7:
        capabilities.cap7()

    elif menuChoice == 8:
        capabilities.cap8()

    elif menuChoice == 0:
        break




