
import string
from random import *

s = "abcdeadgc"
# print(set(i for i in s if s.count(i) > 1))


class PasswordGenerator:

    __chars = string.punctuation + string.ascii_letters + string.digits

    @staticmethod
    def __generate_password(length=7):
        """generates a random password of the given length. Length must be 7 or greater"""

        try:
            length = int(length)
            if length >= 7:
                return "".join(choice(PasswordGenerator.__chars) for x in range(randint(length, length)))
            else:
                return "".join(choice(PasswordGenerator.__chars) for x in range(randint(7, 7)))
        except ValueError:
            raise ValueError("Expected integer but given {} for `length`.".format(type(length)))

    @staticmethod
    def generate_password(length=7, from_chars=None):
        return PasswordGenerator.__generate_password(length)


try:
    p = PasswordGenerator.generate_password(5)
    print(len(p), p)
except Exception as e:
    print(e.args)

