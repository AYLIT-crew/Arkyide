# The builder image, used to build the virtual environment
FROM python:3.12-slim-bookworm AS builder

# Locking version to 1.8.3
RUN pip install poetry==1.8.3


ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --no-dev --no-root && rm -rf $POETRY_CACHE_DIR
RUN apt-get update && apt-get install -y nmap

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.12-slim-bookworm AS runner

ENV VIRTUAL_ENV=/app/.venv \ 
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
RUN apt-get update && apt-get install -y nmap

COPY arkyide.py ./arkyide.py

ENTRYPOINT [ "python", "arkyide.py" ]

FROM builder AS test

ENV VIRTUAL_ENV=/app/.venv \ 
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY arkyide.py ./arkyide.py
COPY tests ./tests

RUN poetry install --with dev --no-root && rm -rf $POETRY_CACHE_DIR

ENTRYPOINT [ "poetry", "run", "pytest" ]
