from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base


class FunctionUserRoleAuthModel(Base):

    __tablename__ = 'functions_group_auth_role'

    function_auth_role_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True)
    user_role_id = Column(Integer, nullable=False)
    function_group_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')
    updated_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')

    def __init__(self, data):
        self.user_role_id = data.get('user_role_id')
        self.function_group_id = data.get('function_group_id')

    def __repr__(self):
        return {
            'function_auth_role_id': self.function_auth_role_id,
            'user_role_id': self.user_role_id,
            'function_group_id': self.function_group_id,
        }
