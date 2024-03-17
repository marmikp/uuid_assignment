from typing import Annotated, Optional
from enum import Enum
from pydantic import BaseModel, Field


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    non_binary = 'non-binary'


class Equipment(str, Enum):
    mobile = 'mobile'
    desktop = 'desktop'
    laptop = 'laptop'
    headset = 'headset'
    studio = 'studio'


class Platform(str, Enum):
    iOS = 'iOS'
    Andriod = 'Android'
    Windows = 'Windows'


class CsvRow(BaseModel):
    Project_ID: int
    Project_Name: str
    Language: str
    Audio_Playtime_In_Mins: float
    Frequency: str
    Job_Name: str
    Job_Status: str
    job_task_assets_info_id: str
    Task_Name: str
    Task_Status: str
    Task_Path: str
    WorkFlow_Level: str
    Username: str
    Rejection_Reason: str
    Form_Type: str
    Email: str
    Gender: str
    Location: str
    UUID: str
    Age: str
    NativeCountry: str
    Platform: str
    Script: str
    PromptFileName: str


class AudioInfo(BaseModel):
    audio_path: str
    text_transcription: str
    age: str
    gender: Gender
    speaker_id: str
    speaker_culture: str
    equipment: Equipment
    platform: Platform
    noise_env: str

