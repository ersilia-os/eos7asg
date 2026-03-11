FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install padelpy==0.1.10
RUN conda install -c conda-forge openjdk=11

WORKDIR /repo
COPY . /repo
