
import string
from random import *

chars = string.punctuation + string.ascii_letters + string.digits


def generate_password(length=5):
    return "".join(choice(chars) for x in range(randint(5, length)))


p = generate_password(5)
print(len(p), p)

