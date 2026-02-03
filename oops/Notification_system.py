class Notification:
    def send_notification(self, message):
        print("Notification:", message)

# main program
n = Notification()
n.send_notification("Your assignment is due today!")
