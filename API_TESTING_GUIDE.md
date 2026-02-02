# 🧪 API TESTING GUIDE

## Как тестировать API endpoints с Postman

---

## 📥 Установка Postman

1. Скачай Postman: https://www.postman.com/downloads/
2. Установи и запусти
3. Создай новый Workspace: "Movie Review API Tests"

---

## 🔌 API Endpoints для тестирования

### Base URL
```
http://127.0.0.1:8000/api/
```

---

## 1️⃣ GENRES API

### GET - List all genres
**Endpoint**: `GET http://127.0.0.1:8000/api/genres/`

**Headers**: Не требуется

**Response**:
```json
[
    {
        "id": 1,
        "name": "Action",
        "description": "Action movies",
        "movie_count": 5
    },
    {
        "id": 2,
        "name": "Drama",
        "description": "Dramatic films",
        "movie_count": 3
    }
]
```

### POST - Create new genre
**Endpoint**: `POST http://127.0.0.1:8000/api/genres/`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON):
```json
{
    "name": "Comedy",
    "description": "Funny movies that make you laugh"
}
```

**Response**:
```json
{
    "id": 3,
    "name": "Comedy",
    "description": "Funny movies that make you laugh",
    "movie_count": 0
}
```

---

## 2️⃣ MOVIES API

### GET - List all movies
**Endpoint**: `GET http://127.0.0.1:8000/api/movies/`

**Headers**: Не требуется

**Response**:
```json
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "The Shawshank Redemption",
            "description": "Two imprisoned men bond...",
            "release_year": 1994,
            "director": "Frank Darabont",
            "duration_minutes": 142,
            "genre": {
                "id": 2,
                "name": "Drama",
                "description": "Dramatic films",
                "movie_count": 3
            },
            "poster_url": "https://example.com/poster.jpg",
            "average_rating": 4.5,
            "review_count": 10,
            "created_at": "2026-02-01T10:00:00Z"
        }
    ]
}
```

### GET - Get specific movie
**Endpoint**: `GET http://127.0.0.1:8000/api/movies/1/`

**Headers**: Не требуется

**Response**: Включает все reviews для фильма

### POST - Create new movie
**Endpoint**: `POST http://127.0.0.1:8000/api/movies/`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON):
```json
{
    "title": "Inception",
    "description": "A thief who steals corporate secrets through dream-sharing technology",
    "release_year": 2010,
    "director": "Christopher Nolan",
    "duration_minutes": 148,
    "genre_id": 1,
    "poster_url": "https://example.com/inception.jpg"
}
```

### PUT - Update movie
**Endpoint**: `PUT http://127.0.0.1:8000/api/movies/1/`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON):
```json
{
    "title": "Inception (Updated)",
    "description": "Updated description",
    "release_year": 2010,
    "director": "Christopher Nolan",
    "duration_minutes": 148,
    "genre_id": 1
}
```

### DELETE - Delete movie
**Endpoint**: `DELETE http://127.0.0.1:8000/api/movies/1/`

**Headers**: Не требуется

**Response**: 204 No Content

### GET - Top rated movies
**Endpoint**: `GET http://127.0.0.1:8000/api/movies/top_rated/`

**Headers**: Не требуется

**Response**: Массив топ-20 фильмов по рейтингу

---

## 3️⃣ REVIEWS API

### GET - List all reviews
**Endpoint**: `GET http://127.0.0.1:8000/api/reviews/`

**Headers**: Не требуется

**Response**:
```json
{
    "count": 25,
    "next": "http://127.0.0.1:8000/api/reviews/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "movie": 1,
            "movie_title": "The Shawshank Redemption",
            "user": {
                "id": 1,
                "username": "john_doe",
                "email": "john@example.com"
            },
            "rating": 5,
            "title": "Masterpiece!",
            "comment": "One of the best films ever made...",
            "created_at": "2026-02-01T12:00:00Z",
            "updated_at": "2026-02-01T12:00:00Z"
        }
    ]
}
```

### GET - Get specific review
**Endpoint**: `GET http://127.0.0.1:8000/api/reviews/1/`

### POST - Create new review (requires authentication)
**Endpoint**: `POST http://127.0.0.1:8000/api/reviews/`

**Headers**:
```
Content-Type: application/json
```

**Note**: Требуется быть залогиненным в браузере или использовать session authentication

**Body** (raw JSON):
```json
{
    "movie": 1,
    "rating": 5,
    "title": "Amazing movie!",
    "comment": "This is one of the best movies I've ever seen. The acting was superb and the story was captivating from start to finish."
}
```

**Response**:
```json
{
    "id": 26,
    "movie": 1,
    "movie_title": "The Shawshank Redemption",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    },
    "rating": 5,
    "title": "Amazing movie!",
    "comment": "This is one of the best movies I've ever seen...",
    "created_at": "2026-02-02T10:30:00Z",
    "updated_at": "2026-02-02T10:30:00Z"
}
```

### PUT - Update review (only own review)
**Endpoint**: `PUT http://127.0.0.1:8000/api/reviews/1/`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON):
```json
{
    "movie": 1,
    "rating": 4,
    "title": "Good movie (updated)",
    "comment": "Updated my review after second viewing"
}
```

### DELETE - Delete review (only own review)
**Endpoint**: `DELETE http://127.0.0.1:8000/api/reviews/1/`

**Response**: 204 No Content

### GET - My reviews
**Endpoint**: `GET http://127.0.0.1:8000/api/reviews/my_reviews/`

**Note**: Требуется аутентификация

---

## 🔑 Аутентификация в Postman

Для endpoints, требующих аутентификации:

### Метод 1: Session Authentication (рекомендуется для тестирования)

1. Открой браузер
2. Зайди в админ-панель: `http://127.0.0.1:8000/admin/`
3. Залогинься
4. В Postman используй те же куки сессии

### Метод 2: Basic Auth в Postman

1. В Postman выбери вкладку "Authorization"
2. Type: "Basic Auth"
3. Username: твой юзернейм
4. Password: твой пароль

---

## 📊 Примеры тестовых сценариев

### Сценарий 1: Полный цикл создания фильма и отзыва

1. **Создать жанр**:
   ```
   POST /api/genres/
   Body: {"name": "Sci-Fi", "description": "Science Fiction"}
   ```

2. **Создать фильм**:
   ```
   POST /api/movies/
   Body: {
       "title": "Interstellar",
       "description": "Space exploration movie",
       "release_year": 2014,
       "director": "Christopher Nolan",
       "duration_minutes": 169,
       "genre_id": 1
   }
   ```

3. **Получить список фильмов**:
   ```
   GET /api/movies/
   ```

4. **Создать отзыв** (требует аутентификации):
   ```
   POST /api/reviews/
   Body: {
       "movie": 1,
       "rating": 5,
       "title": "Epic!",
       "comment": "Mind-blowing space adventure"
   }
   ```

5. **Получить топ фильмы**:
   ```
   GET /api/movies/top_rated/
   ```

### Сценарий 2: CRUD операции для отзыва

1. **Create**: POST /api/reviews/
2. **Read**: GET /api/reviews/1/
3. **Update**: PUT /api/reviews/1/
4. **Delete**: DELETE /api/reviews/1/

---

## ✅ Чек-лист для тестирования

### Genres
- [ ] GET /api/genres/ - список жанров
- [ ] POST /api/genres/ - создание жанра
- [ ] GET /api/genres/1/ - конкретный жанр
- [ ] PUT /api/genres/1/ - обновление жанра
- [ ] DELETE /api/genres/1/ - удаление жанра

### Movies
- [ ] GET /api/movies/ - список фильмов
- [ ] POST /api/movies/ - создание фильма
- [ ] GET /api/movies/1/ - конкретный фильм
- [ ] PUT /api/movies/1/ - обновление фильма
- [ ] DELETE /api/movies/1/ - удаление фильма
- [ ] GET /api/movies/top_rated/ - топ фильмов
- [ ] GET /api/movies/1/reviews/ - отзывы фильма

### Reviews
- [ ] GET /api/reviews/ - список отзывов
- [ ] POST /api/reviews/ - создание отзыва
- [ ] GET /api/reviews/1/ - конкретный отзыв
- [ ] PUT /api/reviews/1/ - обновление отзыва
- [ ] DELETE /api/reviews/1/ - удаление отзыва
- [ ] GET /api/reviews/my_reviews/ - мои отзывы

---

## 🎥 Примеры для демонстрации на защите

### 1. Показать GET запрос
```
GET http://127.0.0.1:8000/api/movies/
```
Результат: Список всех фильмов с пагинацией

### 2. Показать POST запрос
```
POST http://127.0.0.1:8000/api/reviews/
Body: {
    "movie": 1,
    "rating": 5,
    "title": "Excellent",
    "comment": "Great film!"
}
```
Результат: Созданный отзыв с ID

### 3. Показать PUT запрос
```
PUT http://127.0.0.1:8000/api/reviews/1/
Body: {
    "movie": 1,
    "rating": 4,
    "title": "Good (updated)",
    "comment": "Changed my mind"
}
```
Результат: Обновленный отзыв

### 4. Показать DELETE запрос
```
DELETE http://127.0.0.1:8000/api/reviews/1/
```
Результат: 204 No Content

---

## 📸 Сохранение результатов для защиты

1. Делай скриншоты каждого успешного запроса
2. Покажи Response с данными
3. Покажи Status Code (200, 201, 204)
4. Сохрани в папку `postman_screenshots/`

---

## 🐛 Troubleshooting

### Ошибка: 403 Forbidden при POST
**Решение**: Залогинься в админ-панели в браузере

### Ошибка: 404 Not Found
**Решение**: Проверь URL и убедись что сервер запущен

### Ошибка: 400 Bad Request
**Решение**: Проверь формат JSON в Body

### Ошибка: CSRF token missing
**Решение**: Используй session auth через браузер или отключи CSRF для API в settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}
```

---

Готово! Теперь можешь тестировать все API endpoints! 🚀
