import random
import string


def generate_password(length, uppercase, lowercase, numbers, special):
    # Define the character sets for each type of character

    uppercase_chars = string.ascii_uppercase if uppercase else ""
    lowercase_chars = string.ascii_lowercase if lowercase else ""
    number_chars = string.digits if numbers else ""
    special_chars = string.punctuation if special else ""

    possible_chars = uppercase_chars + lowercase_chars + number_chars + special_chars

    length = max(length, 8)

    # Generate the password
    password = "".join(random.choice(possible_chars) for i in range(length))

    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

    return password


password = generate_password(
    length=12, uppercase=True, lowercase=True, numbers=True, special=True
)
print(password)
