import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    """Generates a random password with the specified length and character types."""

    character_pool = []
    if include_uppercase:
        character_pool.extend(string.ascii_uppercase)
    if include_lowercase:
        character_pool.extend(string.ascii_lowercase)
    if include_digits:
        character_pool.extend(string.digits)
    if include_symbols:
        character_pool.extend(string.punctuation)

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=16, include_symbols=False)  # Generate a 16-character password without symbols
print(password)
