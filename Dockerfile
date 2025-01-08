FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONPATH="/workspace"

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY . .

RUN mkdir -p customer_management/raw/bronze \
    && mkdir -p customer_management/raw/silver \
    && mkdir -p customer_management/raw/gold \
    && mkdir -p customer_management/streamlit/pages \
    && mkdir -p customer_management/controller \
    && mkdir -p customer_management/database \
    && mkdir -p customer_management/models \
    && mkdir -p customer_management/utils \
    && touch customer_management/__init__.py \
    && touch customer_management/raw/__init__.py \
    && touch customer_management/raw/bronze/__init__.py \
    && touch customer_management/raw/silver/__init__.py \
    && touch customer_management/raw/gold/__init__.py \
    && touch customer_management/streamlit/__init__.py \
    && touch customer_management/streamlit/pages/__init__.py \
    && touch customer_management/controller/__init__.py \
    && touch customer_management/database/__init__.py \
    && touch customer_management/models/__init__.py \
    && touch customer_management/utils/__init__.py

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "customer_management/app.py"] 