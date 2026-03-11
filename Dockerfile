FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install openjdk=11
RUN pip install padelpy==0.1.10

WORKDIR /repo
COPY . /repo
