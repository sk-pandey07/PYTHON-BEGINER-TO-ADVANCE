bill = int(input("enter bill: "))
if(bill <= 0):
    print("invalid amount")
elif(bill >= 0 and bill <= 100):
    print("total: ",bill * 5)
elif(bill > 100 and bill <= 200):
    print("total: ",bill * 7)
else:
    print("total: ",bill * 10)
