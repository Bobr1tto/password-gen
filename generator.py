import random
import string


def generate_password(length, use_symbols=False):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


print(generate_password(12))
print(generate_password(12, use_symbols=True))
