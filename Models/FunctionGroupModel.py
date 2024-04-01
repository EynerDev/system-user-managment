from sqlalchemy import Column, String, DateTime, Integer
from Database.conn import Base

FUNCTIONS_ROUTE = 1
FUNCTIONS_ADMIN = 2
FUNCTIONS_INSTRUCTOR = 3
FUNCTIONS_APRENDIZ = 4


class FunctionGroupsModel(Base):

    __tablename__ = 'function_groups'

    function_group_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')
    updated_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')

    def __init__(self, data):
        self.name = data.get("name").upper()

    def __repr__(self):
        return {
            'function_group_id': self.function_group_id,
            'name': self.name,
        }
