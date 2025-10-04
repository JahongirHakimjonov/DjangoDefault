# Django Default

![banner](https://i.postimg.cc/WzS3fs9f/Pics-Art-24-07-08-01-10-45-321.png "banner")

> Opinionated стартовый шаблон Django 5.2 с современным стеком: DRF + SimpleJWT, Unfold admin, многоязычие (
> modeltranslation), CKEditor 5, Redis cache, Celery, Swagger / Redoc (drf-spectacular), PostgreSQL, Docker, Taskfile,
> ruff, mypy, pytest.
>
> English summary: Ready-to-use Django 5.2 boilerplate with REST, JWT auth, multilingual setup, async tasks, rich
> admin & tooling.

### Требования

- Установить [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Установить [Docker](https://docs.docker.com/get-docker/)
- Установить [Task](https://taskfile.dev/installation/) или использовать команду `uvx --from go-task-bin task`

Готовый стек / инструменты, которые могут использоваться в микросервисном backend окружении:

- [Django](https://www.djangoproject.com/) – веб-фреймворк
- [uvicorn](https://www.uvicorn.org/) – ASGI сервер
- [gunicorn](https://gunicorn.org/) – WSGI сервер
- [PostgreSQL](https://www.postgresql.org/) – реляционная база данных
- [uv](https://docs.astral.sh/uv/) – инструмент для управления зависимостями и запусков
- [pytest](https://docs.pytest.org/en/7.4.x/) – тестирование
- [ruff](https://beta.ruff.rs/docs/) – линтер и автоформатер
- [mypy](https://mypy-lang.org/) – статическая типизация
- [pre-commit](https://pre-commit.com/) – git хуки
- [docker](https://www.docker.com/) – контейнеризация
- [task](https://taskfile.dev/) – автоматизация задач

---

## Содержание

1. Функционал
2. Архитектура и структура каталогов
3. Стек технологий
4. Быстрый старт (локально / Docker)
5. Переменные окружения
6. Управление зависимостями (uv)
7. Management-команды
8. API документация (drf-spectacular)
9. Аутентификация (SimpleJWT)
10. Многоязычность (i18n & modeltranslation)
11. Админ-панель (Unfold)
12. Редактор (django-ckeditor-5)
13. Кеш и Redis
14. Фоновая обработка задач (Celery + Flower, RabbitMQ / Redis)
15. Качество кода (ruff, mypy, deptry, pre-commit)
16. Тестирование (pytest + Taskfile)
17. Логи и мониторинг
18. Docker / Продакшен рекомендации
19. Обновление / Расширение
20. Donate & Контакты

---

## 1. Функционал

- Шаблон с разделением на `core` и прикладные приложения в `apps/`.
- Кастомная модель пользователя `users.User`.
- DRF c JWT-аутентификацией (SimpleJWT) и схемами OpenAPI (drf-spectacular + sidecar UI).
- Многоязычие (en / uz / ru) + локали в `assets/locale`.
- Админ-панель на базе Unfold с доп. интеграциями (filters, forms, import_export, guardian, simple_history).
- CKEditor 5 для богатого текста.
- Redis cache + (опционально) Celery брокер/бэкенд (Redis или RabbitMQ).
- Celery Worker / Beat / Flower (готовы в docker-compose закомментированы).
- Docker окружение с PostgreSQL 16.
- Taskfile автоматизирует lint / format / typecheck / tests / coverage.
- Управление зависимостями через `uv` (быстрее pip + lock-файл).
- Набор кастомных management-команд: `createadmin`, `makeapp`, `nginx`, `secret_key`.
- Подготовлено для CI (форматирование, типы, тесты, покрытие).

---

## 2. Архитектура / Структура

```
src/
  core/                # Django settings, celery init, конфиги (jwt, cache, swagger ...)
  apps/
    shared/            # Общие утилиты/базовые классы
    users/             # Кастомная модель пользователя и связанная логика
assets/
  static/              # Исходные статические файлы
  staticfiles/         # Собранные статики (collectstatic)
  locale/              # Файлы переводов (.po/.mo)
deployments/compose/   # Dockerfile + скрипты запуска
Taskfile.yml           # Автоматизация команд
pyproject.toml         # Зависимости и конфигурации инструментов
```

---

## 3. Стек технологий

- Django 5.2
- DRF, SimpleJWT
- drf-spectacular (+ sidecar swagger/redoc UI)
- Unfold admin + интеграции
- modeltranslation (полевая трансляция моделей)
- cors-headers, rosetta (удобный интерфейс переводов)
- CKEditor 5
- Celery + (Redis / RabbitMQ)
- Redis cache (django-redis)
- PostgreSQL
- uvicorn / gunicorn (продакшен ASGI/WSGI)
- ruff, mypy, deptry, pytest, coverage
- Taskfile (кросс-платформенная автоматизация)

---

## 4. Быстрый старт

### 4.1 Вариант A: Локально (uv)

```bash
# Установите uv (если нет)
pip install uv

# Установка зависимостей
uv sync

# Создайте .env (см. раздел Переменные окружения)
cp .env.example .env  # если добавите пример

# Применить миграции и создать суперпользователя
uv run python src/manage.py migrate
uv run python src/manage.py createsuperuser

# Запуск dev-сервера
uv run python src/manage.py runserver 0.0.0.0:8000
```

### 4.2 Вариант B: Docker

```bash
# Запуск только веб + postgres
docker compose up -d --build

# Логи
docker compose logs -f web

# Применить миграции (если не в entrypoint)
docker compose exec web python manage.py migrate

# Создать админа
docker compose exec web python manage.py createadmin
```

### 4.3 Включение фоновых сервисов (Celery / Redis / RabbitMQ / Flower)

В `docker-compose.yml` раскомментируйте нужные блоки: `redis`, `rabbitmq`, `celery_worker`, `celery_beat`,
`celery_flower`. Затем:

```bash
docker compose up -d --build
```

---

## 5. Переменные окружения

Минимальный набор (пример `.env`):

```
SECRET_KEY=changeme
DEBUG=true
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000

POSTGRES_DB=django
POSTGRES_USER=django
POSTGRES_PASSWORD=django
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Кеш / Celery (Redis)
REDIS_CACHE_URL=redis://redis:6379/1
CACHE_TIMEOUT=300
CELERY_BROKER=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# RabbitMQ (если используете)
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest

# Порты
PORT=8001
CELERY_FLOWER=5555
```

Если используете внешний брокер (RabbitMQ) — обновите `CELERY_BROKER` на `amqp://user:pass@rabbitmq:5672//`.

---

## 6. Управление зависимостями (uv)

Команды:

```bash
uv sync                 # установить все группы (dev, test, lint, typecheck)
uv add <pkg>            # добавить зависимость
uv remove <pkg>         # удалить
uv pip compile          # обновить lock (если нужно вручную)
```

---

## 7. Management-команды

| Команда          | Назначение                                                    |
|------------------|---------------------------------------------------------------|
| `makeapp <name>` | Создать новое приложение в `apps/`, скорректировать `apps.py` |
| `secret_key`     | Сгенерировать новый SECRET_KEY                                |

Запуск:

```bash
python manage.py makeapp blog
```

---

## 8. API документация

Доступно после запуска:

- Swagger UI: `/api/schema/swagger-ui/`
- Redoc: `/api/schema/redoc/`
- OpenAPI JSON: `/api/schema/`

Конфигурация — `core/config/swagger.py` (при необходимости расширьте).

---

## 9. Аутентификация (SimpleJWT)

Настройки в `core/config/jwt.py`.

- Access token: 1 день
- Refresh token: 7 дней
- Заголовок: `Authorization: Bearer <token>`

Пример получения токена (если настроен эндпоинт):

```
POST /api/auth/token/  {"username": "...", "password": "..."}
```

---

## 10. Многоязычность

- Языки: en, uz, ru
- Переводы: `assets/locale/<lang>/LC_MESSAGES/django.po`
- Modeltranslation: `MODELTRANSLATION_LANGUAGES = ("uz", "ru", "en")`
- Базовый язык: `uz`

Генерация / компиляция сообщений:

```bash
python manage.py makemessages -l ru -l uz -l en
python manage.py compilemessages
```

Rosetta позволяет редактировать переводы через UI.

---

## 11. Админ-панель (Unfold)

Расширенный современный UI. Навигация и дополнительные настройки — см. файл `core/config/unfold_navigation.py`.
Добавляйте приложения в списки INSTALLED_APPS (через `PROJECT_APPS`).

---

## 12. Редактор (CKEditor 5)

Используйте `CKEditor5Field` для текстовых полей:

```python
from django_ckeditor_5.fields import CKEditor5Field

body = CKEditor5Field(config_name="default")
```

Настройку профилей можно вынести в `core/config/ckeditor5.py`.

---

## 13. Кеш и Redis

Конфигурация в `core/config/cache.py`. Пример ручного использования:

```python
from django.core.cache import cache

cache.set("key", "value", 60)
value = cache.get("key")
```

Сессии работают через кеш (`SESSION_ENGINE`).

---

## 14. Фоновая обработка задач (Celery)

Пример задачи:

```python
# apps/shared/tasks.py
from celery import shared_task


@shared_task
def add(x, y):
    return x + y
```

Запуск локально:

```bash
celery -A core worker -l info
celery -A core beat -l info
```

Flower (мониторинг):

```bash
celery -A core flower --port=5555
```

---

## 15. Качество кода (ruff, mypy, deptry, pre-commit)

Taskfile цели:

```bash
task lint      # ruff check
task format    # автоформат + фиксы
task typecheck # mypy
task deptry    # неиспользуемые зависимости
task all       # полный набор (как CI)
```

---

## 16. Тестирование

Создавайте тесты в `tests/` или внутри приложения (`apps/<app>/tests/`). Запуск:

```bash
uv run pytest -vv
```

Покрытие (пример):

```bash
uv run pytest --cov=apps --cov-report=term-missing
```

---

## 17. Логи и мониторинг

Расширяйте `core/config/logs.py` (если потребуется) для JSON-формата. Рекомендуется интеграция с Sentry / OpenTelemetry
в продакшене.

---

## 18. Docker / Продакшен рекомендации

- Используйте отдельный том для статики / медиа.
- Добавьте `collectstatic` и миграции в entrypoint.
- Настройте reverse proxy (nginx) + HTTPS.
- Настройте healthcheck endpoints (например, `/healthz`).

---

## 19. Обновление / Расширение

Добавление нового приложения:

```bash
python manage.py makeapp blog
```

Добавьте его в навигацию Unfold при необходимости.

---

## 20. Donate & Контакты

Автор: Jahongir Hakimjonov

- GitHub: https://github.com/JahongirHakimjonov
- Instagram: https://www.instagram.com/ja_kahn_gir/
- Telegram: https://t.me/jakhangir_blog

Поддержать:

- Buy Me Coffee: https://buymeacoffee.com/ja_khan_gir
- Tirikchilik: https://tirikchilik.uz/ja_khan_gir

<a href="https://pypi.org/project/django-default/"><img src="https://i0.wp.com/securityaffairs.com/wp-content/uploads/2021/08/PyPI.png?ssl=1" width="200" height="90" alt="pypi"></a>
<a href="https://buymeacoffee.com/ja_khan_gir"><img src="https://i.postimg.cc/cLwdq9pL/bmc-qr-2.png" width="160" height="160" alt="donate"></a>

---

## Star History

<a href="https://www.star-history.com/#JahongirHakimjonov/DjangoDefault&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=JahongirHakimjonov/DjangoDefault&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=JahongirHakimjonov/DjangoDefault&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=JahongirHakimjonov/DjangoDefault&type=Date" />
 </picture>
</a>

---

## Лицензия

MIT — см. файл LICENSE.

---

## TODO Идеи

- Пример GraphQL (Strawberry / Graphene)
- Интеграция Sentry
- GitHub Actions workflow пример
- Rate limiting / throttling расширенное
- Доп. RBAC поверх guardian/simple_history

PR приветствуются!
