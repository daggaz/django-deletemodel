FROM python:3.13-slim AS base

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src /app
WORKDIR /app/

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]
