"""
Este módulo contiene una prueba para verificar la funcionalidad de login en Botex.
Obtiene las credenciales de un archivo .env y las imprime para realizar el test.
"""

import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el email y la contraseña desde las variables de entorno
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


# Aquí podrías utilizar las variables para la lógica de login
def test_login():
    """
    Función de prueba para simular un login.
    Obtiene las credenciales desde el archivo .env y las imprime.
    """
    print(f"Email: {email}")
    print(f"Password: {password}")
    # Lógica para iniciar sesión con email y contraseña...


if __name__ == "__main__":
    test_login()
