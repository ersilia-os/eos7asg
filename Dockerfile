FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install padelpy==0.1.10

WORKDIR /repo
COPY ./repo
