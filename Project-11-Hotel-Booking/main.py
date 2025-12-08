import pandas as pd

df = pd.read_csv('hotels.csv',dtype={"id":str})
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id,"name"]
        pass

    def book(self):
        """Book the Hotel by changing its availablity to no"""
        df.loc[df["id"] == self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv",index=False)
        pass

    def available(self):
        """Check the availablity of the Hotel """
        availablity = df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availablity == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        pass
    def generate(self):
        content = f"""
            Thank You for your reservation
            here are your booking data:
            Name:{self.customer_name}
            Hotel name:{self.hotel}"""
        return content

class CreditCard:
    pass

print(df)
hotel_ID = input("Enter the id of the hotel")
hotel = Hotel(hotel_ID)

if hotel.available():

    # CREDIT CARD
    credit_number = input("Enter your credit card number of 16 digits")
    if len(credit_number) != 16:
        print("credit card number should be of 16 digits")
        credit_number = input("Enter your credit card number of 16 digits")
    expiration_date = input("Enter the expiration date in YYYY-MM format")
    holder = input("Enter the name of the account Holder")
    cvc = input("Enter the cvc")

    #Hotel book
    hotel.book()


    name = input("Enter your name")
    reservation_ticket = ReservationTicket(customer_name=name,hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel isn't free")