# Souvenir Shop Backend

Backend часть дипломного проекта интернет-магазина корпоративной сувенирной продукции.

## Технологии

- Python 3.13
- Django 6
- Django REST Framework
- SQLite
- django-cors-headers

## Установка

### 1. Клонировать репозиторий

bash git clone <repository_url> cd souvenir-shop-backend 

### 2. Создать виртуальное окружение

bash python -m venv venv source venv/bin/activate 

Для Windows:

bash venv\Scripts\activate 

### 3. Установить зависимости

bash pip install -r requirements.txt 

### 4. Создать файл .env

Скопировать пример:

bash cp .env.example .env 

При необходимости изменить значения переменных.

### 5. Выполнить миграции

bash python manage.py migrate 

### 6. Создать администратора

bash python manage.py createsuperuser 

### 7. Заполнить тестовые данные

bash python manage.py seed_products 

### 8. Запустить сервер

bash python manage.py runserver 

Backend будет доступен по адресу:

text http://127.0.0.1:8000 

Административная панель:

text http://127.0.0.1:8000/admin 

## Переменные окружения

Пример находится в файле .env.example.

Основные переменные:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- CORS_ALLOWED_ORIGINS
- SQLITE_PATH
- STATIC_ROOT
- MEDIA_ROOT

## Структура хранения данных

База данных SQLite хранится в директории:

text data/db.sqlite3 

Каталог data/ подготовлен для дальнейшего подключения Docker Volume.

## API

Основные эндпоинты:

text GET    /api/products/ GET    /api/categories/ POST   /api/orders/ GET    /api/feedback/ 