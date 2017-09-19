from random import randint

def get_username(surname, year_joined):
    surname = surname[0:3]
    year_joined = str(year_joined)
    year_joined = year_joined[2:]
    ran_numbers = ""
    for num in range(0,3):
        ran_numbers += str(randint(0,9))
    return surname + ran_numbers + str(year_joined)
