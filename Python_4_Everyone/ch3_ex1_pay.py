# String hours inputed
shrs = input("Enter Hours:")
#String rate inputed
srate = input("Enter Rate: ")

try:
    #verifiy intiger or float was inputted
    #If float passed to "if" statement
    #non-float passed to except
    shrs = float(shrs)
    srate = float(srate)
except:
    #non-int changed to a -1
    #passed to 'if" statement
    shrs = -1
    srate = -1

#adding negatives creates negatives (which are less than zero, passed to else statement
#for qualified int adding them together will create a positive num greater then zero   
if shrs + srate > 0:
    
    #convert string hours to float hours
    fhrs = float(shrs)
    #convert string rate to float rate
    frate = float(srate)
    #check if hours worked are less of equal to 40
    if fhrs <= 40:
        #less than or equal to 40 simply multiple together 
        pay = fhrs * frate
        #print standard pay rate
        print("Pay", pay)
    elif fhrs > 40:
        #calculate over time hours
        oth = fhrs - 40
        #calculate regular pay without OT
        rrate = (fhrs - oth) * frate
        #calculate over time rate
        otr =  15 * oth
        #add regular pay to overtime pay
        otpay = rrate + otr
         # print pay
        print(otpay)
    #Should never execute but used just incase!!  
    else :
        print("oop!")
#Will execute if a non-float is inputed      
else:
    print("It needs to be a Number")
