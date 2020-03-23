import random
import string


def password_length(valid):
    global wanted_password
    one = 1
    while one < 3:
        try:
            wanted_password = int(input("What length would you like your password to be? It needs to be at least 6 "
                                        "characters: "))
        except ValueError:
            print("Invalid answer.. You need to answer with a digit.")
        else:
            one += 3
    while wanted_password != valid:
        if wanted_password > 5:
            valid = wanted_password
            users_look(valid)
        elif wanted_password < 6:
            print("Invalid length!")
            wanted_password = int(input("New length: "))


def password_generator(string_length=6):
    digitsAndLetters = string.ascii_letters + string.digits
    return ''.join(random.choice(digitsAndLetters) for i in range(string_length))


def users_look(valid):
    print("Let´s generate some passwords:")
    print("First random password is " + password_generator(valid))
    print("Second random password is " + password_generator(valid))
    print("Third random password is " + password_generator(valid))
    user_pleased()


def user_pleased():
    pleased = input("Are you pleased with these passwords? Yes or no: ").lower()
    if pleased == 'no':
        print("Let´s generate som new passwords!")
        password_length(valid=150)
    else:
        exit()


password_length(valid=150)
