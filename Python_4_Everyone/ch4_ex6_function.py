
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        hours > 40
        othours = hours - 40
        regrate = (hours - othours) * rate
        otrate =  15 * othours
        pay = regrate + otrate

    return pay

shrs = input("Enter Hours:")
srate = input("Enter Rate: ")
fhrs = float(shrs)
frate = float(srate)

xp = computepay(fhrs, frate)

print("Pay: ",xp)
