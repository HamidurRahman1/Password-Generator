
import string
from random import *

print(string.punctuation)
print(string.ascii_letters)
print(string.digits)

s = "".join(choice(string.ascii_letters+string.digits+string.punctuation) for x in range(randint(5, 15)))
print(s)
