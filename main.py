from signup import signup
from login import login
from menu import menu
from utils import clear

# Ex dee
userInfo = []


def choose():
    clear()
    print("Type 1 for signup or 2 for login:")
    choice = int(input("> "))
    clear()
    start(choice)


def start(choice):
    if choice == 1:
        signup()
    elif choice == 2:
        userInfo = login()
        if userInfo:
            print("Welcome back " + userInfo[0] + userInfo[1] + ".")
            menu(userInfo[3])
        else:
            print("Your username is incorrect.")
            input()
            choose()




choose()
