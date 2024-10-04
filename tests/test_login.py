# test_login.py
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el email y la contraseña desde las variables de entorno
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


# Aquí podrías utilizar las variables para la lógica de login
def test_login():
    print(f"Email: {email}")
    print(f"Password: {password}")
    # Lógica para iniciar sesión con email y contraseña...


if __name__ == "__main__":
    test_login()
