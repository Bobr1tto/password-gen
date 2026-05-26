import random
import string


def generate_password(length):
    chars = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


print(generate_password(12))
