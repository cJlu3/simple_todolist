from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI

from todolist.models import Task_DB_Model, Task_Model
from todolist.service import TodoService

app = FastAPI()


@app.post("/db/add")
def add(new_task: Task_Model) -> dict:
    TodoService.add(new_task)
    return {"ok": True, "added data": new_task}


@app.get("/db/get")
def get_by_id(task_id: int) -> Task_DB_Model:
    return TodoService.get(task_id)


@app.get("/db/list")
def filtered_list(
    title: Optional[str] = None,
    desc: Optional[str] = None,
    is_done: Optional[bool] = None,
    create_date: Optional[datetime] = None,
    finish_date: Optional[datetime] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[Task_DB_Model]:
    return TodoService.list(
        title=title,
        desc=desc,
        is_done=is_done,
        create_date=create_date,
        finish_date=finish_date,
        limit=limit,
        offset=offset,
    )


@app.get("/db/count")
def count_all_tasks() -> dict:
    count = TodoService.count()
    return {"ok": True, "tasks count": count}


@app.put("/db/update")
def task_update(task_id: int, new_task: Task_Model) -> dict:
    old_task = TodoService.get(task_id)
    TodoService.update(task_id=task_id, task=new_task)
    return {"ok": True, "old_data": old_task, "new_data": new_task}


@app.patch("/db/finish")
def task_finish(task_id: int) -> dict:
    TodoService.finish(task_id=task_id)
    finished_task = TodoService.get(task_id)
    return {"ok": True, "finished_task": finished_task}


@app.delete("/db/delete")
def task_delete(task_id: int) -> dict:
    deleted_task = TodoService.get(task_id)
    TodoService.delete(task_id=task_id)
    return {"ok": True, "deleted task": deleted_task}


@app.delete("/db/delete_all")
def delete_all_tasks() -> dict:
    TodoService.delete_all()
    return {"ok": True}
