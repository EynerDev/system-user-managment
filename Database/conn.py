from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


host = os.getenv("HOST_DB")
user_name = os.getenv("USERNAME_DB")

password = os.getenv("PASSWORD_DB")
password = f":{password}" if password else ""

database = os.getenv("DATABASE_NAME")

URI = f"mysql+pymysql://{user_name}{password}@{host}/{database}"
print(URI)
engine = create_engine(URI)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()