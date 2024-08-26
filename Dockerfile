FROM python:3.12-slim

COPY . /app
WORKDIR /app
RUN mkdir -p /app/src
VOLUME /app/src
RUN pip install -r requirements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
#CMD [ "python3", "main.py" ]

