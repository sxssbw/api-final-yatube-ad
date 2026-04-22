# API для Yatube

API для социальной сети Yatube. Позволяет публиковать посты, оставлять комментарии, подписываться на авторов и управлять своим контентом. 

## Технологии

- Python 3.9
- Django 3.2
- Django REST Framework
- Simple JWT (аутентификация)
- pytest (для тестов)

## Функциональность

- Регистрация и аутентификация пользователей (JWT).
- CRUD для постов (создание, чтение, обновление, удаление).
- Комментирование постов.
- Подписки на авторов.
- Фильтрация и поиск.
- Права доступа: только автор может редактировать/удалять свой контент.
- Документация API доступна по адресу `/redoc/`.

## Установка и запуск

### 1. Клонировать репозиторий

git clone https://github.com/sxssbw/api_yatube

### 2. Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/Scripts/activate

### 3. Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

### 4. Выполнить миграции:

python manage.py migrate

### 5. Запустить проект:

python manage.py runserver

## Примеры запросов

### Получение списка всех постов
GET /api/v1/posts/

### Создание нового поста (требуется авторизация)
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
"text": "Текст нового поста",
"group": 1
}

### Получение информации о конкретном посте
GET /api/v1/posts/{post_id}/

### Удаление поста (только автор)
DELETE /api/v1/posts/{post_id}/
Authorization: Bearer <access_token>

### Добавление комментария к посту (требуется авторизация)
POST /api/v1/posts/{post_id}/comments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
"text": "Текст комментария"
}

### Редактирование комментария (только автор)
PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
"text": "Измененный комментарий"
}

## Автор
sxssbw