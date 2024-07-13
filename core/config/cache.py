import os

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_CACHE_URL"),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "core",
    }
}

CACHE_MIDDLEWARE_SECONDS = os.getenv("CACHE_TIMEOUT")

# In your Django settings.py or a dedicated Celery configuration module

CELERY_BROKER_URL = os.getenv("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("RABBITMQ_RESULT_BACKEND")
