FROM python:3.10.4-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /telegrambott
WORKDIR /telegrambott

RUN pip install --upgrade pip
ADD requirements.txt /telegrambott/
RUN pip install -r requirements.txt
ADD . /telegrambott/