FROM python:3.7.0-alpine3.8
RUN pip install scanless
USER 1000:1000
ENTRYPOINT ["scanless"]
