FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03.4

WORKDIR /repo
COPY . /repo
