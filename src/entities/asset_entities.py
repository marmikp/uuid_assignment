import datetime
import json
import os
from typing import Annotated, Optional

from pydantic import BaseModel, Field

from common.aws_fs_helper import AwsS3FsHelper


class PhraseEntity(BaseModel):
    phraseId: int
    phrase: str


class UUIDEntity(BaseModel):
    Username: str
    Project_ID: int
    Language: str
    speaker_id: Annotated[Optional[int], Field(default=None)]


class DBAsset(BaseModel):
    id: Annotated[Optional[int], Field(default=None)]
    Project_ID: int
    Project_Name: str
    Language: str
    Audio_Playtime_In_Mins: float
    Frequency: int
    Job_Name: str
    Job_Status: str
    JobStartDate: str
    Asset_Name: str
    Asset_Path: str
    Asset_Status: str
    Asset_Start_Time: str
    Asset_Uploaded_Date: str
    Is_Active_Asset: Annotated[Optional[int], Field(default=None)]
    Collect_Asset_Status: str
    WorkFlow_Level: str
    Username: str
    Rejection_Reason: str
    Form_Type: str
    email: str
    age: int
    gender: str
    location: str
    uuid: str
    script: str
    Discarded_Reason: str
    delivery_status: bool = False
    user_approved: bool = True
    asset_approved: bool = True
    tech_rejection_reason: str = ''

    def get_db_entry(self):
        return self

    def get_uuid_entry(self):
        return UUIDEntity(**self.__dict__)

    def get_location(self):
        return json.loads(self.location.replace("\\", ""))

    def set_entity(self, entity, value):
        setattr(self, entity, value)


class CsvAssetRow(BaseModel):
    Project_ID: int
    Project_Name: str
    Language: str
    Audio_Playtime_In_Mins: float
    Frequency: int
    Job_Name: str
    Job_Status: str
    JobStartDate: str
    Asset_Name: str
    Asset_Path: str
    Asset_Status: str
    Asset_Start_Time: str
    Asset_Uploaded_Date: str
    Is_Active_Asset: Annotated[Optional[int], Field(default=None)]
    Collect_Asset_Status: str
    WorkFlow_Level: str
    Username: str
    Rejection_Reason: str
    Form_Type: str
    email: str
    age: int
    gender: str
    location: str
    uuid: str
    script: str
    Discarded_Reason: str
    delivery_status: bool = False
    user_approved: bool = True
    asset_approved: bool = True
    tech_rejection_reason: str = ''

    def get_db_entry(self):
        return DBAsset(**self.__dict__)

    def get_uuid_entry(self):
        return UUIDEntity(**self.__dict__)

    def get_location(self):
        return json.loads(self.location)

    def set_entity(self, entity, value):
        setattr(self, entity, value)


class AssetEntry(BaseModel):
    csv_entry: Annotated[CsvAssetRow, Field(default=None)]
    db_entry: Annotated[DBAsset, Field(default=None)]

    def get_entity(self, entity):
        if self.db_entry is not None:
            return self.db_entry.__dict__[entity]

        if self.csv_entry is not None:
            return self.csv_entry.__dict__[entity]

    def get_db_entry(self):
        if self.db_entry is not None:
            return self.db_entry.get_db_entry()
        if self.csv_entry is not None:
            return self.csv_entry.get_db_entry()

    def get_uuid_entry(self):
        if self.db_entry is not None:
            return self.db_entry.get_uuid_entry()
        if self.csv_entry is not None:
            return self.csv_entry.get_uuid_entry()

    def get_location(self):
        if self.db_entry is not None:
            return self.db_entry.get_location()
        if self.csv_entry is not None:
            return self.csv_entry.get_location()

    def set_entity(self, entity, value):
        if self.db_entry is not None:
            self.db_entry.set_entity(entity, value)
        if self.csv_entry is not None:
            self.csv_entry.set_entity(entity, value)
