FROM bentoml/model-server:0.11.0-py312
MAINTAINER ersilia

RUN pip install rdkit==2024.9.6

WORKDIR /repo
COPY . /repo