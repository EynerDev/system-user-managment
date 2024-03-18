from Models.fichasModel import FichasModel, FORMACION, FINALIZADA, CANCELADA
from Models.ProgramasModel import ProgramsModel
from Database.conn import session
from Models.SubItemsModel import SubItemsModel
from Models.Assign_ficha_instructorModel import assign_ficha_instructor
# from Models.InstructorModel import InstructorModel


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
            raise AssertionError("No se encuentra registrado un programa con"
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

    

    