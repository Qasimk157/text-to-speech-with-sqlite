from sqlalchemy import Column, Integer, String

from .database import Base


class TTSPayload(Base):

    __tablename__ ='TTs'
    Id=Column(Integer,primary_key=True,index=True)
    enterText=Column(String)