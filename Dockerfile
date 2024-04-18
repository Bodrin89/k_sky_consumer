FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2

RUN pip install "poetry==$POETRY_VERSION"


RUN apt update && apt install -y netcat-openbsd

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi
COPY . .

