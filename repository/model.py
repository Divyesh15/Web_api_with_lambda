from sqlalchemy import Column, Integer
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StudentModel(Base):
    __tablename__ = 'student_info'
    roll_no = Column("roll_no", Integer, autoincrement=True, primary_key=True)
    name = Column("name", VARCHAR(100))
