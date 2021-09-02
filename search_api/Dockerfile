FROM python:3.9.4

RUN mkdir -p /search_api
WORKDIR /search_api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /search_api

# ENTRYPOINT [ "python" ]
# CMD [ "setup.py"," BUILD_ELASTIC=False", "ELASTIC_HOST=elasticsearch"]
CMD ["uwsgi", "app.ini"]