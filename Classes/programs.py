from Database.conn import session
from Models.ProgramasModel import ProgramsModel


class Programs:

    def register_program(self, data: dict) -> dict:
        program_name = data["name_program"].upper()

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
