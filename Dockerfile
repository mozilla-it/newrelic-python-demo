FROM python:3

WORKDIR /app

ENV PATH /app:$PATH

ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

ENTRYPOINT ./entrypoint.sh

