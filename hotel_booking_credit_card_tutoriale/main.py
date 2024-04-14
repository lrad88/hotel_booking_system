
# this is my version of extending the classes and capabilities of an object
# oriented program

# the process of extending a program is to create a new
# class and then modify the loop, this can be seen in the
# credit_card class which was added later in the code

# when you want to add new features to a program you dont modify
# existing classes you just create new ones

import pandas as pd

df = pd.read_csv("/Users/khronikle/Desktop/"
                 "PycharmProjects/various/UdemyLessons/web-app3/"
                 "OOP_inheritance_tutorial/hotel_booking_credit_card_tutoriale/"
                 "hotels.csv", dtype={"id": str})
# dtype=str loads all csv data as strings, including the numbers, which
# will help to get rid of ValueErrors, but the better option would be
# to use dtype={"id":str} which will only load the id column as a string

df_cards = (pd.read_csv("/Users/khronikle/Desktop/"
                        "PycharmProjects/various/UdemyLessons/web-app3/"
                        "OOP_inheritance_tutorial/hotel_booking_credit_card_tutoriale/"
                        "cards.csv", dtype=str).to_dict(orient="records"))
# .to_dict can actually load the dataframe as a dictionary

# notice how the methods relate to class eg.
# Hotel -> book, or ReservationTicket -> generate

df_cards_security = pd.read_csv("/Users/khronikle/"
                                "Desktop/PycharmProjects/various/UdemyLessons/web-app3/"
                                "OOP_inheritance_tutorial/hotel_booking_credit_card_tutoriale/"
                                "card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        # this hotel_id is different to the hotel_id in the logic below
        self.hotel_id = hotel_id

        # the above line makes it so that hotel_id becomes a definition usable
        # anywhere in the Hotel class
        # instead of it being localised to __init__ function

        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    # above line outputs the hotel name when given the hotel id and is
    # then stored in the self.name variable

    def book(self):
        """Books a hotel by changing its availability from yes to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # above line changes the availability from yes to no
        df.to_csv("hotels.csv", index=False)

    # above line prevents python from adding another column index to the csv

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            # above line checks the data frame for the hotel_id and if it is the same
            # as the inputted hotel_id it will return True or "yes"
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        # customer_name is a local attribute of the __init__ method and so
        # customer_name has been turned into an attribute of the self instance
        # which will make it globally available within the Hotel class
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking information:
        Name: {self.customer_name}
        hotel name: {self.hotel.name}
        """
        return content


# the big question always is: what parameters should __init__ take ?
# to answer this question you should ask: what is the minimum set of
# parameters you need to instantiate a credit card object for example ?
# below the credit card class has been split between what is needed to
# identify the credit card holder and the data needed to validate
# a credit card payment

class CreditCard:
    def __init__(self, NUMBER):
        self.number = NUMBER

    def validate(self, expiratioN, holdeR, cvC):
        card_data = {"number": self.number, "expiration": expiratioN,
                     "holder": holdeR, "cvc": cvC}
        # dictionary relating credit  card data to strings
        if card_data in df_cards:
            return True


# if card data not in df_cards it will return a None value by default
# so there is no need to return False


class SecureCreditCard(CreditCard):
    # above is an example of inheritance. this class inherits all the
    # attributes and methods from the CreditCard class as shown in the
    # brackets. SecureCreditCard class is now known as a child class
    # and the CreditCard class is known as a parent class
    def authenticate(self, given_passworD):
        password = df_cards_security.loc[df_cards_security["number"]
                                         == self.number, "password"].squeeze()
        if password == given_passworD:
            return True
        else:
            return False


# above is an example of self.number method inherited from
# the CreditCard parent class


class Spa_Package(Hotel):
    def __init__(self, hotel_id):
        self.hotel_idZ = hotel_id

        self.nameZ = df.loc[df["id"] == self.hotel_idZ, "name"].squeeze()


class SpaTicket(Spa_Package):
    def __init__(self, CustomeRName, hotel_id):
        self.customer_namO = CustomeRName
        self.hotel_namO = hotel_id

    def generated(self):
        content = f"""
                You have just booked the spa package!
                Here is your booking information:
                Name: {self.customer_namO}
                hotel name: {self.hotel_namO.nameZ}
                """
        return content


print(df)

# below is the actual linear path that the user will take through the
# code to book a hotel, the classes are there to facilitate this
# process

hotel_ID = input("Enter id of the hotel: ")  # id input
hotel = Hotel(hotel_ID)  # inputted id is connected to Hotel class
# within the hotel_id variable

HoEtel = Spa_Package(hotel_ID)

if hotel.available():  # availability checked in hotels.csv

    credit_card = SecureCreditCard(NUMBER="1234")
    if credit_card.validate(expiratioN="12/26",
                            holdeR="JOHN SMITH", cvC="123"):
        passw = input("Enter your password: ")
        if credit_card.authenticate(given_passworD=passw):
            print("Your payment was taken at this point!")
            hotel.book()  # connects to the book method
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name,
                                                   hotel_obj=hotel)
            print(reservation_ticket.generate())

            print("Do you want to book a SPA package ? (y/n)")
            if input() == "y":
                print("Thank you for your SPA reservation!")
                print("Here is your SPA booking information:")
                spa_res_ticket = SpaTicket(CustomeRName=name,
                                           hotel_id=HoEtel)
                print(spa_res_ticket.generated())
            else:
                print("You're all set, Thanks for booking with us!")

        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with payment")
# prints whats in the generate method
else:
    print("Hotel is not available")
