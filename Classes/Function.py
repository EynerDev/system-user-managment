from Models.FunctionsModel import FunctionsModel
from Database.conn import session


class Function:

    def register_function(self, data: dict) -> dict:

        path = data["function_path"]
        method = data["function_method"]

        self.validate_function_exists(path, method)

        data_model = {
            "name": data["name"].upper(),
            "path": path,
            "method": method.upper()
        }

        new_function = FunctionsModel(data_model)
        session.add(new_function)
        session.commit()

        data_response = {
            "function_id": new_function.function_id,
            **data_model
        }

        return {"statusCode": 201, "data": data_response}

    def get_functions(self):
        result_data = session.query(FunctionsModel).filter(
            FunctionsModel.active == 1
        ).all()

        data_response = [result.__repr__() for result in result_data]

        return data_response

    def update_function(self, data: dict):

        function_id = data["function_id"]
        name = data["name"].upper()
        path = data["path"]
        method = data["method"].upper()

        update_function = session.query(FunctionsModel).filter(
            FunctionsModel.function_id == function_id,
            FunctionsModel.active == 1
        ).first()

        if not update_function:
            return {"statusCode": 404,
                    "msg": "No se encontro esta funcion."}

        if update_function.path != path or update_function.method != method:
            self.validate_function_exists(path, method)

        update_function.name = name
        update_function.path = path
        update_function.method = method
        session.commit()

    def desactivate_function(self, data: dict):

        function_id = data["function_id"]

        update_function = session.query(FunctionsModel).filter(
            FunctionsModel.function_id == function_id,
            FunctionsModel.active == 1
        ).first()

        if not update_function:
            return {"statusCode": 404,
                    "msg": "No se encontro esta funcion."}

        update_function.active = 0
        session.commit()

    def validate_function_exists(self, path: str, method: str):

        print(path)
        print(method)

        validate_function_data = session.query(FunctionsModel).filter(
            FunctionsModel.path == path,
            FunctionsModel.method == method.upper(),
            FunctionsModel.active == 1
        ).all()

        if validate_function_data:
            raise AssertionError(
                "Ya existe una funcion con este PATH y este metodo.")

    def get_function_id(self, path: str, method: str):

        function_data = session.query(FunctionsModel).filter(
            FunctionsModel.path == path,
            FunctionsModel.method == method.upper(),
            FunctionsModel.active == 1
        ).first()

        if not function_data:
            raise AssertionError(
                "Esta funcionalidad no existe dentro del sistemas.")

        print(f"function_name ==>{function_data.name}")
        print(f"function_id ==> {function_data.function_id}")

        data_response = {
            "function_id": function_data.function_id,
            "active": function_data.active
        }

        return data_response
