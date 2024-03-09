from sqlalchemy import Column, String, DateTime, Integer
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp
FORMACION = 4
FINALIZADA = 5
CANCELADA = 6


class FichasModel(Base):

    __tablename__ = 'fichas'

    ficha_id = Column(Integer, primary_key=True, autoincrement=True,
                      nullable=False)

    program_id = Column(Integer, nullable=False)
    number_ficha = Column(Integer, nullable=False)
    alias = Column(String(10), nullable=False)
    status_id = Column(Integer,  nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())

    def __init__(self, data):
        self.program_id = data.get('program_id'),
        self.number_ficha = data.get('number_ficha'),
        self.alias = data.get('alias'),
        self.status_id = data.get('status_id')

    def __repr__(self):
        return {
            'program_id': self.program_id,
            'number_ficha': self.number_ficha,
            'alias': self.alias,
            'status_id': self.status_id
        }
