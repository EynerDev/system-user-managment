from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base


class FunctionGroupRelationModel(Base):

    __tablename__ = 'function_group_relation'

    function_group_relation_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True)
    function_group_id = Column(Integer, nullable=False)
    function_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')
    updated_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP',
                        onupdate='CURRENT_TIMESTAMP')

    def __init__(self, data):
        self.function_group_id = data.get('function_group_id')
        self.function_id = data.get('function_id')

    def __repr__(self):
        return {
            'function_group_relation_id': self.function_group_relation_id,
            'function_group_id': self.function_group_id,
            'function_id': self.function_id
        }
