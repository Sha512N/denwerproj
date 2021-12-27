from sqlalchemy import Column, Integer, String
from sqlalchemy import Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQL = 'mysql+pymysql://root@localhost:3306/system_types'
ENGINE = create_engine(SQL)

BASE = declarative_base()

class ArchType(BASE):
    ID = Column(Integer, primary_key=True)
    NAME = Column(Text)
    PARENT_ID = Column(Integer)
    SHORT_LINK = Column(String(15))
    __tablename__ = 'archi_types'


class ArchDescription(BASE):
    ID = Column(Integer, primary_key=True)
    ARCH_ID = Column(Integer)
    TEXT = Column(Text)
    __tablename__ = 'arch_desc'