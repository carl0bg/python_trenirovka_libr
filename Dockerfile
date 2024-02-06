FROM python:3

COPY . /python
WORKDIR /python

EXPOSE 8081

RUN python main.py


CMD [ "python", "main.py" ]