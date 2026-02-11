# HotelRoom class with billing system

class HotelRoom:
    def __init__(self, room_no, price_per_day, days):
        self.room_no = room_no
        self.price_per_day = price_per_day
        self.days = days

    def calculate_bill(self):
        return self.price_per_day * self.days

    def display(self):
        print("Room No:", self.room_no)
        print("Price per Day:", self.price_per_day)
        print("Number of Days:", self.days)
        print("Total Bill:", self.calculate_bill())

r1 = HotelRoom(101, 2000, 3)
r1.display()
