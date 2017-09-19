def clear():
    print("\n" * 100)


def edit(username, index, data, action):
    print("Editing...")
    file = open("users/" + username + ".txt", "r+")
    info = (file.read()).split("\n")
    if action == 0:
        #Subtract
        info[index] = str(int(info[index])-data)
        file.seek(0)
        for i in info:
            file.write(i + "\n")
        file.close()
    elif action == 1:
        info[index] = str(int(info[index]) + data)
        file.seek(0)
        for i in range(0,len(info)-1):
            file.write(info[i] + "\n")
        file.close()