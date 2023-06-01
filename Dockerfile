FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2023.3.1

WORKDIR /repo
COPY . /repo