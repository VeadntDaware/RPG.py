import random
import string

def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Usage example
password_length = 10
random_password = generate_password(password_length)
print("Random Password:", random_password)
