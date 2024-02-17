
import string
import random

class AbstractPasswordGenerator:
    "Abstraction of password generator."

    def generate_password(length: int):
        pass

class PasswordGenerator(AbstractPasswordGenerator):
    "Implements AbstractPasswordGenerator"

    def generate_password(length: int) -> str:

        allowed_chars = []

        allowed_chars += string.ascii_letters
        allowed_chars += string.digits
        allowed_chars += string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(allowed_chars)

        return password