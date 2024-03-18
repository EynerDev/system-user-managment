from Models.UsersRolesModel import UserRolesModel, ROOT
from Database.conn import session


class UserRoles:

    def register_user_role(self, data: dict) -> dict:

        data["role_name"] = data["role_name"].upper()
        self.validate_user_role_name_exists(data["role_name"])

        insert_role = UserRolesModel(data)
        session.add(insert_role)
        session.commit()

        data_response = {
             "user_role_id": insert_role.user_role_id,
             "role_name": insert_role.role_name
        }

        return {"statusCode": 201, "msg": data_response}
    

    def get_user_roles(self, data) -> list:

        management_user_id = data.get("user_id", 0)

        condition = [
            UserRolesModel.active == 1
        ]

        if management_user_id != ROOT:
            condition.append(
                UserRolesModel.user_role_id != ROOT
            )

        result_data = session.query(UserRolesModel).filter(
            *condition
        ).order_by(UserRolesModel.user_role_id.asc()).all()

        data = [result.__repr__() for result in result_data]

        return data

    def update_user_role(self, data: dict):

        user_role_id = data["user_role_id"]
        role_name = data["role_name"].upper()

        user_rol_update = session.query(UserRolesModel).filter(
            UserRolesModel.user_role_id == user_role_id,
            UserRolesModel.active == 1
        ).first()

        status_code = 200
        msg = "Ok"

        if not user_rol_update:
            status_code = 404
            msg = "No se encontro un rol con esta user_role_id"
        else:
            if user_role_id == ROOT:
                raise AssertionError(
                    "Este rol de usuario no se puede editable.")

            if user_rol_update.role_name != role_name:
                self.validate_user_role_name_exists(role_name)

            user_rol_update.role_name = role_name
            session.commit()

        return {"statusCode": status_code, "msg": msg}

    def desactivate_user_role(self, data):

        user_role_id = data["user_role_id"]

        user_rol_delete = session.query(UserRolesModel).filter(
            UserRolesModel.user_role_id == user_role_id,
            UserRolesModel.active == 1
        ).first()

        status_code = 200
        msg = "Ok"

        if not user_rol_delete:
            status_code = 404
            msg = "No se encontro un rol con esta user_role_id"
        else:
            if user_role_id == ROOT:
                raise AssertionError(
                    "Este rol de usuario no puede ser modificado.")

            user_rol_delete.active = 0
            session.commit()

        return {"statusCode": status_code, "msg": msg}

    def validate_user_role_name_exists(self, role_name: str):

        result_validate = session.query(UserRolesModel).filter(
            UserRolesModel.role_name == role_name,
            UserRolesModel.active == 1
        ).all()

        if result_validate:
            raise AssertionError("Ya existe un rol con este nombre.")

    def validate_user_role(self, user_role_id: int) -> bool:

        result = session.query(UserRolesModel).filter(
            UserRolesModel.user_role_id == user_role_id,
            UserRolesModel.active == 1
        ).first()

        validate = False

        if result:
            validate = True

        return validate
