FROM python:3.9

ADD . /app
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
WORKDIR /app

CMD ["uvicorn", "app.main:app"]
