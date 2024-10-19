FROM python:3.10-slim-buster


# Set environment variables to ensure UTF-8 encoding
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Install Flower for Celery monitoring
#RUN pip install flower

# Copy and set permissions for celery worker start script
#COPY ./deployments/compose/django/celery/worker/start /start-celeryworker
#RUN sed -i 's/\r$//g' /start-celeryworker && \
#    chmod +x /start-celeryworker

# Copy and set permissions for celery beat start script
#COPY ./deployments/compose/django/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r$//g' /start-celerybeat && \
#    chmod +x /start-celerybeat

# Copy and set permissions for flower start script
#COPY ./deployments/compose/django/celery/flower/start /start-flower
#RUN sed -i 's/\r$//g' /start-flower && \
#    chmod +x /start-flower

# Update and install necessary packages
RUN apt update && apt upgrade -y && apt install git -y && apt install -y gettext

WORKDIR /app
COPY . /app

# Update pip and install requirements
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    pip install gunicorn && \
    pip install uvicorn

# Copy and set permissions for entrypoint script
COPY ./deployments/compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && \
    chmod +x /entrypoint

# Copy and set permissions for start script
COPY ./deployments/compose/django/start /start
RUN sed -i 's/\r$//g' /start && \
    chmod +x /start


ENTRYPOINT ["/entrypoint"]
