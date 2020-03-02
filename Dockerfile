FROM python:3.8-slim

COPY ./requirements.txt . 
RUN pip install -r requirements.txt

COPY . /stainless

WORKDIR /stainless

ENTRYPOINT ["python"]
CMD ["app.py"]
