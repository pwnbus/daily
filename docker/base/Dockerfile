FROM ubuntu:bionic

RUN \
  useradd -m daily && \
  apt-get update && \
  apt-get install -y \
    python3 \
    python3-pip \
    libmysqlclient-dev && \
  rm -rf /var/lib/apt/lists/* && \
  pip3 install virtualenv && \
  mkdir /app && \
  virtualenv -p `which python3` /venv

COPY docker/wait-for-container.sh /app/wait-for-container.sh
COPY docker/wait-for-port.sh /app/wait-for-port.sh
COPY setup.py /app/setup.py
COPY docker/config.yml /app/config.yml
COPY daily /app/daily

WORKDIR /app

USER root

RUN \
  chown -R daily:daily /app && \
  chown -R daily:daily /venv

USER daily

# Automatically source into python virtual environment
ENV PATH=/venv/bin:$PATH

RUN pip install -e .
