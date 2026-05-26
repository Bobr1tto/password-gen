import random
import string


def generate_password(length, use_symbols=False):
    if length < 4 or length > 128:
        raise ValueError("Длина пароля должна быть от 4 до 128 символов")
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password


<<<<<<< HEAD
print(generate_password(16))
print(generate_password(16, use_symbols=True))
=======
print(generate_password(8))
print(generate_password(8, use_symbols=True))
>>>>>>> b606e7523d5fb80d0e868ee4426c550bd58346b9
