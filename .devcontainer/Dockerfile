FROM mcr.microsoft.com/devcontainers/base:jammy

RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    python3-pip \
    python3-dev \
    build-essential

RUN pip install psycopg2-binary
