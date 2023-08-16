FROM python:3.10.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHEK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --fix-missing gcc default-libmysqlclient-dev pkg-config default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
