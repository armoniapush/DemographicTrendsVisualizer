FROM python:3.10.12

WORKDIR /appdocker
COPY requirements.txt /appdocker/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /appdocker/requirements.txt

COPY . /appdocker

CMD bash -c "while true; do sleep 1; done"
