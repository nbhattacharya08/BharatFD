# filepath: /home/nilanjan/Documents/Coding/BharatFD_assignment/Dockerfile
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/
COPY wait-for-it.sh /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]