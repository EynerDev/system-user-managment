from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class InstructorModel(Base):
    
    __tablename__ = "instructor"
    
    instructor_id = Column(Integer, autoincrement=True, primary_key=True,
                           nullable=False)
    user_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.user_id = data.get('user_id')

    def __repr_(self):
        return {
            'user_id': self.user_id,
        }
