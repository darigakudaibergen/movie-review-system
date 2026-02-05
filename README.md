# Movie Review System

This is a Django project created for a university assignment (Topic 12).
The website allows users to browse movies, view details and read or add reviews.
The admin panel is used to manage movies, genres and reviews.

## How to run the project locally

1. Create virtual environment:
   python -m venv venv

2. Activate virtual environment:
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate

5. Create admin user:
   python manage.py createsuperuser

6. Run the server:
   python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

## Available pages

- Home page: http://127.0.0.1:8000/
- Top rated movies: http://127.0.0.1:8000/top-rated/
- Admin panel: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/

## Team contribution

This repository is a new project for Topic 12.
The previous project was completed earlier.

- Dariga — project setup, database models, admin panel, templates, CSS
- Participant 2 — API testing guide
- Participant 3 — documentation update
