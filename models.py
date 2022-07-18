import datetime
from email import message
from email.policy import default
import string
from database import Base
from sqlalchemy import ForeignKey,Column
from sqlalchemy import String, Boolean, Integer, Text, DateTime

class Message(Base):
    __tablename__='messages'
    id=Column(Integer,primary_key=True,autoincrement=True)
    message=Column(Text)
    status=Column(Integer,default=1)
    created_at = Column(DateTime,default=datetime.datetime.now())
    def __repr__(self) -> str:
        return f"<Item Message={self.message}>"



class Numbers(Base):
    __tablename__='numbers'
    id=Column(Integer,primary_key=True,autoincrement=True)
    message_id=Column(Integer)
    number=Column(Integer)
    status=Column(Integer,default=1)
    created_at = Column(DateTime,default=datetime.datetime.now())
    def __repr__(self) -> str:
        return f"<Item Message={self.message}>"
