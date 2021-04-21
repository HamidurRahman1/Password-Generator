
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

        if length >= MIN_LENGTH:
            return "".join(choice(from_string) for x in range(randint(length, length)))
        else:
            return "".join(choice(from_string) for x in range(randint(MIN_LENGTH, MIN_LENGTH)))

    @staticmethod
    def generate_password(length=MIN_LENGTH, source=CHARS, unique_source=False):

        try:
            length = int(length)
            if isinstance(source, str) and unique_source:
                source = str(set(source))
                return PasswordGenerator.__generate_password(length, source)
            elif isinstance(source, str) and not unique_source:
                return PasswordGenerator.__generate_password(length, source)
            elif isinstance(source, set):
                return PasswordGenerator.__generate_password(length, str(source))
        except ValueError:
            raise ValueError("Expected integer but given {} for `length`".format(type(length)))


try:
    p = PasswordGenerator.generate_password(7, {"d"})
    print(p)
except Exception as e:
    print(e.args)
