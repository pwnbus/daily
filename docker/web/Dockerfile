FROM python:3

WORKDIR /usr/src/app

COPY setup.py /usr/src/app/setup.py
COPY config.yml /usr/src/app/config.yml
COPY bin /usr/src/app/bin
COPY dashboard /usr/src/app/dashboard

RUN pip install -e .

CMD ["/usr/src/app/bin/web"]
