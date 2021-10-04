FROM python:alpine3.7

RUN apk add postgresql-dev postgresql g++
WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT sh -c bin/start
EXPOSE 8000
