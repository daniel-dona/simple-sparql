FROM ubuntu:20.04



RUN apt-get update
RUN apt-get upgrade -y
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get install apt-utils nano -y
RUN apt-get install python3 python3-pip -y

RUN python3 -m pip install -U pip
RUN python3 -m pip install rdflib flask flask_restful requests Flask-Cors

VOLUME /data

COPY init.py /init.py
RUN chmod +x /init.py

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

CMD /init.py
