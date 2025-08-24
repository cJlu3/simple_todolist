from typing import Optional

from sqlalchemy import delete, func, insert, select, update

from core import async_session_factory
from todolist.models import Tasks


class TasksRepository:
    @classmethod
    async def add(cls, values: dict):
        stmt = insert(Tasks).values(**values)
        async with async_session_factory() as session:
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def get(cls, task_id: int):
        query = select(Tasks).where(Tasks.id == task_id)
        async with async_session_factory() as session:
            query_res = await session.execute(query)
            res = query_res.scalar_one()
        return res

    @classmethod
    async def list(
        cls,
        filter: dict,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        query = select(Tasks).filter_by(**filter).limit(limit).offset(offset)
        async with async_session_factory() as session:
            query_res = await session.execute(query)
            res = query_res.scalars().all()
        return res

    @classmethod
    async def count(cls) -> int:
        query = func.count(Tasks.id)
        async with async_session_factory() as session:
            query_res = await session.execute(query)
            res = query_res.scalar_one()
        return res

    @classmethod
    async def update(cls, task_id: int, values: dict):
        stmt = update(Tasks).where(Tasks.id == task_id).values(**values)
        async with async_session_factory() as session:
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def finish(cls, task_id: int):
        stmt = update(Tasks).where(Tasks.id == task_id).values(is_done=True)
        async with async_session_factory() as session:
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def delete(cls, task_id: int):
        stmt = delete(Tasks).where(Tasks.id == task_id)
        async with async_session_factory() as session:
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def delete_all(cls):
        stmt = delete(Tasks)
        async with async_session_factory() as session:
            await session.execute(stmt)
            await session.commit()
