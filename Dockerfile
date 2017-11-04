FROM python:3

ADD . /scanless
WORKDIR /scanless

RUN python setup.py install

ENTRYPOINT ["scanless"]

# vim: ft=Dockerfile:
