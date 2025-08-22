from typing import Optional

from sqlalchemy import delete, func, insert, select, update

from db import Session
from todolist.models import Tasks


class TasksRepository:
    @classmethod
    async def add(cls, values: dict):
        stmt = insert(Tasks).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def get(cls, task_id: int):
        query = select(Tasks).where(Tasks.id == task_id)
        with Session() as session:
            query_res = session.execute(query)
            res = query_res.scalar_one()
        return res

    @classmethod
    def list(
        cls,
        filter: dict,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        query = select(Tasks).filter_by(**filter).limit(limit).offset(offset)
        with Session() as session:
            query_res = session.execute(query)
            res = query_res.scalars().all()
        return res

    @classmethod
    def count(cls) -> int:
        query = func.count(Tasks.id)
        with Session() as session:
            query_res = session.execute(query)
            res = query_res.scalar_one()
        return res

    @classmethod
    def update(cls, task_id: int, values: dict):
        stmt = update(Tasks).where(Tasks.id == task_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def finish(cls, task_id: int):
        stmt = update(Tasks).where(Tasks.id == task_id).values(is_done=True)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, task_id: int):
        stmt = delete(Tasks).where(Tasks.id == task_id)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        stmt = delete(Tasks)
        with Session() as session:
            session.execute(stmt)
            session.commit()
