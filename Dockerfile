FROM python:3.8.10 AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
       build-essential \
       curl \
       git \
       jq \
       libgomp1 \
       vim
       
WORKDIR /app

RUN pip install --no-cache --upgrade pip

RUN pip install rasa==2.8.14

RUN pip install pandas

RUN pip install python-dotenv

RUN pip install openpyxl

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml


