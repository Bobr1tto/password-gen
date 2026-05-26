import random
import string


def generate_password(length, use_symbols=False):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


print(generate_password(12))
print(generate_password(12, use_symbols=True))
