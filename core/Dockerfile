FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . .

RUN apt-get update

RUN apt-get install -y python3-dev default-libmysqlclient-dev

RUN pip3 install -r requirements.txt