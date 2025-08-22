from datetime import datetime
from typing import Optional
from todolist.models import Task_Model, Task_DB_Model
from todolist.repository import TasksRepository


class TodoService:
    @classmethod
    def add(cls, task: Task_Model):
        task_dict = task.to_dict()
        TasksRepository.add(task_dict)

    @classmethod
    def get(cls, task_id: int):
        task = TasksRepository.get(task_id)
        res = Task_DB_Model.model_validate(task)
        return res

    @classmethod
    def list(
        cls,
        title: Optional[str] = None,
        desc: Optional[str] = None,
        is_done: Optional[bool] = None,
        create_date: Optional[datetime] = None,
        finish_date: Optional[datetime] = None,
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
        lst = TasksRepository.list(filter)
        res = []
        for item in lst:
            task = Task_DB_Model.model_validate(item)
            res.append(task)
        return res

    @classmethod
    def count(cls):
        res = TasksRepository.count()
        return res

    @classmethod
    def update(cls, task_id: int, task: Task_Model):
        values = task.to_dict()
        TasksRepository.update(task_id, values)

    @classmethod
    def finish(cls, task_id: int):
        TasksRepository.finish(task_id)

    @classmethod
    def delete(cls, task_id):
        TasksRepository.delete(task_id)

    @classmethod
    def delete_all(cls):
        TasksRepository.delete_all()
