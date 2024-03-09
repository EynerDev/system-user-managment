from sqlalchemy import Column, String, Text, DateTime, Integer, BigInteger
from Database.conn import Base
from sqlalchemy.sql.functions import current_timestamp


class UsersModel(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, nullable=False, autoincrement=True,
                     primary_key=True)
    type_doc = Column(Integer, nullable=False)
    document = Column(BigInteger, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(Text, nullable=False)
    number = Column(BigInteger, nullable=False)
    user_role_id = Column(Integer, nullable=False)
    user_name = Column(String(50), nullable=False)
    password = Column(Text, nullable=False)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.type_doc = data.get('type_doc')
        self.document = data.get('document')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name').title()
        self.email = data.get('email')
        self.number = data.get('number')
        self.user_role_id = data.get('user_role_id')
        self.user_name = data.get('user_name')
        self.password = data.get('password')

    def __repr__(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'number': self.number,
            'user_name': self.user_name,
            'user_role_id': self.user_role_id,

        }
