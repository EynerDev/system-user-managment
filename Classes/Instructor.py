from Database.conn import session
from Models.InstructorModel import InstructorModel
from Classes.fichas import Fichas
from Models.UsersModel import UsersModel


class Instructor:

    fichas = Fichas()

    def register_instructor(self, data):

        user_id = data["user_id"]
        ficha_id = data["ficha_id"]

        self.validate_user_id_exist(user_id)
        self.validate_ficha_exist(ficha_id)

        newInstructor = InstructorModel(data)
        session.add(newInstructor)
        session.commit()

    def validate_user_id_exist(self, user_id):
        validate_user = session.query(UsersModel).filter(
            UsersModel.user_id == user_id,
            UsersModel.active == 1

        ).all()

        if not validate_user:
            raise AssertionError("Este usuario no se encuentra registrado")

    def get_instructor(self):
        get_instructor = session.query(InstructorModel).filter(
            InstructorModel.active == 1
        ).all()

        data_response = [Instructor.__repr__()
                         for instructor in get_instructor]
        return data_response

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
            
    
