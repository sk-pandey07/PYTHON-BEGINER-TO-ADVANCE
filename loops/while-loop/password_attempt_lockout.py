import time
attempts = 0
lose_count = 0
while True:
    password = input("enter password:")
    if password == "pyhon.123":
        print("correct password")
        break

    attempts += 1
    print("wrong password")

    if attempts == 3:
        lose_count += 1
        wait_time = lose_count * 10

        print("to many time")
        print("Try again after ",wait_time," second")

        time.sleep(wait_time)
        attempts = 0
