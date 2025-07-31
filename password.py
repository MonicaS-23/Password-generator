import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    # Create a pool of characters based on user preferences
    char_pool = ""
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation
    
    # Check if the pool has any characters
    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password by picking characters from the pool
    password = ''.join(random.choice(char_pool) for _
