from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class UserPermissionModel(Base):

    __tablename__ = 'user_permission'

    user_permission_id = Column(Integer, autoincrement=True, nullable=False,
                                primary_key=True)
    user_id = Column(Integer, nullable=False)
    function_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')
    updated_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')

    def __init__(self, data):
        self.user_id = data.get('user_id')
        self.function_id = data.get('function_id')

    def __repr__(self):
        return {
            'user_permission_id': self.user_permission_id,
            'user_id': self.user_id,
            'function_id': self.function_id,
        }
