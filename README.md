# Learning Management System Backend

## Overview

This repository contains the backend code for a Learning Management System (LMS) built using Django and Django Rest Framework (DRF). 

## Features

- **Course Management**: Create, update, delete, and retrieve courses.
- **Assignment Management**: Manage assignments associated with courses.
- **Schedule Management**: Manage course schedule associated with courses.
- **Gradebook**: Record and retrieve student grades.
- **Student Progress Tracking**: Monitor student progress through courses and assignments.

## Technologies Used

- **Python**: Programming language.
- **Django**: Web framework for building the backend.
- **Django Rest Framework (DRF)**: Toolkit for building Web APIs.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/OLPC-TONYE/codecampus_backend.git
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

5. **Run database migrations**

```bash
python manage.py migrate
```

6. **Run the development server**

```bash
python manage.py runserver
```

2. **Access the application**

The application will be accessible at `http://localhost:8000/api/v1/`.

## API Documentation

The API documentation is in progress

