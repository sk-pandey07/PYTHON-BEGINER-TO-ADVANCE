def strike_time(strikes, time):
    intervals = strikes - 1
    time_per_interval = time / 5
    return intervals * time_per_interval
strikes = int(input("Enter number of strikes: "))
result = strike_time(strikes, 5)

print("Time taken:", result, "seconds")
