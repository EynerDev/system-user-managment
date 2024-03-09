import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv()


class JWTtoken:

    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY_JWT")

    def encode(self, data: dict) -> str:

        payload = {
            **data,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, self.secret_key, algorithm='HS256')

        return token

    def decode(self, token: str) -> dict:

        try:

            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload

        except jwt.ExpiredSignatureError:
            raise AssertionError(
                "Token expirado. Por favor, inicia sesión nuevamente.")
        except jwt.InvalidTokenError:
            raise AssertionError("El token ingresado no es valido.")
