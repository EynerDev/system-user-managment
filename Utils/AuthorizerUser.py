from Classes.Users import User
from Classes.Function import Function
from Models.UsersRolesModel import ROOT, INSTRUCTOR, APRENDIZ
from Models.UserPermissionModel import UserPermissionModel
from Models.FunctionGroupRoleAuthModel import FunctionUserRoleAuthModel
from Models.FunctionGroupRelationModel import FunctionGroupRelationModel
from Database.conn import session
from sqlalchemy.orm import aliased
from sqlalchemy import and_


class AuthorizerUser:

    def validate_auth(self, data: dict):

        # El código recupera los valores de "user_id", "path" y "méthod" del
        # diccionario de "data".
        user_id = data["user_id"]
        path = data["path"]
        method = data["method"].upper()
        print(f"path: {path} - method : {method}")

        # Las líneas `usuario = Usuario()` y `función = Función()` están
        # creando instancias de las clases `Usuario` y `Función`,
        # respectivamente.
        user = User()
        function = Function()

        # Creamos una variable user_role_id para capturar el rol del usuario
        # que esta logueado
        user_role_id = user.get_user_role_id(user_id)

        # Validamos el valor de user_role_id, si este es igual a 0 devolvemos
        # un mensaje de error
        if user_role_id == 0:
            raise AssertionError(
                "Hubo un problema con esta funcionalidad con este usuario.")

        # # Validamos si el usuario tiene un rol "ROOT"
        # if user_role_id == ROOT:
        #     return True

        # Creamos una variable function_data en la que vamos a capturar el
        # "function_id", a traves del path y el method
        function_data = function.get_function_id(
            path, method
        )

        function_id = function_data["function_id"]
        function_active = function_data["active"]

        # print(f"function_active ==>{function_active}")

        # print(str(function_id, function_active))

        # Validamos si el rol del usuario es "INSTRUCTOR" o "APRENDIZ" e
        # Imprimimos el valor de validate_user_role
        validate_user_role = user_role_id in [INSTRUCTOR, APRENDIZ]
        print(f"validate_user_role ==>{str(validate_user_role)}")

        if function_active == 0 and not validate_user_role:
            raise AssertionError(
                "Esta funcionalidad no se encuentra disponible"
                "por el momemto")

        # Validamos si el usuario tiene algun permiso especial a esta function
        validate_permission = self.validate_user_permission(
            user_id, function_id
        )
        # Imprimimos el valor de validate_permission
        print(f"valisate_permission {str(validate_permission)}")

        if validate_permission:
            return True

        # Validamos si el usuario tiene permiso para ejecutar esta function
        validate_group_role = self.validate_group_role_auth(
            user_role_id, function_id
        )
        # print(str(user_role_id, function_id))

        # print(str(validate_group_role))

        if not validate_group_role:
            raise AssertionError("No tiene acceso a esta funcionalidad.")

        return True

    def validate_user_permission(self, user_id: int, function_id: int) -> bool:

        # El código utiliza el método de consulta de SQLAlchemy para recuperar
        # un objeto UserPermissionModel de la base de datos. Filtra la consulta
        # según los campos user_id, function_id y activo de la tabla
        # UserPermissionModel. El método `.first()` se utiliza para recuperar
        # solo el primer resultado de la consulta. Luego, el resultado se
        # asigna a la variable `validate_user_permission`.
        validate_user_permission = session.query(UserPermissionModel).filter(
            UserPermissionModel.user_id == user_id,
            UserPermissionModel.function_id == function_id,
            UserPermissionModel.active == 1
        ).first()

        validate = False

        if validate_user_permission:
            validate = True

        return validate

    def validate_group_role_auth(self, user_role_id: int,
                                 function_id: int) -> bool:

        auth = aliased(FunctionUserRoleAuthModel)
        relation = aliased(FunctionGroupRelationModel)

        validate_group_role = session.query(
            auth
        ).join(
            relation, and_(
                relation.function_group_id == auth.function_group_id,
                relation.active == 1
            )
        ).filter(
            auth.user_role_id == user_role_id,
            relation.function_id == function_id,
            auth.active == 1
        ).first()

        # print(str(validate_group_role))

        validate = False

        if validate_group_role:
            validate = True

        return validate
