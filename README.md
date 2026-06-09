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

git clone <repository_url>
cd souvenir-shop-backend 

### 2. Создать виртуальное окружение

python -m venv venv
source venv/bin/activate 

Для Windows:

venv\Scripts\activate 

### 3. Установить зависимости

pip install -r requirements.txt 

### 4. Создать файл .env

Скопировать пример:

cp .env.example .env 

При необходимости изменить значения переменных.

### 5. Выполнить миграции

python manage.py migrate 

### 6. Создать администратора

python manage.py createsuperuser 

### 7. Заполнить тестовые данные

python manage.py seed_products 

### 8. Запустить сервер

python manage.py runserver 

Backend будет доступен по адресу:

http://127.0.0.1:8000 

Административная панель:

http://127.0.0.1:8000/admin 

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

data/db.sqlite3 

Каталог data/ подготовлен для дальнейшего подключения Docker Volume.

## API

Основные эндпоинты:

- GET  /api/products/
- GET  /api/categories/
- POST /api/orders/
- GET  /api/feedback/