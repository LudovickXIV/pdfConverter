#FROM ubuntu:18.04
FROM python:3.8.3

RUN apt-get update && apt-get install -y \
    python-pip \
    wkhtmltopdf

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

COPY requirements.txt .
COPY manage.py /app/
RUN pip install -r requirements.txt

# copy project
COPY . .
ENTRYPOINT exec python manage.py runserver 0.0.0.0:8000
#CMD ["runserver", "0.0.0.0:8000"]