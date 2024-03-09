from sqlalchemy import Column, Integer, Text, DateTime
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class SubItemsModel(Base):

    __tablename__ = "sub_items"

    sub_items_id = Column(Integer, nullable=False, primary_key=True,
                          autoincrement=True)
    item_id = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())

    def __init__(self, data):
        self.item_id = data.get["id_item"],
        self.description = data.get["description"]

    def __repr__(self):
        return {
            "sub_item_id": self.sub_items_id,
            "id_item": self.item_id,
            "description": self.description
        }
