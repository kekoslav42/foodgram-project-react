![foodgram](https://github.com/kekoslav42/foodgram-project-react/workflows/foodgram/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
# foodgram-project-react

# Описание
    
Продуктовый помощник - приложение где пользователи могут публиковать свои рецепты,
добавлять рецепты других пользователей в избранное, а так же добавлять в список покупок,
что дает возможность скачать файл .txt со всеми ингредиентами

**[Пока что доступен тут](http://51.250.30.120/recipes)** --> **[документация API](http://51.250.30.120/api/docs/)**

## Для авторизованных пользователей доступны:

Главная страница.

Страница другого пользователя.

Страница отдельного рецепта.

Страница «Мои подписки».

Страница «Избранное».

Страница «Список покупок».

Страница «Создать рецепт».

## Для неавторизованных пользователей доступны:

Главная страница.

Страница отдельного рецепта.

Страница любого пользователя.

Страница авторизации.

Страница регистрации.


# Запуск на локальном сервере

1. Клонировать репозиторий

```bash
git clone https://github.com/kekoslav42/foodgram-project-react.git
```

2. Установить docker и docker-compose

Инструкция по установке доступна в официальной инструкции

3. В папке с проектом перейти в infra и создать файл .env

Добавить следующее содержимое
```
SECRET_KEY = Секретный ключ django
ALLOWED_HOSTS = Разрешенные подключения
DB_ENGINE= django.db.backends.postgresql
DB_NAME= Имя базы данных
POSTGRES_USER= Пользователь базы данных
POSTGRES_PASSWORD= Пароль базы данных
DB_HOST= Хост базы данных
DB_PORT= Порт базы данных
```
4. В папке infra выполнить команду
```
docker-compose up
```

## Запуск на удаленном сервере
1. В папке с проектом перейти в infra и создать файл .env 
с таким же содержимым как и для запуска на локальном сервере
2. Копировать файлы из папки infra на сервер
```
scp docker-compose.yaml <user>@<server-ip>:
scp .env <user>@<server-ip>:
scp nginx.conf <user>@<server-ip>:
```

3. Cоздать переменные окружения в разделе `secrets` гитхаб репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USER # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TG_CHAT_ID # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
```
4. В nginx.conf указать server_name(ip or domain)

### При пуше в master:
1. Проверка кода на соответствие стандарту PEP8
2. Сборка докер-образов.
3. Пуш на DockerHub.
3. Деплой на удаленный сервер.
4. Информирование в телеграмм.

### Автор
Maksim Rumyantsev - 
**[GitHub](https://github.com/kekoslav42/)** -
**[Telegram](https://t.me/Maksim_Rumyantsev)** - 
**[VK](https://vk.com/maksim_rumyancev)** 