# Generator Passwords

import random
import string

def gen_password(length=6, use_uppercase=True, use_digits=True, use_special=True):
    """
    Genera una contraseña segura con la longitud especificada.

    :param length: Longitud de la contraseña.
    :param use_uppercase: Incluir letras mayúsculas (default: True).
    :param use_digits: Incluir dígitos (default: True).
    :param use_special: Incluir caracteres especiales (default: True).
    :return: Contraseña generada.
    """
    
# Conjunt of base caracters: lower words
characters = string.ascii_lowercase

# Conjunt of base caracters: up words
if use_uppercase:
    characters += string.ascii_uppercase
    
# Add digits for this necesary
if use_digits:
    characters += string.digits

# Add special caracters for this necesary
if use_special:
    characters += string.punctuation
    
# the password has a minimun 1 character
if length < 6:
    raise ValueError(" La longitud de la contrasela debe de ser de al menos 6 dígitos ")

# Generate the password
password = ''.join(random.choice(characters) for i in range(length))
return password

# Example of use
if __name__ == "__genPass__":
    #longitud de la contraseña
    password_length = 6

# Generate to the password
password = gen_password(password_length)
print(f"La contraseña generada es: {password}")
