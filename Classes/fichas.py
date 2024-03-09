from Models.fichasModel import FichasModel, FORMACION, FINALIZADA, CANCELADA
from Models.ProgramasModel import ProgramsModel
from Database.conn import session
from Models.SubItemsModel import SubItemsModel
from Models.UsersModel import UsersModel
from Models.Assign_ficha_instructorModel import assign_ficha_instructor


class Fichas:
    def register_ficha(self, data: dict) -> dict:
        program_id = data["program_id"]
        number_ficha = data["number_ficha"]

        self.validate_ficha_exist(number_ficha)
        self.validate_program_exist(program_id)

        new_ficha = FichasModel(data)
        session.add(new_ficha)
        session.commit()

        return {"statusCode": 201, "data": {"msg": "Ficha Registrada"}}

    def validate_ficha_exist(self, number_ficha):

        validate_ficha = session.query(FichasModel).filter(
            FichasModel.number_ficha == number_ficha,
            FichasModel.active == 1
        ).all()

        if validate_ficha:
            raise AssertionError("Ya se encuentra una ficha registrada con ese"
                                 "numero de ficha")

    def validate_program_exist(self, program_id: int):
        validate_program = session.query(ProgramsModel).filter(
            ProgramsModel.program_id == program_id,
            ProgramsModel.active == 1
        ).all()

        if not validate_program:
            raise AssertionError("No se encuentra registrado un program con"
                                 "este program_id")

    def get_fichas(self):
        fichas = session.query(FichasModel).filter(
            FichasModel.active == 1
        ).all()

        data_response = [ficha.__repr__() for ficha in fichas]
        return data_response

    def get_status(self):
        get_status = session.query(SubItemsModel).filter(
            SubItemsModel.item_id == 2
        ).all()

        data_response = [item.__repr__() for item in get_status]
        return data_response

    def desactivate_ficha(self, data: dict) -> dict:
        number_ficha = data["number_ficha"]

        desactivateFicha = session.query(FichasModel).filter(
            FichasModel.number_ficha == number_ficha
        ).first()

        if desactivateFicha:
            desactivateFicha.active = 0
            session.commit()

        return {
            "msg": "Ficha Desactivada"
        }

    def change_status_ficha(self, data: dict) -> dict:
        number_ficha = data["number_ficha"]
        status = data["status_id"]

        change_status = session.query(FichasModel).filter(
            FichasModel.number_ficha == number_ficha,
            FichasModel.active == 1
        ).all()

        if status in [FORMACION, FINALIZADA, CANCELADA]:
            change_status.status_id == status
            session.commit()

        else:
            raise AssertionError("¡ERROR! status_id no valido")

        print(status)

    def assign_ficha(self, data):

        instructor_id = data["instructor_id"]
        ficha_id = data["ficha_id"]

        self.validate_ficha_assign(instructor_id, ficha_id)

        new_ficha_assign = assign_ficha_instructor(data)
        session.add(new_ficha_assign)
        session.commit()

    def validate_ficha_assign(self, instructor_id, ficha_id):
        validate_ficha_assig = session.query(assign_ficha_instructor).filter(
            assign_ficha_instructor.instructor_id == instructor_id,
            assign_ficha_instructor.ficha_id == ficha_id,
            assign_ficha_instructor.active == 1
        ).all()

        if validate_ficha_assig:
            raise AssertionError("¡Error! Ya esta asignada esta ficha"
                                 "a este instructor")

    # def get_fichas_asigned_instructor(seld, instructor_id):

    #     fichas = aliased(FichasModel)
    #     fichas_assigned  = aliased(assign_ficha_instructor)
    #     insgtructor = aliased

    #      condition = [
    #          fichas_assigned.instructor_id == instructor_id
    #          fichas.active == 1,
    #          instructor.active == 1
    #      ]

    #     assigned_fichas_instructor = session.query(assign_ficha_instructor
    #                                                ).
    #         filter(
    #                assign_ficha_instructor.instructor_id == instructor_id,
    #                assign_ficha_instructor.active == 1
    #     )
    #         fichas_instructores = session.query(Ficha).join(fichas_assigned
    #                                                         , Instructor.id == Ficha.instructor_id).all()
    #     data_response =
    #     # funct_relation_model = aliased(FunctionGroupRelationModel)
    #     # function_model = aliased(FunctionsModel)

    #     # condition = [
    #     #     funct_relation_model.function_group_id == function_group_id,
    #     #     function_model.active == 1,
    #     #     funct_relation_model.active == 1
    #     # ]

    #     # if functions:
    #     #     condition.append(
    #     #         funct_relation_model.function_id.in_(functions)
    #     #     )

    #     # function_relation_data = session.query(
    #     #     funct_relation_model.function_id, function_model.name
    #     # ).join(
    #     #     function_model,
    #     #     funct_relation_model.function_id == function_model.function_id
    #     # ).filter(
    #     #     *condition
    #     # ).all()

    #     # data_response = []

    #     # for function_id, function_name in function_relation_data:
    #     #     data_response.append(
    #     #         {
    #     #             "function_id": function_id,
    #     #             "function_name": function_name
    #     #         }
    #     #     )

    #     # return data_response
