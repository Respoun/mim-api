FROM python:3.7-alpine

ADD . /app
COPY ./requirements.txt /code/requirements.txt
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
WORKDIR /app

CMD ["./start.sh"]