import datetime
from username import get_username
import utils

data = []


def signup():
    gender = int(input("Enter 1 for male or  2 for female:\n> "))

    if gender == 1:
        gender = "Mr."
    elif gender == 2:
        gender = "Ms."
    data.append(gender + "\n")
    utils.clear()

    surname = input("Enter your surname:\n> ")
    data.append(surname + "\n")
    year_joined = datetime.datetime.now().year
    data.append(str(year_joined) + "\n")
    username = get_username(surname, year_joined)
    data.append(username + "\n")
    utils.clear()

    print("How many days would you like to book?")
    days = str(input("> "))
    data.append(days + "\n")
    utils.clear()

    points = int(days) * 1000
    data.append(str(points) + "\n")
    if points >= 100000:
        data.append("Diamond")
    elif points >= 50000:
        data.append("Platinum")
    elif points >= 30000:
        data.append("Gold")
    elif points >= 10000:
        data.append("Silver")
    elif points < 10000:
        data.append("Bronze")


    users = open("users/" + username + ".txt", "w")
    for i in data:
        users.write(i)
    users.close()

    print("Your new username is " + username + ". Remember it for logging in.")

