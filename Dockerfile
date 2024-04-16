# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim-bullseye as base

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1


# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Poetry


# Copy poetry.lock and pyproject.toml
COPY  poetry.lock pyproject.toml ./

# Install Poetry

RUN poetry config virtualenvs.create false --local
RUN poetry install



