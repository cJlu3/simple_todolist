from datetime import datetime
from typing import Optional

from todolist.models import Task_DB_Model, Task_Schema
from todolist.repository import TasksRepository


class TodoService:
    @classmethod
    async def add(cls, task: Task_Schema):
        task_dict = task.to_dict()
        await TasksRepository.add(task_dict)

    @classmethod
    async def get(cls, task_id: int):
        task = await TasksRepository.get(task_id)
        res = Task_DB_Model.model_validate(task)
        return res

    @classmethod
    async def list(
        cls,
        title: Optional[str] = None,
        desc: Optional[str] = None,
        is_done: Optional[bool] = None,
        create_date: Optional[datetime] = None,
        finish_date: Optional[datetime] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        filter = {
            k: v
            for k, v in {
                "title": title,
                "desc": desc,
                "is_done": is_done,
                "create_date": create_date,
                "finish_date": finish_date,
            }.items()
            if v is not None
        }
        lst = await TasksRepository.list(filter, limit=limit, offset=offset)
        res = []
        for item in lst:
            task = Task_DB_Model.model_validate(item)
            res.append(task)
        return res

    @classmethod
    async def count(cls):
        res = await TasksRepository.count()
        return res

    @classmethod
    async def update(cls, task_id: int, task: Task_Schema):
        values = task.to_dict()
        await TasksRepository.update(task_id, values)

    @classmethod
    async def finish(cls, task_id: int):
        await TasksRepository.finish(task_id)

    @classmethod
    async def delete(cls, task_id):
        await TasksRepository.delete(task_id)

    @classmethod
    async def delete_all(cls):
        await TasksRepository.delete_all()
