from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class AttendanceModel(Base):
    
    __tablename__ = 'attendance'
    
    id_apre_asis = Column(Integer, primary_key=True, autoincrement=True,
                          nullable=False)
    id_apren = Column(Integer, nullable=False)
    ficha = Column(Integer, nullable=False)
    state_asis = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=current_timestamp())

    def ___init__(self, data):
        self.id_apren = data.get('id_aprendiz'),
        self.ficha = data.get('ficha'),
        self.state_asis = data.get('state_asistencia')

    def __repr__(self):
        return {
            'aprendiz': self.id_apren,
            'ficha': self.ficha,
            'state_asistencia': self.state_asis
        }
