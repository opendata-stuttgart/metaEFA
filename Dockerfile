FROM aexea/aexea-base:py3.5
MAINTAINER Aexea Carpentry

ADD requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install -Ur requirements.txt

ADD . /opt/code
WORKDIR /opt/code/meta_efa

USER uid1000
EXPOSE 8000

ENTRYPOINT ["./start.sh"]
