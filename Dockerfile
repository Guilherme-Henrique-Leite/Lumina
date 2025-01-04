FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock ./
COPY customer_management/ ./customer_management/
COPY .env ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "customer_management/app.py", "--server.port=8501", "--server.address=0.0.0.0"] 