FROM python:3.8-slim-buster

## install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean

COPY ./requirements.txt . 
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
