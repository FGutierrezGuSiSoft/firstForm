FROM python:3.7.2-slim

RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
