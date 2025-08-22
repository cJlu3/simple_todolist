from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[Optional[str]] = mapped_column(nullable=True)
    is_done: Mapped[bool] = mapped_column(nullable=False, default=False)
    create_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        nullable=False,
        default=func.now(),
    )
    finish_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )


class Task_DB_Model(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=1, max_length=200)
    desc: Optional[str]
    is_done: bool = Field(default=False)
    create_date: Optional[datetime] = Field(default=None)
    finish_date: Optional[datetime] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in ["title", "desc", "is_done"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict(self) -> dict:
        return self.model_dump(exclude={"id", "create_date"})

    def __str__(self) -> str:
        line = f"\n\
            id      = {self.id}\n\
            title   = {self.title}\n\
            desc    = {self.desc}\n\
            is_done = {self.is_done}\n\
            created = {self.create_date}\n\
            finish  = {self.finish_date}"
        return line


class Task_Model(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    desc: Optional[str]
    is_done: bool = Field(default=False)
    finish_date: Optional[datetime] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in ["title", "desc", "is_done"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict(self) -> dict:
        return self.model_dump()

    def __str__(self) -> str:
        line = f"\n\
            title   = {self.title}\n\
            desc    = {self.desc}\n\
            is_done = {self.is_done}\n\
            finish  = {self.finish_date}"
        return line
