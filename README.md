# Тестовое задание в ООО "Ришат"

Решение доступно по ссылке: http://89.108.76.94/order/1

Панель администратора: http://89.108.76.94/admin

Логин и пароль от админки: `admin`, `admin`

## Запуск локально

Для запуска задания локально нужно создать `.env` файл на основе примера из `.env.example`:

```
# Database variables
POSTGRES_USER="django"
POSTGRES_PASSWORD="django"
POSTGRES_DB="test"

# Application variables
DATABASE_NAME="test"
DATABASE_USER="django"
DATABASE_PASSWORD="django"
DATABASE_HOST="db"
DATABASE_PORT="5432"
SECRET_KEY="django_secret"
STRIPE_KEY="sk_test_123123"
```

После того, как файл создан, есть два варианта запуска задания

### С использованием docker

Для этого необходимо запустить команду

```
docker-compose -f docker-compose-dev.yml up --build
```

Или, если вы используете `docker-compose-plugin`, то

```
docker compose -f docker-compose-dev.yml up --build
```

#### Через скрипты pdm

Если у вас есть [`pdm`](https://pdm.fming.dev/latest/), то можно использовать уже готовый
скрипт, использующий `docker-compose-plugin`:

```
pdm run docker-dev
```

### Запуск локально

Для того, чтобы запустить проект локально, нужно установить
[`pdm`](https://pdm.fming.dev/latest/) и выполнить следующие команды:

```
pdm install
pdm run dev
```

> Для правильного запуска **ОБЯЗАТЕЛЬНО** нужно создать `.env` файл

## Запуск в production

Команда для поднятия production окружения в Docker:

```
docker compose -f docker-compose-prod.yml up --build -d
```

> Для этой команды необходим `.env.prod` файл

# Автор

- Лоскан Артем - [`artemowkin`](https://github.com/artemowkin)