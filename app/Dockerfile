FROM python:latest

WORKDIR /app

COPY ./src/ ./src/
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "src/main.py" ]
