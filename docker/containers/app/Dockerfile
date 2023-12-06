FROM python:3.10-alpine3.13

RUN pip install --upgrade pip

WORKDIR /usr/src/app

RUN apk --no-cache add shadow bash gcc musl-dev python3-dev g++ libffi-dev make musl-dev mariadb-connector-c-dev vim
COPY ./requirements.txt .
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"
RUN pip install rq curlify mysqlclient
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["python", "main.py"]
