FROM python:3.9.13

ENV PYTHONUNBUFFERED 1

WORKDIR /webstatistics/
COPY requirements.txt ./requirements.txt
COPY ./webstatistics ./
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


