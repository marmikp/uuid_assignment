from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base = declarative_base()


class USA273(Base):
    __tablename__ = "usa_273_metadata"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Project_ID = Column(Integer)
    Language = Column(String)
    Audio_Playtime_In_Mins = Column(Float)
    Frequency = Column(Integer)
    Job_Name = Column(String)
    Job_Status = Column(String)
    Task_Name = Column(String)
    Task_Status = Column(String)
    Task_Path = Column(String)
    WorkFlow_Level = Column(String)
    Username = Column(String)
    Rejection_Reason = Column(String)
    Form_Type = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender = Column(String)
    location = Column(String)  # Assuming JSON for dictionary storage
    uuid = Column(String)
    script = Column(String)
    #created_at = Column(DateTime, default=func.now())
    delivery_status = Column(Boolean, default=False)


    def __repr__(self) -> str:
        return f"<USA273(id={self.id}, Project_ID={self.Project_ID}, Language={self.Language}, " \
               f"Audio_Playtime_In_Mins={self.Audio_Playtime_In_Mins}, Frequency={self.Frequency}, " \
               f"Job_Name={self.Job_Name}, Job_Status={self.Job_Status}, Task_Name={self.Task_Name}, " \
               f"Task_Status={self.Task_Status}, Task_Path={self.Task_Path}, WorkFlow_Level={self.WorkFlow_Level}, " \
               f"Username={self.Username}, Rejection_Reason={self.Rejection_Reason}, Form_Type={self.Form_Type}, " \
               f"email={self.email}, age={self.age}, gender={self.gender}, location={self.location}, " \
               f"uuid={self.uuid}, script={self.script}, created_at={self.created_at}, " \
               f"delivery_status={self.delivery_status})>"


def create_table(engine):
    Base.metadata.create_all(engine)