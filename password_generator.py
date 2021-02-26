
import string
from random import *

chars = string.punctuation + string.ascii_letters + string.digits


def generate_password(length=5):
    return "".join(choice(chars) for x in range(randint(5, length)))


s = "abcdeadgc"
print(set(i for i in s if s.count(i) > 1))

p = generate_password(5)

