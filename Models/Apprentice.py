from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class ApprenticeModel(Base):

    __tablename__ = 'apprentice'

    apprentice_id = Column(Integer, primary_key=True, autoincrement=True,
                           nullable=False)
    user_id = Column(Integer, nullable=False)
    ficha_id = Column(Integer, nullable=False)
    state_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=current_timestamp())

    def __init__(self, data):
        self.id_person = data.get('user_id')
        self.id_ficha = data.get('ficha_id')
        self.state_id = data.get('state_id')

    def __repr__(self):
        return {
            'user': self.user_id,
            'ficha': self.ficha_id,
            'state': self.state_id
        }
