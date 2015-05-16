FROM aexea/django-base
MAINTAINER Aexea Carpentry

WORKDIR meta_efa
USER root
ENTRYPOINT ["./start.sh"]
CMD ["web"]
