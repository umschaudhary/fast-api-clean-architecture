FROM python

WORKDIR /project

COPY pyproject.toml .
COPY poetry.lock .


RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

RUN poetry install
COPY . .


EXPOSE 8000

