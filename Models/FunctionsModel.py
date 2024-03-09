
from sqlalchemy import Column, DateTime, Integer, Text
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class FunctionsModel(Base):
    __tablename__ = "functions"

    function_id = Column(Integer, autoincrement=True, primary_key=True,
                         nullable=False)
    name = Column(Text, nullable=False)
    path = Column(Text, nullable=False)
    method = Column(Text, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())

    def __init__(self, data):
        self.name = data.get('name').upper()
        self.path = data.get('path')
        self.method = data.get('method').upper()

    def __repr__(self):
        return {
            'function_id': self.function_id,
            'name': self.name,
            'path': self.path,
            'method': self.method
        }
