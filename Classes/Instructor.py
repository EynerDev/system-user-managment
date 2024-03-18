from Database.conn import session
from Models.InstructorModel import InstructorModel
from Classes.fichas import Fichas
from Models.UsersModel import UsersModel
from Models.UsersRolesModel import INSTRUCTOR
from Models.Assign_ficha_instructorModel import assign_ficha_instructor
from Models.fichasModel import FichasModel


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

        return {
            "status_code": 200,
            "msg": "Instructor registrado con exito"
        }

    def get_instructor(self):

        valid_user_register_instructor = session.query(UsersModel).filter(
            UsersModel.user_role_id == INSTRUCTOR,
            UsersModel.active == 1
        ).first()

        if valid_user_register_instructor:
            for Instructor in valid_user_register_instructor:
                return {
                    "statusCode": 200,
                    "user_id":  valid_user_register_instructor.user_id,
                    "first_name": valid_user_register_instructor.first_name,
                    "last_name": valid_user_register_instructor.last_name,
                    "email": valid_user_register_instructor.email

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
                    f"¡ERROR! la ficha con ficha_id ={ficha_id} no existe"
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

    # def validate_ficha_assign(self, instructor_id, fichas_id):
    #     validate_ficha_assig = session.query(assign_ficha_instructor).filter(
    #         assign_ficha_instructor.instructor_id == instructor_id,
    #         FichasModel.ficha_id.in_(fichas_id),
    #         assign_ficha_instructor.active == 1
    #     ).all()

    #     if validate_ficha_assig:
    #         raise AssertionError("¡Error! Ya esta asignada esta ficha"
    #                              "a este instructor")

    def get_fichas_asigned_instructor(self, data):

        instructor_id = data["instructor_id"]

        instructor_exist = self.validate_instructor_exist(instructor_id)

        if instructor_exist:
            fichas_asignadas = session.query(assign_ficha_instructor).filter(
                assign_ficha_instructor.instructor_id == instructor_id
            ).all()

            instructor_name = session.query(UsersModel).filter(
                UsersModel.user_id == instructor_exist.user_id
            ).first()

            name_instructor = f"{instructor_name.first_name} {
                instructor_name.last_name}"

            nombres_fichas_asignadas = []

            for asignacion in fichas_asignadas:
                ficha = session.query(FichasModel).filter(
                    FichasModel.ficha_id == asignacion.ficha_id
                ).first()

                if ficha:
                    nombres_fichas_asignadas.append(ficha.alias)

            return {
                "statusCode": 200,
                "msg": {
                    "Instructor_name": name_instructor,
                    "email": instructor_name.email,
                    "fichas": nombres_fichas_asignadas
                }}
        else:
            return {
                "statusCode": 404,
                "msg": "¡ERROR! Instructor no encontrado"
            }
