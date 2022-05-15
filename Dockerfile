FROM python:3.10.4-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/