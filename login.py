import os.path
def login():
    username = input("Username:\n> ")

    info = []
    fname = "users/" + username + ".txt"
    if os.path.isfile(fname):
        user = open(fname, "r")
        data = user.read()
        info = data.split("\n")
        user.close()
        return info
    else:
        return 0