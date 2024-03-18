from Database.conn import session
from Models.UsersModel import UsersModel
from Models.UsersRolesModel import UserRolesModel, ROOT
from Utils.encryptPassword import PasswordEncrypt
from Utils.JwtToken import JWTtoken
from Models.FunctionsModel import FunctionsModel
from Models.UserPermissionModel import UserPermissionModel


class User:

    def create_new_user(self, data: dict) -> dict:
        user_name = data["user_name"]
        password = data["password"]

        self.validate_user_exist(user_name)

        password_hash = PasswordEncrypt()
        passwordEncrypt = password_hash.encrypt(password)
        data["password"] = passwordEncrypt

        newUser = UsersModel(data)
        session.add(newUser)
        session.commit()
        return {"statusCode": 201, "data": {"message": "Usuario Registrado"}}

    def validate_user_exist(self, user_name):
        validate_user = session.query(UsersModel).filter(
            UsersModel.user_name == user_name
        ).all()

        if validate_user:
            raise AssertionError(
                "Esta persona ya esta registrada en el sistema"
            )

    def get_user_role_id(self, user_id: int) -> int:

        user_data = session.query(UsersModel).filter(
            UsersModel.user_id == user_id,
            UsersModel.active == 1
        ).first()

        # print(f"User data ==> {user_data}")

        user_role_id = 0

        if user_data:
            user_role_id = user_data.user_role_id
            print(f"user_role_id ==> {str(user_role_id)}")

        return user_role_id

    def auth_user(self, data: dict) -> dict:
        user_name = data["user_name"]
        password = data["password"]

        auth_user = session.query(UsersModel).filter(
            UsersModel.user_name == user_name,
            UsersModel.active == 1
        ).first()

        if not auth_user:
            return {
                "statusCode": 404,
                "msg": "No se encontro usuario con este user_name"
            }

        user_auth_id = auth_user.user_id

        print(user_auth_id)

        password_hash = auth_user.password

        # Validacion de contraseña
        password_encrypt = PasswordEncrypt()

        if not password_encrypt.validate(password, password_hash):
            raise AssertionError("Contraseña Incorrecta")

        jwt_token = JWTtoken()
        print(JWTtoken())
        token = jwt_token.encode({
            "user_id": user_auth_id
        })

        return {
            'token': token
        }

    def desactivate_user(self, data: dict) -> dict:

        user_name = data["user_name"]
        print(user_name)

        desactivateUser = session.query(UsersModel).filter(
            UsersModel.user_name == user_name,
            UsersModel.active == 1
        ).first()

        # role = session.query(UsersModel, UserRolesModel
        #                      ).filter(UsersModel.user_role_id
        #                               == UserRolesModel.user_role_id
        #                               ).first()

        if not desactivateUser:
            raise AssertionError(
                "¡ERROR! Al desactivar el usuario"
            )

        else:
            if desactivateUser.user_role_id == ROOT:
                raise AssertionError(
                    "¡ERROR!, Un usuario con rol "
                    f"{desactivateUser.user_role_id} no puede"
                    "ser eliminado"
                )
            desactivateUser.active == 0
            session.commit()

        return {
            "statusCode": "200", "msg": "Ok",
            "data": {
                "msg": "Usuario desactivado"
            }
        }

    def update_User(self, data):
        user_name = data["user_name"]
        password_user = data["password"]

        updateUser = session.query(UsersModel).filter(
            UsersModel.user_name == user_name,
            UsersModel.active == 1
        ).first()

        if not updateUser:
            raise AssertionError(
                "¡ERROR! Usuario no encontrado"
            )
        else:

            updateUser = data
            session.commit()

            PasswordEncript = PasswordEncrypt.encrypt(password_user)
            data["password"] = PasswordEncript

            return {
                "message": "Usuario actualizado correctamente",
                "data": updateUser.__repr__()
            }

    def get_users(self):
        users = session.query(UsersModel).filter(
            UsersModel.active == 1
        ).all()

        data_response = [user.__repr__() for user in users]
        return data_response

    def user_permission_assign(self, data: dict) -> dict:

        user_id = data["users"]
        functions = data["functions"]

        # Get users exists

        validate_user_data = session.query(UsersModel).filter(
            UsersModel.user_id == user_id,
            UsersModel.active == 1
        ).all()

        # Get function exists
        validate_function_data = session.query(FunctionsModel).filter(
            FunctionsModel.function_id.in_(functions),
            FunctionsModel.active == 1
        ).all()

        function_data = []
        for function in validate_function_data:
            function_data.append(function.function_id)

        # permission assingn
        if validate_user_data:
            for function_id in function_data:

                validate_permission = session.query(
                    UserPermissionModel
                ).filter(
                    UserPermissionModel.user_id == user_id,
                    UserPermissionModel.function_id == function_id,
                    UserPermissionModel.active == 1
                ).first()

                if not validate_permission:

                    data_model = {
                        "user_id": user_id,
                        "function_id": function_id
                    }

                    new_user_permission = UserPermissionModel(data_model)
                    session.add(new_user_permission)
                    session.commit()

        return {"statusCode": 201,
                "msg": " Permisos asignados exitosamente."}
