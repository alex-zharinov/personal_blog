### Personal Blog

## API для персонального блога
> API позволяет взаимодействовать с блогом

## Технологии проекта:
- Python — высокоуровневый язык программирования;
- Django REST Framework — библиотека, используемая в Django для создания Rest API;

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/alex-zharinov/personal_blog.git
```
```
cd personal_blog
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Создать .env. Пример:
```
#  ./.env

SECRET_KEY=SUP3R-S3CR3T-K3Y-F0R-MY-PR0J3CT
```
Создать БД:
```
python3 blog/manage.py migrate
```
Запустить проект:
```
python3 blog/manage.py runserver
```

### Ваш проект будет доступен по ссылке:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Примеры запросов:
- Получить список всех публикаций:
```
GET /api/v1/blogs/
```
- Создать публикацию (только для авторизовнных пользователей):
```
POST /api/v1/blogs/
```
Request samples:
```
{
  "title": "string",
  "text": "string",
}
```
- Удалить публикацию (только для автора публикации):
```
DELETE /api/v1/blogs/{id}/
```
- Ознакомиться с полныйм списком запросов можно в документации:
```
GET /api/doc/
```

## Автор
[Жаринов Алексей](https://github.com/alex-zharinov)
