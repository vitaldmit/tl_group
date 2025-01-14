# Django-приложение выводит древовидную структуру отделов со списком сотрудников.

1. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv tl_group
cd tl_group
. bin/activate
pip install --upgrade pip
mkdir src
cd src
```

2. Клонируйте репозиторий:
```bash
https://github.com/vitaldmit/tl_group.git .
```

3. Установите зависимости:
```bash
pip install -r requirements-dev.txt
```

4. Создайте `.env` файл на основе шаблона:
```bash
cp env.example .env
```

5. Запустите проверку:
```bash
python manage.py check
```

6. Запустите сервер:
```bash
python manage.py runserver
```

7. Перейдите по адресу [http://127.0.0.1:8000/employee/](http://127.0.0.1:8000/employee/)
