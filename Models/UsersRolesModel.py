from sqlalchemy import Column, String, DateTime, Integer
from Database.conn import Base

ROOT = 1
INSTRUCTOR = 2
APRENDIZ = 3


class UserRolesModel(Base):

    __tablename__ = 'users_roles'

    user_role_id = Column(Integer, nullable=False,
                          primary_key=True, autoincrement=True)
    role_name = Column(String(255), nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')
    updated_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')

    def __init__(self, data):
        self.role_name = data.get('role_name').upper()

    def __repr__(self):
        return {
            'user_role_id': self.user_role_id,
            'role_name': self.role_name,
        }
