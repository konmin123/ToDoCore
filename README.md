## ToDoCore

Это Rest Api сервер для сайта списка дел реализованный через DRF c авто-документацией Swagger. 

Установка: 

1. Склонируйте репозиторий:

```
git clone git@github.com:konmin123/ToDoCore.git
```

2. Создайте и активируйте вирутальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

3. Установите зависимости:

```
pip install -r requirements.txt
```  

4. Создайте текстовый файл .env.txt аналогично шаблону template.env.txt

5. Проведите миграции:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

6. Создайте суперпользователя:

```
python manage.py createsuperuser
```

7. Запустите тестовый сервер:

```
python manage.py runserver
```
