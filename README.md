# 🎬 Movie Review System

A Django-based web application for movie reviews and ratings.

## 👥 Team Members

- **Participant 1**: Models, Admin Panel, Database
- **Participant 2**: HTML Templates, CSS Styling
- **Participant 3**: Views, URLs, Forms
- **Participant 4**: REST API Endpoints
- **Participant 5**: Documentation, Deployment

## 📋 Features

### Core Features
- ✅ Browse movies with filters and sorting
- ✅ View detailed movie information
- ✅ User authentication system
- ✅ Write, edit, and delete reviews
- ✅ Star rating system (1-5 stars)
- ✅ Top rated movies page
- ✅ Search functionality
- ✅ Responsive design

### Admin Features
- ✅ Django Admin panel
- ✅ Manage movies, reviews, and genres
- ✅ View statistics and ratings
- ✅ Custom admin interface

### API Features
- ✅ RESTful API endpoints
- ✅ CRUD operations for movies and reviews
- ✅ JSON responses
- ✅ Pagination support

## 🛠️ Technologies Used

- **Backend**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, Django Templates
- **Styling**: Custom CSS with gradients and animations

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd movie_review_project
```

2. **Create virtual environment**
```bash
python -m venv venv
```

3. **Activate virtual environment**
- Windows:
```bash
venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

7. **Load sample data (optional)**
```bash
python manage.py loaddata sample_data.json
```

8. **Run development server**
```bash
python manage.py runserver
```

9. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/

## 📂 Project Structure

```
movie_review_project/
├── movie_review/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── movies/                # Main app
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   ├── forms.py          # Django forms
│   ├── admin.py          # Admin configuration
│   ├── serializers.py    # API serializers
│   ├── api_views.py      # API views
│   └── api_urls.py       # API routing
├── templates/            # HTML templates
│   └── movies/
│       ├── base.html
│       ├── home.html
│       ├── movie_detail.html
│       ├── add_review.html
│       ├── top_rated.html
│       └── search_results.html
├── static/               # Static files
│   └── css/
│       └── style.css
├── manage.py
└── requirements.txt
```

## 🗃️ Database Models

### Genre
- `name`: Genre name (unique)
- `description`: Genre description

### Movie
- `title`: Movie title
- `description`: Movie description
- `release_year`: Year of release
- `director`: Director name
- `duration_minutes`: Movie duration
- `genre`: Foreign key to Genre
- `poster_url`: URL to movie poster
- `created_at`, `updated_at`: Timestamps

### Review
- `movie`: Foreign key to Movie
- `user`: Foreign key to User
- `rating`: Integer (1-5)
- `title`: Review title
- `comment`: Review text
- `created_at`, `updated_at`: Timestamps

## 🔌 API Endpoints

### Movies
- `GET /api/movies/` - List all movies
- `POST /api/movies/` - Create new movie
- `GET /api/movies/{id}/` - Get movie details
- `PUT /api/movies/{id}/` - Update movie
- `DELETE /api/movies/{id}/` - Delete movie
- `GET /api/movies/top_rated/` - Get top rated movies
- `GET /api/movies/{id}/reviews/` - Get movie reviews

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create review (auth required)
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review (own only)
- `DELETE /api/reviews/{id}/` - Delete review (own only)
- `GET /api/reviews/my_reviews/` - Get current user's reviews

### Genres
- `GET /api/genres/` - List all genres
- `POST /api/genres/` - Create genre
- `GET /api/genres/{id}/` - Get genre details
- `PUT /api/genres/{id}/` - Update genre
- `DELETE /api/genres/{id}/` - Delete genre

## 🧪 Testing API with Postman

### Example: Create a Review
**Endpoint**: `POST /api/reviews/`

**Headers**:
```
Content-Type: application/json
```

**Body** (JSON):
```json
{
    "movie": 1,
    "rating": 5,
    "title": "Amazing movie!",
    "comment": "This is one of the best movies I've ever seen. The acting was superb and the story was captivating."
}
```

### Example: Get Top Rated Movies
**Endpoint**: `GET /api/movies/top_rated/`

No body required.

## 🚀 Deployment

### Using PythonAnywhere (Free)

1. Create account at [PythonAnywhere](https://www.pythonanywhere.com/)

2. Upload your code via Git or zip file

3. Create virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

4. Configure WSGI file

5. Set `ALLOWED_HOSTS` in settings.py:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Run migrations:
```bash
python manage.py migrate
```

8. Create superuser and reload web app

### Using Render (Free)

1. Create account at [Render](https://render.com/)
2. Create new Web Service
3. Connect your GitHub repository
4. Configure build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
5. Configure start command: `gunicorn movie_review.wsgi`
6. Add environment variables
7. Deploy!

## 🎯 Assignment Requirements Checklist

### Assignment 6
- ✅ 3 Django models (Genre, Movie, Review)
- ✅ Database migrations
- ✅ Django Admin panel configured
- ✅ 2+ HTML templates with DTL
- ✅ CSS styling
- ✅ 2+ API endpoints

### Assignment 8
- ✅ 4 HTML templates
- ✅ Template inheritance
- ✅ Loops and conditionals in templates
- ✅ Dynamic data from database
- ✅ Separate CSS file
- ✅ Static files configured
- ✅ 3+ API endpoints (GET, POST, PUT, DELETE)
- ✅ Ready for deployment

## 👨‍💻 Usage Guide

### For Regular Users

1. **Browse Movies**: Visit homepage to see all movies
2. **Filter & Sort**: Use dropdown menus to filter by genre or sort
3. **Search**: Use search bar to find specific movies
4. **View Details**: Click "View Details" to see movie information and reviews
5. **Write Review**: Login and click "Write a Review" on movie page
6. **Top Rated**: Visit "Top Rated" page to see highest rated movies

### For Administrators

1. **Login to Admin**: Go to `/admin/` and login
2. **Add Movies**: Click "Movies" → "Add Movie"
3. **Manage Reviews**: View, edit, or delete user reviews
4. **View Statistics**: See average ratings and review counts
5. **Manage Genres**: Add or edit movie genres

## 🐛 Troubleshooting

### Common Issues

**Problem**: Static files not loading
**Solution**: 
```bash
python manage.py collectstatic
```

**Problem**: Database errors
**Solution**:
```bash
python manage.py makemigrations
python manage.py migrate
```

**Problem**: Admin panel not accessible
**Solution**: Create superuser:
```bash
python manage.py createsuperuser
```

## 📝 Future Enhancements

- User profiles
- Movie recommendations
- Social features (follow users)
- Advanced search filters
- Movie trailers integration
- Email notifications
- Comment replies
- Movie watchlist

## 📄 License

This project is created for educational purposes as part of Django Web Development course.

## 🤝 Contributing

This is a group project. Each team member is responsible for specific components:

1. **Database & Models**: Participant 1
2. **Frontend Design**: Participant 2
3. **Backend Logic**: Participant 3
4. **API Development**: Participant 4
5. **Documentation & Deployment**: Participant 5

## 📞 Support

For questions or issues, contact your team members or course instructor.

---

**Assignment**: Django Web Development - Assignment 6 & 8
**Deadline**: February 2, 2026
**Status**: ✅ Complete and ready for submission
