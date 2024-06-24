# Generator of passwords

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
    # Conjunto de caracteres base: letras minúsculas
    characters = string.ascii_lowercase

    # Conjunto de caracteres base: letras mayúsculas
    if use_uppercase:
        characters += string.ascii_uppercase

    # Agregar dígitos si es necesario
    if use_digits:
        characters += string.digits

    # Agregar caracteres especiales si es necesario
    if use_special:
        characters += string.punctuation

    # La contraseña debe tener al menos 6 caracteres
    if length < 6:
        raise ValueError("La longitud de la contraseña debe ser de al menos 6 caracteres")

    # Generar la contraseña
    password = ''.join(random.choice(characters) for i in range(length))
    return password  # <-- Este return ahora está correctamente indentado dentro de la función

    # Ejemplo de uso
if __name__ == "__main__":
    # Longitud de la contraseña
    password_length = 6

    # Generar la contraseña
    password = gen_password(password_length)
print(f"La contraseña generada es: {password}")
