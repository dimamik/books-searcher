FROM python:3.9.4

RUN mkdir -p /rec_api
WORKDIR /rec_api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /rec_api

ENTRYPOINT [ "python" ]
CMD [ "setup.py", "ELASTIC_HOST=elasticsearch"]