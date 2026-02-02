# 🚀 DEPLOYMENT GUIDE

## Как задеплоить проект на бесплатный сервер

---

## Вариант 1: PythonAnywhere (Рекомендуется)

### ✅ Преимущества:
- Полностью бесплатный
- Простая настройка
- Поддержка Django
- Бесплатная база данных

### 📋 Пошаговая инструкция:

#### 1. Регистрация

1. Иди на https://www.pythonanywhere.com/
2. Нажми "Pricing & signup"
3. Выбери "Create a Beginner account" (бесплатный)
4. Зарегистрируйся

#### 2. Загрузка кода

**Вариант A: Через GitHub (рекомендуется)**

1. Зайди в консоль (Consoles → Bash)
2. Клонируй репозиторий:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

**Вариант B: Через ZIP**

1. В меню "Files" → Upload a file
2. Загрузи ZIP с проектом
3. Распакуй: `unzip movie_review_project.zip`

#### 3. Создание виртуального окружения

```bash
cd movie_review_project
mkvirtualenv --python=/usr/bin/python3.10 movieenv
pip install -r requirements.txt
```

#### 4. Настройка базы данных

```bash
python manage.py migrate
python manage.py createsuperuser
```

#### 5. Сбор статических файлов

Отредактируй `movie_review/settings.py`:
```python
STATIC_ROOT = '/home/YOUR_USERNAME/movie_review_project/staticfiles'
```

Затем:
```bash
python manage.py collectstatic
```

#### 6. Настройка Web App

1. Иди в "Web" → "Add a new web app"
2. Выбери "Manual configuration"
3. Выбери Python 3.10

#### 7. Конфигурация WSGI

1. Кликни на WSGI configuration file
2. Удали всё содержимое
3. Вставь:

```python
import os
import sys

# Путь к твоему проекту
path = '/home/YOUR_USERNAME/movie_review_project'
if path not in sys.path:
    sys.path.append(path)

# Настройка Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'movie_review.settings'

# Загрузка Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**ВАЖНО**: Замени `YOUR_USERNAME` на твой username в PythonAnywhere!

#### 8. Настройка Virtual Environment

1. В разделе "Web" найди "Virtualenv"
2. Введи путь: `/home/YOUR_USERNAME/.virtualenvs/movieenv`

#### 9. Настройка Static Files

1. В разделе "Static files"
2. Добавь:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/movie_review_project/staticfiles`

#### 10. Обновление settings.py

Отредактируй `movie_review/settings.py`:

```python
# ВАЖНО: Добавь свой домен
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com', 'localhost', '127.0.0.1']

# DEBUG можно оставить True для тестирования
DEBUG = True

# Для production рекомендуется:
# DEBUG = False
```

#### 11. Перезагрузка

1. Нажми зеленую кнопку "Reload YOUR_USERNAME.pythonanywhere.com"
2. Подожди 10-20 секунд

#### 12. Проверка

Открой: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Вариант 2: Render.com

### ✅ Преимущества:
- Автоматический деплой из GitHub
- HTTPS включен
- Современная платформа

### 📋 Пошаговая инструкция:

#### 1. Подготовка файлов

Создай файл `build.sh` в корне проекта:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

Сделай его исполняемым:
```bash
chmod +x build.sh
```

#### 2. Обновление requirements.txt

Добавь:
```
gunicorn==21.2.0
psycopg2-binary==2.9.9
dj-database-url==2.1.0
whitenoise==6.6.0
```

#### 3. Обновление settings.py

Добавь в начало файла:
```python
import dj_database_url
```

Замени DATABASES на:
```python
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

Добавь whitenoise в MIDDLEWARE (после SecurityMiddleware):
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Добавь эту строку
    # ...остальное
]
```

Добавь настройки статики:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### 4. Регистрация на Render

1. Иди на https://render.com/
2. Sign Up через GitHub
3. Подтверди email

#### 4. Создание Web Service

1. Нажми "New +" → "Web Service"
2. Выбери свой репозиторий
3. Настройки:
   - **Name**: movie-review-system
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn movie_review.wsgi:application`

#### 5. Environment Variables

Добавь:
- `PYTHON_VERSION`: `3.10.0`
- `SECRET_KEY`: (сгенерируй новый ключ)

#### 6. Deploy

1. Нажми "Create Web Service"
2. Подожди 5-10 минут
3. Проверь URL: `https://YOUR_SERVICE.onrender.com`

---

## Вариант 3: Railway.app

### 📋 Быстрая инструкция:

1. Зарегистрируйся на https://railway.app/
2. "New Project" → "Deploy from GitHub repo"
3. Выбери репозиторий
4. Railway автоматически определит Django
5. Добавь environment variables:
   - `PORT`: 8000
   - `DJANGO_SETTINGS_MODULE`: movie_review.settings
6. Deploy!

---

## 🔧 Общие настройки безопасности

### Для production (когда DEBUG=False):

1. **Сгенерируй новый SECRET_KEY**:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

2. **Обнови settings.py**:
```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
```

3. **Используй переменные окружения**

---

## 🐛 Troubleshooting

### Ошибка: DisallowedHost

**Решение**: Добавь домен в ALLOWED_HOSTS:
```python
ALLOWED_HOSTS = ['yourapp.pythonanywhere.com', 'localhost']
```

### Ошибка: Static files not loading

**Решение**: 
```bash
python manage.py collectstatic --clear
```

### Ошибка: Database errors

**Решение**: 
```bash
python manage.py migrate --run-syncdb
```

### Ошибка: ImportError

**Решение**: Проверь что все зависимости в requirements.txt

---

## ✅ Чек-лист перед деплоем

- [ ] `requirements.txt` актуален
- [ ] Все миграции созданы и применены
- [ ] `ALLOWED_HOSTS` настроен
- [ ] `STATIC_ROOT` настроен
- [ ] `collectstatic` выполнен
- [ ] Создан superuser
- [ ] База данных заполнена тестовыми данными
- [ ] Все endpoints работают локально
- [ ] `.gitignore` правильно настроен

---

## 📝 После деплоя

1. **Создай суперюзера на сервере**:
```bash
python manage.py createsuperuser
```

2. **Добавь тестовые данные** через админ-панель

3. **Протестируй все функции**:
   - Регистрация/логин
   - Создание отзывов
   - API endpoints
   - Админ-панель

4. **Сохрани URL** для защиты проекта

---

## 🎯 Для защиты проекта

Покажи:
1. ✅ Живой URL сайта
2. ✅ Работающую админ-панель
3. ✅ Создание/редактирование отзывов
4. ✅ API endpoints через Postman

---

## 💡 Советы

- **PythonAnywhere** - самый простой вариант для начинающих
- **Render** - лучше для автоматического деплоя
- **Railway** - быстрый setup, но меньше бесплатных ресурсов

Выбирай тот, который тебе удобнее!

---

Удачи с деплоем! 🚀
