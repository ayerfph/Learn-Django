# Django Learning Playground

This repository is a hands-on playground for learning Django, following along with [Programming with Mosh's Django Tutorial for Beginners](https://www.youtube.com/watch?v=rHux0gMZ3Eg).

## Project Structure

```
storefront/
├── manage.py
├── Pipfile
├── db.sqlite3
├── playground/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── hello.html
└── storefront/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/django-learning-playground.git
   cd django-learning-playground
   ```

2. **Install dependencies:**
   ```sh
   pip install pipenv
   pipenv install
   pipenv shell
   ```

3. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

4. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

5. **Visit the playground app:**
   Open [http://127.0.0.1:8000/playground/hello/](http://127.0.0.1:8000/playground/hello/) in your browser.

## Features

- Simple Django project setup
- Example app (`playground`) with a template
- Clean project structure for beginners

## Reference

- [Django Tutorial for Beginners - Full Course in 1 Hours [2022]](https://www.youtube.com/watch?v=rHux0gMZ3Eg) by Programming with Mosh

## License

This project
