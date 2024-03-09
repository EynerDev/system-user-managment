from sqlalchemy import Column, Text, Integer, DateTime
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class ItemsModel(Base):

    __tablename__ = 'items'

    item_id = Column(Integer, nullable=False, primary_key=True,
                     autoincrement=True)
    description = Column(Text, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())

    def __init__(self, data):
        self.description = self.description

    def __repr__(self):
        return {
            "description": self.description
        }
