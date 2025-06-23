# Django TO DO List

A simple TO DO List web application built with Django.

## Features

- Add, edit, and delete tasks
- Mark tasks as complete or incomplete
- Simple, clean UI

## Requirements

- Python 3.8+
- Django 4.x

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/django-todo-list.git
   cd django-todo-list
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
django-todo-list/
├── manage.py
├── todo/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todo_list/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```
