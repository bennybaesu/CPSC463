# PRINT MENU FUNCTION
def printMenu():
    menu = ['(1) - Room Status',
            '(2) - 7 Day Guest List',
            '(3) - Current Reservations',
            '(4) - Manage Housekeeping',
            '(5) - Guest Profile',
            '(6) - Guest Stay Information',
            '(7) - Search Guests',
            '(8) - Daily Report',
            '(0) - QUIT']

    print("MENU:")
    for m in menu:
        print(m)

    while True:
        x = int(input("Enter your menu choice: "))
        if 0 <= x <= 8:
            break
        else:
            print('That is an invalid menu option. Try again.\n')

    return x
