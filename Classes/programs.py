from Database.conn import session
from Models.ProgramasModel import ProgramsModel
from Models.fichasModel import FichasModel, FORMACION


class Programs:

    def register_program(self, data: dict) -> dict:
        program_name = data["name_program"]

        validate_name_program_exist = session.query(ProgramsModel).filter(
            ProgramsModel.name_program == program_name,
            ProgramsModel.active == 1
        ).all()

        if validate_name_program_exist:
            raise AssertionError(
                "!ERROR¡ Este programa ya existe en el sistema"
            )
        else:

            newProgram = ProgramsModel(data)
            session.add(newProgram)
            session.commit()

            return {
                "statusCode": 201,
                "msg": "Programa Registrado Exitosamente"
            }

    def get_programs(self):

        get_programs = session.query(ProgramsModel).filter(
            ProgramsModel.active == 1
        ).all()

        data_response = [program.__repr__() for program in get_programs]
        return data_response

    def desactivate_program(self, data: dict) -> dict:
        program_id = data["program_id"]

        validate_program_id = session.query(ProgramsModel).filter(
            ProgramsModel.program_id == program_id,
            ProgramsModel.active == 1
        ).first()

        if not validate_program_id:
            raise AssertionError(
                "!ERROR¡ No existe programa registrado con este program_id")

        validate_status_program = session.query(FichasModel).filter(
            FichasModel.program_id == program_id,
            FichasModel.active == 1,
            FichasModel.status_id == FORMACION
        ).first()

        if validate_status_program:
            raise AssertionError(
                "!ERROR¡ No puedes desactivar un programa que tenga una ficha"
                " en estado de Formación")

        # Desactivar el programa
        validate_program_id.active = 0
        session.commit()

        return {
            "statusCode": 200,
            "msg": "Programa Desactivado Exitosamente"
        }
