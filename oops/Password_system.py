class User:
    def __init__(self):
        self.__password = "" 

    def set_password(self, pwd):   
        if len(pwd) >= 6:
            self.__password = pwd
        else:
            print("Password too short")

    def check_password(self, pwd):
        return self.__password == pwd

u = User()
u.set_password("python123")

if u.check_password("python123"):
    print("Login Successful")
else:
    print("Wrong Password")
