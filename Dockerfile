FROM python:3.9

LABEL  maintainer "Shinichi Nakagawa <spirits.is.my.rader@gmail.com>"

# install
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

# app
COPY sample_app.py ./
ADD datasets datasets
CMD streamlit run --server.port 8080 sample_app.py