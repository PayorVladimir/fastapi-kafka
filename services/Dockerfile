FROM python:3.10-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN  pip install --upgrade pip setuptools wheel \
     && pip install -r requirements.txt \
     && rm -rf /root/.cache/pip \
