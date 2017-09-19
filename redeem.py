import utils
from math import floor

def redeemDays(info):
    points = info[5]
    utils.clear()
    print("You currently have " + points + " points to spend.")

    if int(points) >= 25000:
        daysAvailable = floor(int(points)/25000)
        print("You may redeem " + str(daysAvailable) + " free days.")
        print("How many would you like to redeem?")
        toRedeem = int(input("> "))
        if toRedeem <= daysAvailable:
            utils.edit(info[3], 5, toRedeem*25000, 0)
            utils.edit(info[3], 4, toRedeem, 1)
            print("Days redeemed.")
    else:
        print("You do not have enough points to redeem any free days.")