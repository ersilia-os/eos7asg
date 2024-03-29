FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -n base conda=4.12.0 
RUN conda install -c cyclus java-jre=8.45
RUN pip install padelpy==0.1.10
RUN conda update -n base -c defaults conda
RUN conda install -n base six

WORKDIR /repo
COPY . /repo
