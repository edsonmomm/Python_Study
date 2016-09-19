# 
def computepay(h,r):
    pay = 0
    if hours <= 40 :
        pay = hours * rate
    else :
        extra = (hours - 40) * (rate * 1.5)
        pay = (40 * rate) + extra

    return pay

try:
    userInput = raw_input("Enter Hours:")
    hours = float(userInput)
    userInput = raw_input("Enter Rate:")
    rate = float(userInput)
except:
    print "Error, please enter numeric input"
    quit()

print rate, hours
grossPay = computepay(hours,rate)
print grossPay