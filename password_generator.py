
import string
from random import *

s = "abcdeadgc"
# print(set(i for i in s if s.count(i) > 1))

CHARS = string.punctuation + string.ascii_letters + string.digits
MIN_LENGTH = 7


class PasswordGenerator:

    @staticmethod
    def __generate_password(length=MIN_LENGTH, from_string=CHARS):
        """generates a random password of the given length. Length must be 7 or greater"""

        try:
            if length >= MIN_LENGTH:
                return "".join(choice(CHARS) for x in range(randint(length, length)))
            else:
                return "".join(choice(CHARS) for x in range(randint(MIN_LENGTH, MIN_LENGTH)))
        except ValueError:
            raise ValueError("Expected integer but given {} for `length`.".format(type(length)))

    @staticmethod
    def generate_password(length=MIN_LENGTH, from_string=CHARS):
        try:
            length = int(length)
            if isinstance(from_string, str):
                return PasswordGenerator.__generate_password(length)
            return PasswordGenerator.__generate_password(length)
        except ValueError:
            raise ValueError("Expected integer but given {} for `length`".format(type(length)))


try:
    p = PasswordGenerator.generate_password(5, "as")
    print(len(p), p)
except Exception as e:
    print(e.args)
