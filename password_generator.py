
import string
from random import *

s = "abcdeadgc"
print(set(i for i in s if s.count(i) > 1))


class PasswordGenerator:

    __chars = string.punctuation + string.ascii_letters + string.digits

    @staticmethod
    def __generate_password(length=5):
        return "".join(choice(PasswordGenerator.__chars) for x in range(randint(5, length)))

    @staticmethod
    def generate_password(length=5):
        return PasswordGenerator.__generate_password(length)


p = PasswordGenerator.generate_password(5)
print(p)

