from datetime import datetime
today = datetime.today()
print("Dog Age Calculator!")
print("Made By @RedstoneGuy9248 (Github)\n")
d, dy, y, dm, m = 0, 0, 0, 0, 0
while True:
    try:
        dobStr = input("Enter your dog's date of birth in the format: DD/MM/YYYY: ")
        dob = datetime.strptime(dobStr, "%d/%m/%Y")
        d = (today - dob).days
        if (d > 0):
            break
        else:
            print("\nERROR: Date is in the future. Please enter a date that is in the past.\n")
    except ValueError:
        print("\nERROR: Invalid Date, Please enter date in the format DD/MM/YYYY!! \n")



if(d > 365.25):
    dy = 15
    y = 1
    d -= 365.25


if(d > 365.25):
    dy += 9
    y = 2
    d -= 365.25



while(d > 365.25):
    dy += 4
    y += 1
    d -= 365.25



m = int(d/(365.25/12))

if(y == 0):
    dm = float(m*15)
elif(y == 1):
    dm = float(m*9)
elif(y > 1):
    dm =  float(m*4)



if (dm > 12):
    dy += (dm // 12)
    dm %= 12

dm = int(dm)
dy = int(dy)
print("\nYour dog's dog age is: {} Years and {} Months\n\n".format(dy,dm))

input("Press enter to exit.")
exit(0)
