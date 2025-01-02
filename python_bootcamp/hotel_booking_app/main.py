import pandas as pd

hotels = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = hotels.loc[hotels["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        hotels.loc[hotels["id"] == self.hotel_id, "available"] = "no"
        hotels.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = hotels.loc[hotels["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_reservation(self):
        content = f"""Thank you for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.hotel_name}
        """
        return content


print(hotels)
hotel_ID = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = Reservation(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate_reservation())
else:
    print("Hotel has no availability")
