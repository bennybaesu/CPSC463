list1 = ['Jacque', "20", "714-609-5023", "37 Turtle Ridge", "May 5th", "May 8th"]
list2 = ["Cody", "7", "714-609-5023", "37 Turtle Ridge", "May 5th", "May 8th"]
list3 = ["Anthony James", "12", "714-609-5023 ", "37 Turtle Ridge ", "May 5th", "May 8th"]
list4 = ["Henry Betty", "18", "714-609-5023", "37 Turtle Ridge ", "May 5th", "May 8th"]
list5 = ["Mike Will", "6", "714-609-5023", "37 Turtle Ridge", "May 5th", "May 8th "]

# Take the name of the flower that you want to search in the list
print('Search for a guest_test')
print('')
print('You can search by Name, Room Number, Phone Number, Street Address, Check-In Date, or Check-Out Date')
print('')
search = input("Search: ")


def findElement(listName, searchElement):
    for value in listName:
        if value == searchElement:
            return True
        return False


if search in list1:
    for items in list1:
        print(items)
elif search in list2:
    for items in list2:
        print(items)
elif search in list3:
    for items in list3:
        print(items)
elif search in list4:
    for items in list4:
        print(items)
elif search in list5:
    for items in list5:
        print(items)
else:
    print("%s is not found in the list" % search)