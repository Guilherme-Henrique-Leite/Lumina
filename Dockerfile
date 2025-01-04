FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONPATH="/app"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY . .

RUN poetry install --no-interaction --no-ansi

RUN mkdir -p /app/customer_management/raw/bronze \
    && touch /app/customer_management/raw/bronze/__init__.py \
    && touch /app/customer_management/raw/__init__.py

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "customer_management/app.py"] 