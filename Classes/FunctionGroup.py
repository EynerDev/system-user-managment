from Models.FunctionGroupModel import FunctionGroupsModel
from Models.FunctionGroupRelationModel import FunctionGroupRelationModel
from Models.FunctionsModel import FunctionsModel
from Models.FunctionGroupRoleAuthModel import FunctionUserRoleAuthModel
from Classes.UserRoles import UserRoles
from Database.conn import session
from sqlalchemy.orm import aliased


class FunctionGroup:

    def register_function_group(self, data: dict) -> dict:

        name = data["name"]

        print(data)

        self.validate_function_group(name)

        new_function_group = FunctionGroupsModel(data)
        session.add(new_function_group)
        session.commit()

        print(name)

        data_response = {
            "new_function_group": new_function_group.function_group_id,
            "name": new_function_group.name
        }

        return {"statusCode": 201, "data": data_response}

    def get_function_group(self) -> dict:

        result_data = session.query(FunctionGroupsModel).filter(
            FunctionGroupsModel.active == 1
        ).all()

        data = [result.__repr__() for result in result_data]

        return data

    def update_function_group(self, data: dict):

        function_group_id = data["function_group_id"]
        name = data["name"].upper()

        update_function_group = session.query(FunctionGroupsModel).filter(
            FunctionGroupsModel.function_group_id == function_group_id,
            FunctionGroupsModel.active == 1
        ).first()

        if not update_function_group:
            return {"statusCode": 404,
                    "msg": "Este grupo de funciones no existe."}

        if update_function_group.name != name:
            self.validate_function_group(name)

        update_function_group.name = name
        session.commit()

    def desactivate_function_group(self, data: dict):

        function_group_id = data["function_group_id"]

        update_function_group = session.query(FunctionGroupsModel).filter(
            FunctionGroupsModel.function_group_id == function_group_id,
            FunctionGroupsModel.active == 1
        ).first()

        if not update_function_group:
            return {"statusCode": 404,
                    "msg": "Este grupo de funciones no existe."}

        update_function_group.active = 0
        session.commit()

    def validate_function_group(self, name: str):

        validate_function_group_exist = session.query(
            FunctionGroupsModel
        ).filter(
            FunctionGroupsModel.name == name.upper(),
            FunctionGroupsModel.active == 1
        ).first()

        if validate_function_group_exist:
            raise AssertionError(
                "Ya existe una grupo de funciones con este nombre.")

    def register_function_relation(self, data: dict) -> dict:

        funct_group_id = data["function_group_id"]
        functions = data["functions"]

        validate_function_rel = session.query(
            FunctionGroupRelationModel
        ).filter(
            FunctionGroupRelationModel.function_group_id == funct_group_id,
            FunctionGroupRelationModel.function_id.in_(functions),
            FunctionGroupRelationModel.active == 1
        ).all()

        if validate_function_rel:
            raise AssertionError(
                "Existen funciones que ya estan asignada este grupo.")

        for function_id in functions:

            data_model = {
                'function_group_id': funct_group_id,
                'function_id': function_id
            }

            new_relation = FunctionGroupRelationModel(data_model)
            session.add(new_relation)
            session.commit()

        return {"statusCode": 201,
                "msg": "Nuevas funciones asignadas exitosamente"}

    def get_function_relation(self, data: dict) -> dict:

        function_group_id = data["function_group_id"],
        functions = data.get("functions", [])

        funct_relation_model = aliased(FunctionGroupRelationModel)
        function_model = aliased(FunctionsModel)

        condition = [
            funct_relation_model.function_group_id == function_group_id,
            function_model.active == 1,
            funct_relation_model.active == 1
        ]

        if functions:
            condition.append(
                funct_relation_model.function_id.in_(functions)
            )

        function_relation_data = session.query(
            funct_relation_model.function_id, function_model.name
        ).join(
            function_model,
            funct_relation_model.function_id == function_model.function_id
        ).filter(
            *condition
        ).all()

        data_response = []

        for function_id, function_name in function_relation_data:
            data_response.append(
                {
                    "function_id": function_id,
                    "function_name": function_name
                }
            )

        return data_response

    def insert_function_group_auth(self, data: dict):

        function_group_id = data["function_group_id"],
        user_roles = data["user_role_id"]
        print(user_roles)

        validate_function_group = session.query(FunctionGroupsModel).filter(
            FunctionGroupsModel.function_group_id == function_group_id,
            FunctionGroupsModel.active == 1
        ).first()

        if not validate_function_group:
            return {
                "statusCode": 404,
                "msg": "Este grupo de funciones no existe."
            }

        user_role = UserRoles()

        for user_role_id in user_roles:

            if not user_role.validate_user_role(user_role_id):
                continue

            funct_auth_role = aliased(FunctionUserRoleAuthModel)

            validate_function_auth = session.query(funct_auth_role).filter(
                funct_auth_role.function_group_id == function_group_id,
                funct_auth_role.user_role_id == user_role_id,
                funct_auth_role.active == 1
            ).all()

            if not validate_function_auth:

                data_model = {
                    "user_role_id": user_role_id,
                    "function_group_id": function_group_id
                }

                new_function_group_auth = FunctionUserRoleAuthModel(
                    data_model
                )
                session.add(new_function_group_auth)
                session.commit()

        return {"statusCode": 201,
                "msg": "Permisos asignados con exito a los roles."}
