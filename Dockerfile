FROM asmaps/ubuntu
MAINTAINER Arne Schauf

USER root

# install geo stuff
RUN apt-get update && apt-get install -y \
    lib32z1-dev \
    libfreetype6-dev \
    libjpeg8-dev \
    libxml2-dev \
    libxslt1-dev \
    postgresql-client \
    postgresql-server-dev-all \
    python-virtualenv \
    python3-pip \
    zlib1g-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install psycopg2 gunicorn Pillow pandas xlrd

ADD requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install -Ur requirements.txt
COPY . /opt/code

RUN chown -R uid1000: /opt

WORKDIR /opt/code/meta_efa

USER uid1000
EXPOSE 8000

# production stuff
ENTRYPOINT ["./start.sh"]
CMD ["web"]
