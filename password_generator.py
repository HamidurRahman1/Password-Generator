
import string
from random import *

s = "abcdeadgc"
# print(set(i for i in s if s.count(i) > 1))


class PasswordGenerator:

    __chars = string.punctuation + string.ascii_letters + string.digits

    @staticmethod
    def __generate_password(length=5):
        """generates a random password of the given length. Length must be 5 or greater"""

        try:
            length = int(length)
            if length >= 5:
                return "".join(choice(PasswordGenerator.__chars) for x in range(randint(5, length)))
        except ValueError:
            raise ValueError("Expected integer but given {} for `length`.".format(type(length)))

    @staticmethod
    def generate_password(length=5, from_chars=None):
        return PasswordGenerator.__generate_password(length)


try:
    p = PasswordGenerator.generate_password("7")
    print(p)
except Exception as e:
    print(e.args)

