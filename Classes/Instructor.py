from Database.conn import session
from Models.InstructorModel import InstructorModel
from Classes.fichas import Fichas
from Models.UsersModel import UsersModel
from Models.UsersRolesModel import INSTRUCTOR
from Models.Assign_ficha_instructorModel import assign_ficha_instructor
from Models.fichasModel import FichasModel
from Models.ProgramasModel import ProgramsModel
from Models.SubItemsModel import SubItemsModel


class Instructor:

    fichas = Fichas()

    def register_instructor(self, data):

        user_id = data["user_id"]

        validate_rol_instructor = session.query(UsersModel).filter(
            UsersModel.user_id == user_id,
            UsersModel.active == 1
        ).first()

        if validate_rol_instructor.user_role_id != INSTRUCTOR:
            raise AssertionError(
                "¡ERROR!, El Rol de este usuario no coincide con el de"
                " instructor"
            )

        newInstructor = InstructorModel(data)
        session.add(newInstructor)
        session.commit()

        name = f"{validate_rol_instructor.first_name} {
            validate_rol_instructor.last_name}"
        return {
            "status_code": 200,
            "msg": "Instructor registrado con exito",
            "data": {
                "name": name,
                "email": validate_rol_instructor.email,
                "number_phone": validate_rol_instructor.number
            }
        }

    def get_instructor(self):
        valid_users_register_instructor = session.query(UsersModel).filter(
            UsersModel.user_role_id == INSTRUCTOR,
            UsersModel.active == 1
        ).all()

        instructors_data = []
        for valid_user_register_instructor in valid_users_register_instructor:

            name_instructor = f"{valid_user_register_instructor.first_name} {
                valid_user_register_instructor.last_name}"

            instructors_data.append({
                "user_id": valid_user_register_instructor.user_id,
                "name_instructor": name_instructor,
                "email": valid_user_register_instructor.email
            })

        return {
            "statusCode": 200,
            "msg": instructors_data
        }

    def desactivate_instructor(self, data):
        Instructor_id = data["instructor_id"]

        desactivate_instructor = session.query(InstructorModel).filter(
            InstructorModel.instructor_id == Instructor_id
        ).all()

        if desactivate_instructor:
            InstructorModel.instructor_id = 0
            session.commit()

            return {
                "msg": "Instructor Desactivado"
            }

    def validate_instructor_exist(self, instructor_id):

        validate_instructor_exit = session.query(InstructorModel).filter(
            InstructorModel.instructor_id == instructor_id,
            InstructorModel.active == 1
        ).first()

        if validate_instructor_exit:
            return validate_instructor_exit

    def assign_ficha(self, data):

        instructor_id = data["instructor_id"]
        fichas_id = data["fichas_id"]

        validate_ficha_assig = session.query(assign_ficha_instructor).filter(
            assign_ficha_instructor.instructor_id == instructor_id,
            assign_ficha_instructor.ficha_id.in_(fichas_id),
            assign_ficha_instructor.active == 1
        ).all()

        if validate_ficha_assig:
            raise AssertionError("¡Error! Ya esta asignada esta ficha "
                                 "a este instructor")
        for ficha_id in fichas_id:

            valid_ficha_exist = session.query(FichasModel).filter(
                FichasModel.ficha_id == ficha_id,
                FichasModel.active == 1
            ).first()

            if not valid_ficha_exist:
                raise AssertionError(
                    f"¡ERROR! la ficha con ficha_id = {ficha_id} no existe "
                    " en la base de datos")

            data_model = {
                'instructor_id': instructor_id,
                'ficha_id': ficha_id
            }

            new_ficha_assign = assign_ficha_instructor(data_model)
            session.add(new_ficha_assign)
            session.commit()

        return {
            "statusCode": 200,
            "msg": "Fichas asignadas de manera exitosa"
        }

    def get_fichas_asigned_instructor(self, data):

        instructor_id = data["instructor_id"]

        instructor_exist = self.validate_instructor_exist(instructor_id)

        if instructor_exist:
            # Realizar un JOIN para obtener directamente la información
            # necesaria de las fichas asignadas
            fichas_asignadas = session.query(
                assign_ficha_instructor, FichasModel, ProgramsModel,
                SubItemsModel)\
                .join(FichasModel,
                      assign_ficha_instructor.ficha_id == FichasModel.ficha_id
                      )\
                .join(ProgramsModel,
                      FichasModel.program_id == ProgramsModel.program_id)\
                .join(SubItemsModel,
                      FichasModel.status_id == SubItemsModel.sub_items_id)\
                .filter(assign_ficha_instructor.instructor_id
                        == instructor_id, ProgramsModel.active == 1)\
                .all()

            instructor_data = session.query(UsersModel).filter(
                UsersModel.user_id == instructor_exist.user_id).first()

            name_instructor = f"{instructor_data.first_name} {
                instructor_data.last_name}"

            nombres_fichas_asignadas = []

            for asignacion, ficha, program, status_ficha in fichas_asignadas:
                nombres_fichas_asignadas.append({
                    "Alias": ficha.alias,
                    "Programa": program.name_program,
                    "Numero de ficha": ficha.number_ficha,
                    "estado_ficha": status_ficha.description
                })

            return {
                "statusCode": 200,
                "msg": {
                    "Instructor_name": name_instructor,
                    "email": instructor_data.email,
                    "fichas": nombres_fichas_asignadas
                }
            }
        else:
            return {
                "statusCode": 404,
                "msg": "¡ERROR! Instructor no encontrado"
            }
