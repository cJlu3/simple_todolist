from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None] = mapped_column(String(200))
    desc: Mapped[str | None]
    is_done: Mapped[bool] = mapped_column(default=False)
    create_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=func.now(),
    )
    finish_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=None,
    )


class Task_DB_Model(BaseModel):
    id: int | None = Field(default=None)
    title: str = Field(min_length=1, max_length=200)
    desc: str | None
    is_done: bool = Field(default=False)
    create_date: datetime | None = Field(default=None)
    finish_date: datetime | None = Field(default=None)

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


class Task_Schema(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    desc: str | None
    is_done: bool = Field(default=False)
    finish_date: datetime | None = Field(default=None, examples=[None])

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
