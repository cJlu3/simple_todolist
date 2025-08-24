# 📝 TodoList API

Небольшое учебное приложение для работы со списком задач.

---

## 🚀 Возможности

- Добавление новых задач  
- Получение задачи по ID  
- Получение списка задач (с фильтрацией)  
- Обновление и удаление задач  
- Хранение данных в PostgreSQL  
- Автоматическая документация API (Swagger UI / ReDoc)  

---

## 🛠 Стек технологий

- **Python 3.13**
- **FastAPI** — современный фреймворк для API  
- **SQLAlchemy (async)** — работа с PostgreSQL  
- **PostgreSQL** — реляционная база данных  
- **Docker & Docker Compose** — контейнеризация приложения и базы данных  

---

## 📦 Запуск

1. Запустить через Docker Compose:

    ```bash
    docker compose up --build
    ```

2. API будет доступно по адресу:

    ```
    http://localhost:8000
    ```

3. документация Swagger UI:

    ```
    http://localhost:8000/docs
    ```

---

## 📂 Структура проекта

```
todolist/
├── app/
│   ├── src/
│   │   ├── api/
|   |   |   ├── api.py
|   |   |   └── schemas.py
│   |   ├── todolist/
|   |   |   ├── models.py
|   |   |   ├── repository.py
|   |   |   └── service.py
│   |   ├── config.py
│   |   ├── core.py
|   |   └── main.py
│   ├── requirements.txt
|   └── Dockerfiles
├── docker-compose.yml
├── .env
└── README.md
```

---

## 📌 Планы по доработке

- [ ] Написание тестов
- [ ] Добавление JWT-аутентификации
- [ ] Добавить поддержку Redis
