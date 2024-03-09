from sqlalchemy import Column, DateTime, Integer
from Database.conn import Base


class assign_ficha_instructor(Base):

    __tablename__ = "assign_ficha_instructor"

    assign_ficha_instructor = Column(Integer, nullable=False, primary_key=True,
                                     autoincrement=True),
    instructor_id = Column(Integer, nullable=False),
    ficha_id = Column(Integer, nullable=False),
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, nullable=False,
                        server_default='CURRENT_TIMESTAMP')
    update_at = Column(DateTime, nullable=False,
                       server_default='CURRENT_TIMESTAMP')

    def __init__(self, data):
        self.instructor_id = data.get("instructor_id"),
        self.ficha_id = data.get("ficha_id")

    def __repr__(self):
        return {
            'instructor_id': self.instructor_id,


        }
