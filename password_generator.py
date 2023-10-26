import random
import string


def generate_password(min_length, characters=True, specials_characters=True):
    """

    :param min_length:
    :param characters:
    :param specials_characters:
    :return:
    """
    digits = string.digits
    letters = string.ascii_letters
    specials = string.punctuation

    database = digits
    if characters:
        database += letters
    if specials_characters:
        database += specials

    meet_criteria = False
    has_characters = False
    has_specials = False
    pwd = ''

    while not meet_criteria or len(pwd) < min_length:
        get_char = random.choice(database)
        pwd += get_char
        if get_char in letters:
            has_characters = True
        elif get_char in specials:
            has_specials = True

        meet_criteria = True
        if characters:
            meet_criteria = has_characters
        if specials_characters:
            meet_criteria = meet_criteria and has_specials

    return pwd


min_length = int(input("please enter your minimum password length:"))
characters = input("do you want to have characters?(y/n)").lower() == 'y'
special_characters = input("do you want to have special characters?(y/n)").lower() == 'y'
pwd = generate_password(min_length, characters, special_characters)
print("the password that you want is:", pwd)
