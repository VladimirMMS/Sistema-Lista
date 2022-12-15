import string
import random

def createId():

    password_len = 5
    characters = string.ascii_letters

    return("".join(random.choice(characters) for _ in range(password_len)))
