# Train class example using OOP

class Train:
    def __init__(self, train_no, destination):
        self.train_no = train_no
        self.destination = destination

    def display(self):
        print("Train Number:", self.train_no)
        print("Destination:", self.destination)


# Object creation
t1 = Train(12345, "Mumbai")
t1.display()
