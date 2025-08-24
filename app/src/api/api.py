from datetime import datetime
from typing import Optional

from fastapi import FastAPI

from todolist.models import Task_Schema
from todolist.service import TodoService
from api.schemas import ResponseData, ResponseOK

app = FastAPI()


@app.post("/api/v1/tasks", response_model=ResponseOK)
async def add_task(new_task: Task_Schema) -> dict:
    await TodoService.add(new_task)
    return {"success": True}


@app.get("/api/v1/tasks/{task_id}", response_model=ResponseData)
async def get_task_by_id(task_id: int) -> dict:
    data = await TodoService.get(task_id)
    return {"success": True, "data": data}


@app.get("/api/v1/tasks", response_model=ResponseData)
async def get_all_tasks(
    title: Optional[str],
    desc: Optional[str],
    is_done: Optional[bool],
    create_date: Optional[datetime],
    finish_date: Optional[datetime],
    limit: Optional[int],
    offset: Optional[int],
) -> dict:
    data = await TodoService.list(
        title=title,
        desc=desc,
        is_done=is_done,
        create_date=create_date,
        finish_date=finish_date,
        limit=limit,
        offset=offset,
    )
    return {"success": True, "data": data}


@app.get("/api/v1/tasks/count", response_model=ResponseData)
async def count_all_tasks() -> dict:
    count = await TodoService.count()
    return {"success": True, "data": count}


@app.put("/api/v1/tasks/{task_id}", response_model=ResponseOK)
async def update_task_by_id(task_id: int, new_task: Task_Schema) -> dict:
    await TodoService.update(task_id=task_id, task=new_task)
    return {"success": True}


@app.patch("/api/v1/tasks/{task_id}", response_model=ResponseOK)
async def complete_task_by_id(task_id: int) -> dict:
    await TodoService.finish(task_id=task_id)
    return {"success": True}


@app.delete("/api/v1/tasks/{task_id}", response_model=ResponseOK)
async def delete_task_by_id(task_id: int) -> dict:
    await TodoService.delete(task_id=task_id)
    return {"success": True}


@app.delete("/api/v1/tasks", response_model=ResponseOK)
async def delete_all_tasks() -> dict:
    await TodoService.delete_all()
    return {"success": True}
