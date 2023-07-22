FROM python:3.11.4-alpine

WORKDIR /opt/tchaikovsky
COPY . .
RUN adduser -D dj && chown -R dj /opt/tchaikovsky

RUN pip install --no-cache --upgrade pip \
    pip install --no-cache -r requirements.txt

USER dj
ENTRYPOINT ["python3", "main.py"]
