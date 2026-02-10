# User class with auto-generated user ID using class variable

class User:
    user_count = 0  

    def __init__(self, name):
        User.user_count += 1
        self.user_id = User.user_count
        self.name = name

    def display(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)


# Object creation
u1 = User("Rahul")
u2 = User("Anita")

u1.display()
print("-----")
u2.display()
