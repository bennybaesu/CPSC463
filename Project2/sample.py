import room
import guest
import reservation
from PIL import Image


def getSampleData():
    sampleGuest = [guest.Guest(), guest.Guest(), guest.Guest(), guest.Guest()]
    sampleRoom = [room.Room(), room.Room(), room.Room(), room.Room()]
    sampleReservation = [reservation.Reservation(), reservation.Reservation(), reservation.Reservation(),
                         reservation.Reservation()]

    # Filling out guest information
    sampleGuest[0].setFirstName('Bob')
    sampleGuest[1].setFirstName('Jerry')
    sampleGuest[2].setFirstName('Jessica')
    sampleGuest[3].setFirstName('Joe')

    sampleGuest[0].setLastName('Johnson')
    sampleGuest[1].setLastName('Jefferson')
    sampleGuest[2].setLastName('Lopez')
    sampleGuest[3].setLastName('Simmons')

    sampleGuest[0].phoneNumber(9511234567)
    sampleGuest[1].phoneNumber(9091430413)
    sampleGuest[2].phoneNumber(7148439514)
    sampleGuest[3].phoneNumber(7140001434)

    sampleGuest[0].setAddress('1234 Cario Ct')
    sampleGuest[1].setAddress('411 Fullerton Blvd')
    sampleGuest[2].setAddress('8911 Anderson Loop')
    sampleGuest[3].setAddress('654 Brookhurst Ave')

    sampleGuest[0].setCity('Boston')
    sampleGuest[1].setCity('Anaheim')
    sampleGuest[2].setCity('Fort Meade')
    sampleGuest[3].setCity('Omaha')

    sampleGuest[0].setState('Massachusetts')
    sampleGuest[1].setState('California')
    sampleGuest[2].setState('Maryland')
    sampleGuest[3].setState('Nebraska')

    sampleGuest[0].setZip(68340)
    sampleGuest[1].setZip(92882)
    sampleGuest[2].setZip(20755)
    sampleGuest[3].setZip(72400)

    sampleGuest[0].setEmail('bjohnson@yahoo.com')
    sampleGuest[1].setEmail('jjefferson@gmail.com')
    sampleGuest[2].setEmail('jlopez@hotmail.com')
    sampleGuest[3].setEmail('joesimmons@gmail.com')

    sampleGuest[0].setID('DL52548')
    sampleGuest[1].setID('QK10475')
    sampleGuest[2].setID('AA74143')
    sampleGuest[3].setID('XL59532')

    sampleGuest[0].setLicensePlate('8ABC523')
    sampleGuest[1].setLicensePlate('7JFS243')
    sampleGuest[2].setLicensePlate('8BOP997')
    sampleGuest[3].setLicensePlate('143G924')

    sampleGuest[0].setIdPhoto(Image.open('id-card.jpg'))
    sampleGuest[1].setIdPhoto(Image.open('id-card.jpg'))
    sampleGuest[2].setIdPhoto(Image.open('id-card.jpg'))
    sampleGuest[3].setIdPhoto(Image.open('id-card.jpg'))

    # Filling out room information
    sampleRoom[0].setRoomNumber(123)
    sampleRoom[1].setRoomNumber(225)
    sampleRoom[2].setRoomNumber(311)
    sampleRoom[3].setRoomNumber(478)

    sampleRoom[0].setRate(50)
    sampleRoom[1].setRate(100)
    sampleRoom[2].setRate(200)
    sampleRoom[3].setRate(600)

    sampleRoom[0].setType('Single Room')
    sampleRoom[1].setType('Double Room')
    sampleRoom[2].setType('Full Suite')
    sampleRoom[3].setType('Master Suite')

    sampleRoom[0].setStatus('Occupied')
    sampleRoom[1].setStatus('Occupied')
    sampleRoom[2].setStatus('Occupied')
    sampleRoom[3].setStatus('Occupied')

    # Filling out reservation information
    sampleReservation[0].setGuest(sampleGuest[0])
    sampleReservation[1].setGuest(sampleGuest[1])
    sampleReservation[2].setGuest(sampleGuest[2])
    sampleReservation[3].setGuest(sampleGuest[3])

    sampleReservation[0].setRoom(sampleRoom[0])
    sampleReservation[1].setRoom(sampleRoom[1])
    sampleReservation[2].setRoom(sampleRoom[2])
    sampleReservation[3].setRoom(sampleRoom[3])

    sampleReservation[0].setTotalCharge(50.00)
    sampleReservation[1].setTotalCharge(100.00)
    sampleReservation[2].setTotalCharge(200.00)
    sampleReservation[3].setTotalCharge(600.00)

    sampleReservation[0].setPaymentsMade(50.00)
    sampleReservation[1].setPaymentsMade(100.00)
    sampleReservation[2].setPaymentsMade(200.00)
    sampleReservation[3].setPaymentsMade(600.00)

    sampleReservation[0].setBalance(00.00)
    sampleReservation[1].setBalance(00.00)
    sampleReservation[2].setBalance(00.00)
    sampleReservation[3].setBalance(00.00)

    return sampleGuest, sampleRoom, sampleReservation


