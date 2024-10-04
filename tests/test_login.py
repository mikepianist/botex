"""
Este módulo contiene una prueba para verificar la funcionalidad de login en Botex.
Obtiene las credenciales de un archivo .env y permite iniciar sesión en la cuenta demo o real.
"""

import os
from dotenv import load_dotenv
from quotexapi.stable_api import Quotex


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Iniciar sesión en Google y Quotex desde las variables de entorno
email_quotex = os.getenv("EMAIL_QUOTEX")
password_quotex = os.getenv("PASSWORD_QUOTEX")
password_app_google = os.getenv("PASSWORD_APP_GOOGLE")
browser_profile_path = os.getenv("BROWSER_PROFILE_PATH")

# Inicializar el cliente de Quotex
client = Quotex(
    email=email_quotex,
    password=password_quotex,
    email_pass=password_app_google,
    user_data_dir=browser_profile_path,
)


def test_login(account_type="demo"):
    """
    Función para iniciar sesión en Quotex.
    Permite cambiar a cuenta demo o real.

    :param account_type: str - Indica el tipo de cuenta ("demo" o "real")
    """
    check, reason = client.connect()
    if check:
        print("Login exitoso.")
        # Cambiar a cuenta demo o real según el parámetro
        if account_type == "real":
            client.change_account("REAL")
            print("Sesión iniciada en cuenta REAL.")
        else:
            client.change_account("PRACTICE")
            print("Sesión iniciada en cuenta DEMO.")
    else:
        print(f"Error al iniciar sesión: {reason}")


if __name__ == "__main__":
    # Llamar a la función y pasar el tipo de cuenta deseada
    test_login(
        account_type="demo"
    )  # Cambia "demo" por "real" si necesitas usar la cuenta real
