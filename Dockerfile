FROM python:3.8.3-alpine
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk add --no-cache gcc musl-dev python3-dev
RUN pip install ruamel.yaml.clib
RUN pip install -r requirements.txt
COPY . .