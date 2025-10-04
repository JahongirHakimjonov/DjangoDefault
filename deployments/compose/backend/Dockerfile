# syntax=docker/dockerfile:1.2
ARG PYTHON_VERSION=3.11
ARG UV_VERSION=0.7.2

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM python:${PYTHON_VERSION} AS builder
COPY --from=uv /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    PYTHONBUFFERED=1

WORKDIR /app

# Create a standard environment inside the project (uv installs dependencies there by default)
RUN uv venv /app/.venv
COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --no-dev --frozen --no-install-project --group docker \
    && mv /app/.venv /opt/venv

FROM python:${PYTHON_VERSION} AS app

WORKDIR /app

# Specify environment variables and PATH to the transferred environment
ENV PYTHONBUFFERED=1 \
    PYTHONPATH=$PYTHONPATH:/app \
    VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH

# Copy and set permissions for celery worker start script
COPY ./deployments/compose/backend/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker && \
    chmod +x /start-celeryworker

# Copy and set permissions for celery beat start script
COPY ./deployments/compose/backend/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat && \
    chmod +x /start-celerybeat

# Copy and set permissions for flower start script
COPY ./deployments/compose/backend/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower && \
    chmod +x /start-flower

# Copy and set permissions for entrypoint script
COPY ./deployments/compose/backend/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && \
    chmod +x /entrypoint

# Copy and set permissions for start script
COPY ./deployments/compose/backend/start /start
RUN sed -i 's/\r$//g' /start && \
    chmod +x /start

# Copy the transferred environment
COPY --from=builder /opt/venv /opt/venv
COPY ./pyproject.toml ./uv.lock ./
COPY src/. /app/

RUN chgrp -R 0 /app && chmod -R g=u /app

EXPOSE 8000

ENTRYPOINT ["/entrypoint"]