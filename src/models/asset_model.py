from typing import Optional

from pydantic import Field
from sqlalchemy import Column, String, Boolean, Integer, Float, JSON, DateTime, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class AssetModel(Base):
    __tablename__ = "usa_273_metadata"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Project_ID = Column(Integer)
    Project_Name = Column(String)
    Language = Column(String)
    Audio_Playtime_In_Mins = Column(Float)
    Frequency = Column(Integer)
    Job_Name = Column(String)
    Job_Status = Column(String)
    JobStartDate = Column(String)
    Asset_Name = Column(String)
    Asset_Path = Column(String)
    Asset_Status = Column(String)
    Asset_Start_Time = Column(String)
    Asset_Uploaded_Date = Column(String)
    Is_Active_Asset = Column(Integer)
    Collect_Asset_Status = Column(String)
    WorkFlow_Level = Column(String)
    Username = Column(String)
    Rejection_Reason = Column(String)
    Form_Type = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender = Column(String)
    location = Column(String)
    uuid = Column(String)
    script = Column(String)
    Discarded_Reason = Column(String)
    delivery_status = Column(Boolean, default=False)
    user_approved = Column(Boolean, default=True)
    asset_approved = Column(Boolean, default=True)
    tech_rejection_reason = Column(String, default='')
    #created_at = Column(DateTime, default=func.now())
    __table_args__ = (UniqueConstraint("Project_ID", "Asset_Name", name="UniqueAsset"),)

    def __repr__(self):
        return f"<USA273(id={self.id}, Project_ID={self.Project_ID}, Language={self.Language}, " \
               f"Audio_Playtime_In_Mins={self.Audio_Playtime_In_Mins}, Frequency={self.Frequency}, " \
               f"Job_Name={self.Job_Name}, Job_Status={self.Job_Status}, Task_Name={self.Task_Name}, " \
               f"Task_Status={self.Task_Status}, Task_Path={self.Task_Path}, WorkFlow_Level={self.WorkFlow_Level}, " \
               f"Username={self.Username}, Rejection_Reason={self.Rejection_Reason}, Form_Type={self.Form_Type}, " \
               f"email={self.email}, age={self.age}, gender={self.gender}, location={self.location}, " \
               f"uuid={self.uuid}, script={self.script}, created_at={self.created_at}, " \
               f"delivery_status={self.delivery_status})>"


class UUIDMapping(Base):
    __tablename__ = 'usa_273_uuid_speakerId_mapping'
    Username: Mapped[str] = mapped_column(unique=True)
    Project_ID = Column(Integer)
    Language = Column(String)
    speaker_id = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return (f"<UUIDMapping(id={self.id}, Project_ID={self.Project_ID}, Language='{self.Language}', "
                f"uuid='{self.uuid}')>")


class PhraseMapping(Base):
    __tablename__ = 'usa_273_phrase_mapping'
    phraseId: Mapped[int] = mapped_column(primary_key=True)
    phrase = Column(String)
