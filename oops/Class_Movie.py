# Movie class example using OOP

class Movie:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration  # duration in minutes

    def display(self):
        print("Movie Name:", self.name)
        print("Duration:", self.duration, "minutes")


# Object creation
m1 = Movie("Inception", 148)
m1.display()
