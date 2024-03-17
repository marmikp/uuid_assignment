from sqlalchemy import Integer, Column, String, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class Logging:
    __tablename__ = "usa_273_logs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    command = Column(String)
    system_ip = Column(String)
    execution_timestamp = Column(DateTime, default=func.now())
