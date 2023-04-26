try:
    hours=float(input("hours:"))
    rate=float(input("rate:"))
except:
    print("Error, please enter numeric input")
    quit()
extra_hours=hours-40
if extra_hours >0:
    pay=((40*rate)+(extra_hours*(rate*1.5)))
else:
    pay=hours*rate
print("pay: ",pay)