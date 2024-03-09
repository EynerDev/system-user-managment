from werkzeug.security import generate_password_hash, check_password_hash


class PasswordEncrypt:

    def encrypt(self, password_user):
        return generate_password_hash(str(password_user))

    def validate(self, password_user, passwordEncrypt):
        return check_password_hash(passwordEncrypt, str(password_user))
