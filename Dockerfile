# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/order_management_api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add python3-dev build-base linux-headers pcre-dev

# logs dir
RUN mkdir /usr/src/logs

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
