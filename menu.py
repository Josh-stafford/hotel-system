import utils
from redeem import redeemDays

def menu(username):
    file = open("users/" + username + ".txt", "r")
    info = (file.read()).split("\n")

    utils.clear()
    print("1 -> Membership status\n"
          "2 -> Point Balance\n"
          "3 -> Days booked\n"
          "4 -> Account info\n"
          "5 -> Redeem points\n"
          "6 -> Logout")
    choice = int(input("> "))
    if choice == 1:
        print("Membership status: " + info[6])
        input()
        menu(info[3])
    elif choice == 2:
        print("Points balance: " + info[5])
        input()
        menu(info[3])
    elif choice == 3:
        print("Days booked: " + info[4])
        input()
        menu(info[3])
    elif choice == 4:
        print("Name: " + info[0] + info[1])
        print("Year joined: " + info[2])
        print("Username: " + info[3])
        input()
        menu(info[3])
    elif choice == 5:
        redeemDays(info)
        input()
        menu(info[3])
    elif choice == 6:
        print("Goodbye " + info[0] + info[1])

    file.close()