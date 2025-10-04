# syntax=docker/dockerfile:1.2
ARG PYTHON_VERSION=3.11
ARG UV_VERSION=0.7.2

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM python:${PYTHON_VERSION} AS builder
COPY --from=uv /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    PYTHONBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/opt/venv

WORKDIR /app

# Копируем спецификации зависимостей
COPY ./pyproject.toml ./uv.lock ./

# Создание и установка зависимостей сразу в /opt/venv (без перемещения)
RUN uv sync --no-dev --frozen --no-install-project --all-groups

FROM python:${PYTHON_VERSION} AS app

WORKDIR /app

ENV PYTHONBUFFERED=1 \
    PYTHONPATH=$PYTHONPATH:/app \
    VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH

# Copy and set permissions for celery worker start script
#COPY ./deployments/compose/backend/celery/worker/start /start-celeryworker
#RUN sed -i 's/\r$//g' /start-celeryworker && chmod +x /start-celeryworker

# Copy and set permissions for celery beat start script
#COPY ./deployments/compose/backend/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r$//g' /start-celerybeat && chmod +x /start-celerybeat

# Copy and set permissions for flower start script
#COPY ./deployments/compose/backend/celery/flower/start /start-flower
#RUN sed -i 's/\r$//g' /start-flower && chmod +x /start-flower

# Copy and set permissions for entrypoint script
COPY ./deployments/compose/backend/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

# Copy and set permissions for start script
COPY ./deployments/compose/backend/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

# Копируем готовое окружение
COPY --from=builder /opt/venv /opt/venv
COPY ./pyproject.toml ./uv.lock ./
COPY src/. /app/

RUN chgrp -R 0 /app && chmod -R g=u /app

ENTRYPOINT ["/entrypoint"]