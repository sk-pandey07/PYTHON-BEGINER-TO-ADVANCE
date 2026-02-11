# Library Book Management using OOP

class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("Book returned successfully.")
        else:
            print("Book was not issued.")

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print("Book Title:", self.title)
        print("Status:", status)

b1 = LibraryBook("Python Programming")

b1.display()
b1.issue_book()
b1.display()
b1.issue_book()
b1.return_book()
b1.display()
